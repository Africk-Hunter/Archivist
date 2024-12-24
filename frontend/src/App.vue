<template>
  <div id="app">
    <div class="siteNameContainer">
      WordMe!
    </div>
    <div class="mainContentContainer">
      <section class="wordBox">
        <h1 class="word">{word}</h1>
        <h2 class="wordType">{wordType}</h2>
        <section class="buttons">
        </section>
      </section>
    </div>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';

export default {
  name: 'App',
  components: {
    HelloWorld
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>