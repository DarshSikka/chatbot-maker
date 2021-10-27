from flask import Flask, request, flash, redirect, send_file
from flask_cors import CORS
from uuid import uuid4
from bot import Bot
import json
import sqlite3
app=Flask(__name__, static_url_path="/", static_folder="static/dist")
CORS(app)
@app.route("/", methods=["GET"])
def home():
    return send_file('static/dist/index.html')
@app.route("/bot", methods=["POST"])
def new_bot():
    print(request.get_json())
    title=request.get_json()['title']
    intents=request.get_json()['intents']
    access_token=request.get_json()['access_token']
    uid=str(uuid4())
    conn=sqlite3.connect("db.sqlite3")
    cur=conn.cursor()
    cur.execute('''SELECT * FROM main WHERE title=?''', (title, ))
    da=cur.fetchall()
    if len(da)>=1:
        return {'ERROR':True, 'MESSAGE':'Name Taken'}
    cur.execute('''
    INSERT INTO main(title, id, access_token) VALUES (?, ?, ?)
    ''', (title, uid, access_token))
    conn.commit()
    with open(f"chat/{uid}.json", 'w') as f:
        f.write(json.dumps(intents))
    return {
        'ERROR':False,
        'MESSAGE':"success",
        'ID':uid
    }
@app.route("/bot/<botid>/api/response", methods=["POST"])
def post_resp(botid):
    conn=sqlite3.connect("db.sqlite3")
    cur=conn.cursor()
    cur.execute('''
    SELECT * FROM main WHERE id = ?
    ''', (botid,))
    bot=cur.fetchone()
    if(not bot):
        return "Bot not found :("
    bot_model=Bot(f"chat/{bot[1]}.json")
    return bot_model.get_response(request.get_json()['question'])
@app.route("/bot/<botid>/name")
def naming(botid):
    conn=sqlite3.connect("db.sqlite3")
    cur=conn.cursor()
    cur.execute('''SELECT * FROM main WHERE id = ?''', (botid, ))
    nam=cur.fetchone()
    if nam:
        return nam[0]
    else: 
        return ""
@app.route("/bot/<botid>/update", methods=["POST"])
def edit(botid):
    body=request.get_json()
    conn=sqlite3.connect("db.sqlite3")
    cur=conn.cursor()
    cur.execute('SELECT * FROM main WHERE title=?', (botid, ))
    data=cur.fetchone()
    if not data:
        return {'ERROR': True,'STATUS': 404}
    elif data[2]==body['ACCESS_TOKEN']:
        with open(f'''chat/{data[1]}.json''', 'w') as f:
            f.write(body['intents'])
        return {'ERROR': False, 'STATUS': 200}
    else: 
        return {'ERROR': True, 'STATUS': 401}
if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")