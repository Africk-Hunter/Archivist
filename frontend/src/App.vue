<template>
  <div id="app">
    <SiteTopBar />
    <div class="mainContentContainer">
      <WordBox :word="word" :wordType="wordType" :fetchWord :nextWord :previousWord :wordIndex />
      <TimerBar :nextWord/>
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
          this.addWordToLocalStorage();
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
    },

    addWordToLocalStorage() {
      const word = {
        word: this.word,
        wordType: this.wordType,
        pronunciation: this.pronunciation,
        definition: this.definition
      };

      let words = JSON.parse(localStorage.getItem('words')) || [];
      localStorage.setItem('words', JSON.stringify([...words, word]));
      words.push(word);
      localStorage.setItem('words', JSON.stringify(words));
    },

    fetchWordFromLocalStorage(index) {
      const words = JSON.parse(localStorage.getItem('words')) || [];
      if (index >= 0 && index < words.length) {
        this.populateWord(words[index]);
      }
    },

    previousWord() {
      if (this.wordIndex === 0) {
        return;
      }
      this.wordIndex--;
      this.togglePreviousButton();
      this.fetchWordFromLocalStorage(this.wordIndex);
    },

    nextWord() {
      if (this.wordIndex < JSON.parse(localStorage.getItem('words')).length - 1) {
        this.wordIndex++;
        this.fetchWordFromLocalStorage(this.wordIndex);
      } else {
        this.fetchWord();
        this.wordIndex++;
      }
      this.togglePreviousButton();
    },

    updateWordIndex() {
      this.wordIndex = newWordIndex;
    },

    togglePreviousButton() {
      if (this.wordIndex === 0) {
        document.getElementById('previous').classList.add('disabled');
      } else {
        document.getElementById('previous').classList.remove('disabled');
      }
    },
  },

  beforeMount() {
    this.fetchWord();
    localStorage.clear();
  },

  mounted() {
    this.togglePreviousButton();
  },

  data() {
    return {
      word: "",
      wordType: "",
      pronunciation: "",
      definition: "",
      wordIndex: 0
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