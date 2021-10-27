<template>
  <form
    @submit="handleSubmit"
    class="flex flex-col w-max mx-auto justify-around h-screen"
  >
    <div class="flex flex-col">
      <label class="text-purple-800 -mb-6 w-max bg-white">Name</label>
      <input
        v-model="models.name"
        type="text"
        placeholder="Name of the bot"
        class="ml-1 mt-5 p-2 ring-1 ring-purple-500 focus:ring-1 focus:ring-purple-900"
      />
    </div>
    <div class="flex flex-col">
      <label class="text-purple-800 -mb-6 w-max bg-white">Access Token</label>
      <input
        v-model="models.access_token"
        type="password"
        placeholder="Access token to edit"
        class="ml-1 mt-5 p-2
      ring-1 ring-purple-500 focus:ring-1 focus:ring-purple-900"
      />
    </div>
    <div class="flex flex-col">
      <label class="text-purple-800 -mb-6 w-max bg-white"
        >Upload .chatbot / .json</label
      >
      <input
        type="file"
        class="ml-1 mt-5 p-2 ml-1 mt-5 p-2 ring-1 ring-purple-500 focus:ring-1 focus:ring-purple-900"
      />
    </div>
    <p
      v-if="flash.TEXT"
      :class="[
        flash.ERROR ? 'bg-red-900' : 'bg-green-900',
        'text-white',
        'p-2',
      ]"
    >
      {{ flash.TEXT }}
    </p>
    <button class="p-4 bg-blue-700 text-white hover:bg-blue-800 cursor-pointer">
      Save New form of bot
    </button>
  </form>
</template>
<script>
export default {
  name: "EditBot",
  data() {
    return {
      flash: { ERROR: true, TEXT: "" },
      models: {
        name: "",
        access_token: "",
      },
    };
  },
  methods: {
    async handleSubmit(e) {
      e.preventDefault();
      const status_to_message = {
        404: "404: Not found with the bot name :(",
        401: "Unauthorized: wrong access token :(",
        200: "Booyah: GenZ loaded into your chatbot :)",
      };
      const [_, $, filer] = e.target;
      const reader = new FileReader();
      reader.onload = async (e) => {
        const json = e.target.result;
        console.log(json);
        const url = `${this.$store.state.api}/bot/${this.models.name}/update`;
        const body = JSON.stringify({
          intents: json,
          ACCESS_TOKEN: this.models.access_token,
        });
        const headers = {
          "Content-Type": "application/json",
        };
        const request = { body, headers, method: "POST" };
        let response = await fetch(url, request);
        response = await response.json();
        this.flash = {
          ERROR: response.error,
          TEXT: status_to_message[response.STATUS],
        };
      };

      reader.readAsText(filer.files[0]);
    },
  },
};
</script>
<style>
label {
  z-index: 1000;
}
</style>
