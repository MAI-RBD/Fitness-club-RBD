<script>
import Header from '../components/app/header/Header.vue'
import Main from '../components/app/main/Main.vue'

export default {
  components: {
    Header,
    Main
  }
}

</script>

<template>
  <main>
    <Header />
    <Main />
  </main>
</template>

<style>

* {
  margin: 0;
  padding: 0;
  border: 0;
  box-sizing: border-box;
}

html {
  color: rgb(226, 226, 226);
  font-family: Tahoma, sans-serif;
  height: 100%
}

ul {
  list-style-type: none;
}

body {
  height: 100%
}

main {
  height: 100%
}

#app {
  height: 100%
}
</style>
