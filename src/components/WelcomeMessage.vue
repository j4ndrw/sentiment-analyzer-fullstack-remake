<template>
  <div class="welcome-message">
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
export default {
  props: {
    message: String,
  },
};
</script>

<style>
.welcome-message {
  margin: 2em 2em;
  
  text-align: center;
  font-size: 1.5em;
  padding: 0px 5px;
  user-select: none;
  text-shadow: 2px 1px 3px black;
  transition: 0.4s;
}

.welcome-message:hover {
  text-shadow: 0px 4px 5px black;
  color: rgba(255, 255, 255, 0.75);
}
</style>