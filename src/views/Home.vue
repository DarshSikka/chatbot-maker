<template>
  <div>
    <div class="flex justify-around items-center">
      <div class="flex flex-col justify-around h-96">
        <h1 class="text-3xl text-blue-900">Make.Chatbot</h1>
        <p class="w-48 text-2xl">
          Make chatbots for free!
        </p>
        <p class="w-96 text-lg">
          Have advantage with both our API and our premade UI for
          non-developers! Simple algorithms without a need for large amounts of
          data provide you an edge on using us! Both a prebuilt site and a
          development API gives you an easy start
        </p>
      </div>
      <img src="https://picsum.photos/500/500" />
    </div>
    <div class="flex justify-around mt-8">
      <Card
        image="https://i.picsum.photos/id/61/300/200.jpg?hmac=MQZaPWaOGDYXs7I1QrHDauppW2rTzjJUZbh_Pucq4WU"
        title="JSON API based"
        description="Our API's are JSON based,
      enabling easy development actions"
      />
      <Card
        image="https://i.picsum.photos/id/61/300/200.jpg?hmac=MQZaPWaOGDYXs7I1QrHDauppW2rTzjJUZbh_Pucq4WU"
        title="Code Packages"
        description="Various modules for different languages are advantageous for developers. "
      />
      <Card
        image="https://i.picsum.photos/id/61/300/200.jpg?hmac=MQZaPWaOGDYXs7I1QrHDauppW2rTzjJUZbh_Pucq4WU"
        title="Pre-UI"
        description="The Pre-UI enables use for non-developers. Also lessens release time for developers"
      />
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import Card from "@/components/Card.vue";
export default defineComponent({
  name: "Home",
  data() {
    return {};
  },
  components: {
    Card,
  },
});
</script>
