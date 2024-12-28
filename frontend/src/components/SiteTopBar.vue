<template>
  <div class="siteTopBar">
    <p class="siteName">Archivist</p>
    <button @click='showHelp' class="siteInfo"><img src="/images/websiteHelp.svg" alt="Help"
        class="siteInfoImg"></button>
  </div>
  <div class="siteInfoBox">
    <p class="infoMessage">Archivist is a web application built to explore new words and their definitions</p>
    <p class="infoMessage">Click <span><img src="/images/nextButton.svg" alt="" class="infoImg"></span> to go to the
      next word and <span><img src="/images/previousButton.svg" alt="" class="infoImg"></span> to go to the previous
      word.</p>
    <p class="infoMessage">Click <span><img src="/images/timerToggle.svg" alt="" class="infoImg"></span> to get access
      to timer options. Clicking one of the number options will display a word every X amount of seconds.</p>
  </div>
</template>

<script>
export default {
  name: 'SiteTopBar',
  methods: {
    showHelp() {
      const siteInfoBox = document.querySelector('.siteInfoBox');

      if (siteInfoBox.style.maxHeight === '20rem') {
        siteInfoBox.style.maxHeight = '0rem';
        siteInfoBox.style.backgroundColor = '#EBE8E2';
        siteInfoBox.style.margin = '.5rem 0 5rem 0';
        siteInfoBox.style.transition = 'max-height .5s ease, background-color .5s ease, margin .5s ease-in-out';
        
      } else {
        siteInfoBox.style.maxHeight = '20rem';
        siteInfoBox.style.backgroundColor = '#dfdcd7';
        siteInfoBox.style.margin = '.5rem 0 2rem 0';
        siteInfoBox.style.transition = 'max-height .5s ease, background-color .5s ease, margin .25s ease-in-out';
      }
    }
  }
};
</script>

<style scoped>
p {
  margin: .5rem 0;
}

.siteTopBar {
  display: flex;
  justify-content: space-between;
  align-items: center;
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

.siteInfoBox {
  display: flex;
  flex-direction: column;
  background: #EBE8E2;
  max-height: 0rem;
  width: 100%;
  margin: .5rem 0 5rem 0;
  overflow: hidden;
  border-radius: 10px;
  padding: .5rem;
  transition: max-height .5s ease, background-color .5s ease, margin .5s ease-in-out;
}

.infoImg {
  height: 1rem;
  width: auto;
}

.infoMessage {
  font-size: .8rem;
  font-family: 'Montserrat', sans-serif;
  align-items: center;

}

span {
  vertical-align: middle;
}

@media (min-width: 768px) {
  .siteName {
    font-size: 2rem;
  }

  .siteInfoImg {
    height: 3rem;
    width: auto;
  }

  .siteInfoBox {
    position: absolute;
    right: 2.5%;
    top: 5rem;
    width: 20%;
  }

  .infoImg {
    height: 1.5rem;
    width: auto;
  }

  .infoMessage {
    font-size: 1.2rem;
  }
}
</style>