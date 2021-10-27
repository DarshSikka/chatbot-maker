<template>
  <div class="text-blue-900 bg-blue-200 w-max text-center rounded-2xl pb-8">
    <img :src="image" class="rounded-t-2xl" />
    <h1 class="text-2xl mt-4">{{ title }}</h1>
    <h2 class="w-40 text-sm mx-auto">{{ description }}</h2>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "Card",
  props: ["image", "title", "description"],
});
</script>
