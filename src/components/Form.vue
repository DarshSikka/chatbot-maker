<template>
  <div class="border-2 border-blue-900 h-96 rounded mt-16">
    <div class="flex flex-col w-max mx-auto h-56 justify-around">
      <input
        type="text"
        placeholder="Keywords"
        class="w-96 p-2 rounded"
        v-model="keyword"
      />
      <button
        @click="addKeyword"
        class="bg-blue-900 hover:bg-blue-800 text-blue-200 p-2 rounded"
      >
        Add
      </button>
      <input
        class="w-96 p-2 rounded"
        type="text"
        placeholder="Response the bot gives to these keywords"
        v-model="resp"
      />
      <input
        class="w-96 p-2 rounded"
        type="number"
        placeholder="Priority"
        v-model="priority"
      />
      <div class="flex">
        <button
          class="bg-blue-700 hover:bg-blue-600 text-center w-48 mx-auto text-white p-4 rounded"
          @click="move"
        >
          Submit Intent
        </button>
        <button
          @click="$emit('close')"
          class="bg-red-700 hover:bg-red-600 text-center w-48 mx-auto text-white p-4 rounded"
        >
          Close
        </button>
      </div>
    </div>
    <div :key="kw.id" v-for="kw in keywords" class="m-auto w-max">
      <input v-model="keywords[kw.id].keyword" class="p-4 rounded" /><button
        class="bg-red-700 text-white p-4 rounded w-max mx-auto p-4 rounded"
        @click="deleteKeyword(kw.id)"
      >
        Delete
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
interface dom {
  target: {
    value: number;
  };
  preventDefault: Function;
}
interface keywordType {
  id: number;
  keyword: string;
}
interface collection {
  keywords: Array<keywordType>;
  resp: string;
  priority: number;
  objectId: number;
}
export default defineComponent({
  mounted() {
    console.log(this.preload);
  },
  name: "Home",
  data() {
    return {
      keyword: this.preload.keyword,
      keywords: this.preload.keywords,
      priority: this.preload.priority,
      resp: this.preload.resp,
      maxId: this.preload.keywords.length,
      objectId: this.preload.objectId,
    };
  },
  methods: {
    addKeyword(e: dom) {
      e.preventDefault();
      const stuff: keywordType = { id: this.maxId, keyword: this.keyword };
      this.keywords.push(stuff);
      this.keyword = "";
      this.maxId += 1;
    },
    deleteKeyword(id: number) {
      this.keywords = this.keywords.filter((kw: keywordType) => kw.id != id);
      this.keywords = this.keywords.map((kw: keywordType, i: number) => ({
        ...kw,
        id: i,
      }));
      this.maxId -= 1;
    },
    move() {
      const collect: collection = {
        keywords: this.keywords,
        resp: this.resp,
        priority: this.priority,
        objectId: this.objectId,
      };
      this.$emit("submitted", collect);
    },
  },
  props: ["preload"],
});
</script>
<style lang="scss">
form {
  input:focus {
    border: 1px solid rgb(30, 58, 138);
    outline: none;
  }
}
</style>
