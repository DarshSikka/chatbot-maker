<template>
  <div>
    <nav class="flex justify-around">
      <router-link to="/">Home</router-link>
      <router-link to="/make-bot">Make bot</router-link>
      <router-link to="/upload">Upload to cloud</router-link>
      <router-link to="/edit">Administrate Bot Editing</router-link>
      <router-link to="/find">Find bot </router-link>
    </nav>
    <router-view />
  </div>
</template>
<style></style>
