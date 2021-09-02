<template>
  <div id="app">
    <Sociodemografico />
  </div>
</template>

<script>
import Sociodemografico from "./components/Sociodemografico.vue";

export default {
  name: "App",
  components: {
    Sociodemografico,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  margin-top: 60px;
  margin-left: 50px;
}
</style>
