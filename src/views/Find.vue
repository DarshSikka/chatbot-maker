<template>
  <div class="w-max mx-auto mt-16">
    <input
      type="text"
      placeholder="UUID"
      v-model="text"
      @keydown="go()"
      class="text-lg rounded p-2 ring-2 outline:ring-2"
    /><br />
    <router-link class="text-purple-900 mt-16" :to="this.bot">{{
      bot
    }}</router-link>
  </div>
</template>
<script>
export default {
  name: "Find",
  data() {
    return {
      text: "",
      bot: "",
    };
  },
  methods: {
    go() {
      this.bot = `/interface/${this.text}`;
    },
  },
};
</script>
