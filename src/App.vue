<template>
  <div id="app">
    <Sociodemografico />
    <capturador_fotos/>
  </div>
</template>

<script>
import Sociodemografico from "./components/Sociodemografico.vue";
import capturador_fotos from './components/CapturaFotos.vue';

export default {
  name: "App",
  components: {
    Sociodemografico,
    capturador_fotos,
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
