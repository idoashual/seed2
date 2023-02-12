<template>
   <div id="app" class="mt-4" style="background-color: rgb(53, 53, 53);" data-app>
    <div class="home">
    <img width="200" height="50" alt="Vue logo" src="./assets/logo.png" class="mb-5">
     <HelloWorld msg="Welcome to Your Vue.js App" />
    </div>
   </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
img {
    display: block;
    margin-left: auto;
    margin-right: auto;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;

  
}

</style>