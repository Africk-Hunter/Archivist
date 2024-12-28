<template>
  <div class="siteTopBar">
    <p class="siteName">Archivist</p>
    <button @click='showHelp' class="siteInfo"><img src="/images/websiteHelp.svg" alt="Help"
        class="siteInfoImg"></button>
  </div>
</template>

<script>
export default {
  name: 'SiteTopBar',
  methods: {
    showHelp() {
      /* Display help box */
    }
  }
};
</script>

<style scoped>
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

@media (min-width: 768px) {
  .siteName {
    font-size: 2rem;
  }

  .siteInfoImg {
    height: 3rem;
    width: auto;
  }
}
</style>