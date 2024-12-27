<template>
  <div id="app">
    <SiteTopBar />
    <div class="mainContentContainer">
      <WordBox :word="word" :wordType="wordType" :fetchWord/>
      <TimerBar />
      <DescriptionContainer :pronunciation="pronunciation" :definition="definition" />
    </div>
  </div>
</template>

<script>
import SiteTopBar from './components/SiteTopBar.vue';
import WordBox from './components/WordBox.vue';
import TimerBar from './components/TimerBar.vue';
import DescriptionContainer from './components/DescriptionContainer.vue';
import axios from 'axios';

export default {
  name: 'App',
  components: {
    SiteTopBar,
    WordBox,
    TimerBar,
    DescriptionContainer
  },
  methods: {
    fetchWord() {
      axios.get('http://localhost:5000/fetch-new-word')
        .then(response => {
          this.populateWord(response.data);
        })
        .catch(error => {
          console.error('Error fetching word:', error);
        });
    },
    populateWord(response) {
      this.word = response.word;
      this.wordType = response.wordType;
      this.pronunciation = response.pronunciation;
      this.definition = response.definition;
    }
  },
  beforeMount() {
    this.fetchWord();
  },
  data() {
    return {
      word: "",
      wordType: "",
      pronunciation: "",
      definition: "",
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

.mainContentContainer {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 1rem;
  margin: 8rem 0 0 0;
  width: 22rem;
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
  .mainContentContainer {
    width: 42rem;
    gap: 2rem;
    margin: 5rem 0 0 0;
  }

  .siteName {
    font-size: 2rem;
  }

  .siteInfoImg {
    height: 3rem;
    width: auto;
  }
}
</style>