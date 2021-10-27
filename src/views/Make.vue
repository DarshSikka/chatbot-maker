<template>
  <div>
    <div class="flex justify-around">
      <button
        @click="n()"
        class="bg-green-900 p-4 rounded text-white hover:bg-green-800 w-36"
      >
        New Intent
      </button>
      <button
        @click="download()"
        class="bg-green-900 p-4 rounded text-white hover:bg-green-800 w-36"
      >
        Download
      </button>
      <label
        for="upload"
        class="bg-green-900 p-4 rounded text-white hover:bg-green-800"
        >Edit existing bot</label
      >
    </div>
    <div class="flex flex-row flex-wrap">
      <div
        style="flex-basis: 200px;"
        :key="intent.id"
        v-for="intent in completeList"
      >
        <div
          class="bg-yellow-400 p-4 rounded text-center text-xl"
          @click="openChange(intent)"
        >
          {{ intent.resp }}
        </div>
        <div
          class="bg-red-400 cursor-pointer"
          @click="deletethis(intent.objectId)"
        >
          Delete
        </div>
      </div>
    </div>
    <input type="file" @change="upload" id="upload" class="hidden" />
    <Form
      v-if="open"
      @close="close()"
      @submitted="collect"
      :preload="this.preload"
    />
  </div>
</template>
<script lang="ts">
import Form from "../components/Form.vue";
interface keywordType {
  id: number;
  keyword: string;
}
interface preload {
  maxId: number;
  resp: "";
  priority: "";
  keywords: Array<keywordType>;
  objectId: number;
}
interface collected {
  keywords: Array<keywordType>;
  resp: string;
  priority: number;
  objectId: number;
}
interface keywordType {
  id: number;
  keyword: string;
}
interface targeted {
  target: HTMLInputElement;
}
import { defineComponent } from "vue";
export default defineComponent({
  data() {
    return {
      completeList: new Array<collected>(),
      open: true,
      preload: {
        maxId: 0,
        resp: "",
        priority: "",
        keywords: new Array<keywordType>(),
        objectId: 0,
      },
      file: "",
    };
  },
  components: {
    Form,
  },
  methods: {
    collect(data: collected) {
      console.log(data);
      console.log(this.completeList);
      if (this.completeList[data.objectId]) {
        this.completeList[data.objectId] = data;
      } else {
        this.completeList.push({ ...data });
      }
      this.open = false;
    },
    deletethis(id: number) {
      console.log(id);
      this.completeList = this.completeList.filter((e, i) => i !== id);
      this.completeList = this.completeList.map((e, i) => ({
        ...e,
        objectId: i,
      }));
    },
    openChange(i: preload) {
      if (this.open == true) {
        return alert(
          "Please cancel or submit this before editing a new intent"
        );
      }
      this.preload = i;
      this.open = true;
    },
    n() {
      if (this.open == true) {
        return alert(
          "Please cancel or submit this before editing a new intent"
        );
      }
      this.preload = {
        maxId: 0,
        resp: "",
        priority: "",
        keywords: new Array<keywordType>(),
        objectId: this.completeList.length,
      };
      this.open = true;
    },
    close() {
      this.open = false;
    },

    upload(e: targeted) {
      const rdr: FileReader = new FileReader();
      rdr.onload = (event) => {
        this.completeList = JSON.parse(String(event.target!.result));
      };
      rdr.readAsText(e.target!.files![0]);
    },
    download() {
      const file = new Blob([JSON.stringify(this.completeList)], {
        type: "application/json",
      });
      const f = URL.createObjectURL(file);
      const anchor = document.createElement("a");
      anchor.download = "bot.chatbot";
      anchor.href = f;
      anchor.click();
    },
  },
});
</script>
