<template>
  <div id="app">
    <div class="siteTopBar">
      <p class="siteName">WordMe!</p>
      <button class="siteInfo"><img src="/images/websiteHelp.svg" alt="Help" class="siteInfoImg"></button>
    </div>
    <div class="mainContentContainer">
      <section class="wordBox">
        <div class="wordInfo">
          <h1 class="word">{{ word }}</h1>
          <h2 class="wordType">{{ wordType }}</h2>
        </div>
        <section class="buttons">
          <button class="previousWord"><img src="/images/previousButton.svg" alt="Previous Word"
              class="navigationButton"></button>
          <button class="nextWord"><img src="/images/nextButton.svg" alt="Next Word" class="navigationButton"></button>
        </section>
      </section>
      <section class="timerBar">
        <button class="timerButton" id="timerToggle"><img src="/images/timerToggle.svg" alt="Timer Options" class="timerImg"></button>
        <button v-for="(time, index) in timerButtons" :key="index" class="timerButton">
          <img :src="time.src" :alt="time.alt" :class="time.class">
        </button>
      </section>

      <section class="desctiptionContainer">
        <p class="pronuncation">{{ pronunciation }}</p>
        <p class="definition">{{ definition }}</p>
      </section>
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      timerButtons: [
        { src: '/images/timer1.svg', alt: "1 Second", class: "timerImg" },
        { src: '/images/timer2.svg', alt: "2 Seconds", class: "timerImg" },
        { src: '/images/timer3.svg', alt: "3 Seconds", class: "timerImg" },
        { src: '/images/timer4.svg', alt: "4 Seconds", class: "timerImg" },
        { src: '/images/timer5.svg', alt: "5 Seconds", class: "timerImg" },
        { src: '/images/timerCustom.svg', alt: "Custom Timer", class: "timerImg" }
      ],
      word: "Archivist",
      wordType: "Noun",
      pronunciation: "ar·​chi·​vist",
      definition: ": a person who has the job of collecting and storing the materials in an archive",
    };
  }
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

:root {
  --largeDesktop: 1920px;
  --desktop: 1440px;
  --tablet: 768px;
}

html,
body {
  margin: 0;
  padding: 0;
  background: #EBE8E2;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}

button {
  all: unset;
  cursor: pointer;
}

#app {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: .5rem 1rem;
  font-family: 'Montserrat', sans-serif;
}

.siteTopBar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}

@media (min-width: 768px) {
  #app {
    width: 97.5%;
  }
}

.siteName {
  font-size: 1.5rem;
  font-weight: 600;
  margin: 0;
  font-style: italic;
}

.siteInfo {
  display: flex;
  height: 100%;
  width: auto;
  align-items: center;
}

.siteInfoImg {
  height: 2.5rem;
  width: auto;
}

@media (min-width: 768px) {
  .siteName {
    font-size: 2rem;
  }

  .siteInfoImg {
    height: 3rem;
    width: auto;
  }
}

.mainContentContainer {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  margin: 8rem 0 0 0;
  width: 22rem;
}

.wordBox {
  display: flex;
  flex-direction: column;
  align-items: center;
  border-radius: 25px;
  padding: 2rem 1rem 1rem 1rem;
  border: 1px solid #000;
  width: 20rem;
}

.word {
  margin: 0;
  font-size: 3rem;
  font-weight: 500;
  font-family: 'Montserrat', sans-serif;
}

.wordType {
  margin: 0;
  font-size: 2rem;
  font-weight: 400;
  font-style: italic;
  font-size: 1.5rem;
}

.buttons {
  display: flex;
  justify-content: flex-end;
  width: 100%;
  gap: .3rem
}

.previousWord,
.nextWord {
  display: flex;
  align-items: center;
  height: 2.1rem;
  width: auto;
}

.navigationButton {
  height: 2rem;
  width: auto;
}

@media (min-width: 768px) {
  .mainContentContainer {
    width: 42rem;
    gap: 2rem;
    margin: 5rem 0 0 0;
  }

  .wordBox {
    width: 40rem;
    gap: .75rem;
  }

  .word {
    font-size: 5rem;
  }

  .wordType {
    font-size: 2.5rem;
  }
}

.timerBar {
  display: flex;
  width: 100%;
  gap: 1.75rem;
}

.timerButton {
  display: flex;
  width: 1rem;
  height: auto;
}

.timerImg {
  width: 2.5rem;
  height: auto;
}

@media (min-width: 768px) {}

.desctiptionContainer {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 1rem;
  margin-top: 1rem;
}

p {
  margin: 0;
}

.pronuncation {
  font-size: 1.5rem;
  font-weight: 400;
}

.definition {
  font-size: 1.6rem;
  font-weight: 400;
}

@media (min-width: 768px) {
  .pronuncation {
    font-size: 2rem;
  }

  .definition {
    font-size: 2.25rem;
  }
}

</style>