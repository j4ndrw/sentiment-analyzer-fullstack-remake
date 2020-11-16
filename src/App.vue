<template>
  <div id="app">
    <WelcomeMessage message="Enter a sentence and I'll tell you what feeling it gives me!"/>
    <SentenceQuery/>
    <TheFooter />
  </div>
</template>

<script>

import WelcomeMessage from "./components/WelcomeMessage";
import SentenceQuery from "./components/SentenceQuery";
import TheFooter from "./components/TheFooter";

export default {
  name: "App",
  components: {
    WelcomeMessage,
    SentenceQuery,
    TheFooter,
  },
};
</script>

<style>
* {
  margin: 0 auto;
  padding: 0px;
  box-sizing: border-box;
}

html, body {
  max-width: 100%;
  scroll-behavior: smooth;
}

body {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  transition: 0.5s;
}
* {
  background: linear-gradient(286deg, #8400d1, #0349b9);
  background-size: 500% 500%;
  animation: MovingGradient 40s ease infinite;
}

@keyframes MovingGradient {
  0% {
    background-position: 0% 39%;
  }

  50% {
    background-position: 100% 62%;
  }

  100% {
    background-position: 0% 39%;
  }

}

#app {
  max-width: 100%;
  background-color: black;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  overflow: visible;
  overflow-x: hidden;
}
</style>
