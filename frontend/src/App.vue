<template>
  <div id="app">
    <div class="siteTopBar">
      <p class="siteName">WordMe!</p>
      <button class="siteInfo"><img src="" alt="Help"></button>
    </div>
    <div class="mainContentContainer">
      <section class="wordBox">
        <h1 class="word">{word}</h1>
        <h2 class="wordType">{wordType}</h2>
        <section class="buttons">
          <button class="previousWord"></button>
          <button class="nextWord"></button>
        </section>
      </section>
      <section class="timerBar">
        <button class="timerToggle"><img src="" alt="Timer Options"></button>
        <button 
          v-for="(time, index) in timerButtons" 
          :key="index" 
          class="timerButton">
          <img :src="time.src" :alt="time.alt">
        </button>
      </section>
      <section class="desctiptionContainer">
        <p class="pronuncation">{pronunciation}</p>
        <p class="definition">{definition}</p>
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
  },
  data() {
    return {
      timerButtons: [
        { src: "", alt: "1 Second" },
        { src: "", alt: "2 Seconds" },
        { src: "", alt: "3 Seconds" },
        { src: "", alt: "4 Seconds" },
        { src: "", alt: "5 Seconds" },
        { src: "", alt: "Custom Timer" }
      ]
    };
  }
};
</script>

<style>
  #app {
    display: flex;
    flex-direction: column;
  }
  
</style>