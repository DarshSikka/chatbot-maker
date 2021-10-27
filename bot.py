import json
class Bot:
    '''
    Initializes a Bot.
    Pass `intents=<path to a json file>` in order to initialize
    '''
    def __init__(self, intents):
        with open(intents, 'r') as file:
            self.intents=json.load(file)
    def get_intents(self):
        return self.intents
    def get_response(self, question):
        most_priority={'resp': "Sorry, didn't catch you. Try again?",'priority': -5}
        for intent in self.intents:
            priorities=[n for n in intent['keywords'] if n['keyword'].lower() in question.lower()]
            if(len(priorities)>0):
                if intent['priority']>most_priority['priority']:
                    most_priority={'resp': intent['resp'], 'priority':intent['priority']}
        return most_priority['resp']