<template>
  <div class="flex flex-col items-center">
    <form @submit="submit">
      <div class="flex flex-col mt-16">
        <input
          type="text"
          id="title"
          class="p-2 border-2 border-purple-900"
          @focus="input_change"
          @focusout="input_back"
        />
        <label
          :class="[label, 'cursor-text', 'ml-2', 'bg-white', 'w-max']"
          for="title"
          >Bot Name</label
        >
      </div>
      <div class="flex flex-col mt-16">
        <input
          type="password"
          id="password"
          class="p-2 border-2 border-purple-900"
          @focus="pass_change"
          @focusout="pass_out"
        />
        <label
          :class="[passlabel, 'curor-text', 'ml-2', 'bg-white', 'w-max']"
          for="password"
          >Access Token</label
        >
      </div>
      <textarea type="text" class="hidden" readonly :value="file"></textarea>
      <button
        type="submit"
        class="p-2 mt-16 bg-blue-900 text-white hover:bg-blue-800 ml-12"
      >
        Submit
      </button>
    </form>
    <input type="file" @change="filer" class="mt-12" />
    <p
      :class="[
        flash.ERROR ? 'bg-red-900' : 'bg-green-900',
        'p-2',
        'text-white',
        'mt-12',
      ]"
    >
      {{ flash.MESSAGE }}
    </p>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
interface HTMLFormEvent {
  target: Array<HTMLInputElement>;
  preventDefault: Function;
}
export default defineComponent({
  name: "",
  data() {
    return {
      file: "",
      label: "-mt-9",
      passlabel: "-mt-9",
      flash: { ERROR: false, MESSAGE: "" },
    };
  },
  methods: {
    filer(e: { target: HTMLInputElement }) {
      const fdr = new FileReader();
      fdr.onload = (eve) => {
        this.file = String(eve.target!.result);
      };
      fdr.readAsText(e!.target!.files![0]);
    },
    async submit(e: HTMLFormEvent) {
      e.preventDefault();
      const [title, access_token, json] = e.target;
      const jv = JSON.parse(json.value);
      console.log(title.value, json.value);
      const resp = await fetch(`http://localhost:5000/bot`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          title: title.value,
          intents: jv,
          access_token: access_token.value,
        }),
      });
      const res = await resp.json();
      if (res.ERROR) {
        this.flash = res;
      } else {
        this.flash = {
          ERROR: false,
          MESSAGE: `Your bot is now on the cloud! Access it using uuid: ${res.ID}. Administrate using the bot name and access token you just entered.`,
        };
      }
    },
    input_change() {
      this.label = "-mt-16";
    },
    input_back(e: { target: HTMLInputElement }) {
      if (e.target.value === "") {
        this.label = "-mt-9";
      } else {
        this.label = "-mt-16";
      }
    },
    pass_change() {
      this.passlabel = "-mt-16";
    },
    pass_out(e: { target: HTMLInputElement }) {
      if (e.target.value === "") {
        this.passlabel = "-mt-9";
      } else {
        this.passlabel = "-mt-16";
      }
    },
  },
});
</script>
<style scoped>
input,
label {
  transition-duration: 2s;
}
input:focus {
  border: 2px solid purple;
  outline: none;
}
</style>
