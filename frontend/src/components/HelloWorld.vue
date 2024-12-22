<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>Welcome to your Vue.js app!</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      msg: 'Hello World!'
    }
  }
}
</script>

<style scoped>
.hello {
  text-align: center;
  margin-top: 60px;
}
</style>