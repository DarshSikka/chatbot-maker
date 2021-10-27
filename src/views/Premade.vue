<template>
  <div>
    <input
      type="text"
      v-model="msg"
      @keyup="ask"
      class="p-2 ml-10 ring-2 rounded-xl"
      :placeholder="`Talk to ${this.botname}`"
    />
    <div class="messages">
      <div :key="msg.message" v-for="msg in arr">
        <div
          :class="[
            msg.user ? 'bg-green-400' : 'bg-blue-400',
            'rounded-xl',
            'w-max p-4',
            msg.user ? 'ml-96' : 'ml-10',
          ]"
        >
          <b>{{ msg.user ? "You" : this.botname }}: </b>{{ msg.message }}
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { defineComponent } from "vue";
export default defineComponent({
  name: "Premade",
  data() {
    return {
      msg: "",
      arr: [],
      apiCall: "",
      botname: "",
    };
  },
  methods: {
    async ask(eve) {
      if (eve.key === "Enter") {
        this.arr.push({ message: this.msg, user: true });
        const req = await fetch(this.apiCall, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ question: this.msg }),
        });
        const res = await req.text();
        this.arr.push({ message: res, user: false });
        console.log(this.arr);
      }
    },
  },
  async mounted() {
    const params = this.$route.params;
    const uu = params.uuid;
    this.apiCall = `${this.$store.state.api}/bot/${uu}/api/response`;
    const prom = await fetch(`${this.$store.state.api}/bot/${uu}/name`);
    this.botname = await prom.text();
    console.log(this.botname);
    if (!this.botname) {
      alert("Not Found :(");
      window.location = "/#";
    }
  },
});
</script>
