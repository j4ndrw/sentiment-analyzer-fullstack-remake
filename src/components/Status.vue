<template>
  <h1 
    class="status-text"
    :class="color"
  >
    {{ status }}
  </h1>
</template>

<script>
export default {
  props: {
    status: String,
    color: String
  },
};
</script>

<style>
h1 {
  transition: 0.3s;
}
.status-text {
  display: flex;
  justify-content: center;
  align-items: center;

  width: 75%;
  padding: 15px;

  min-height: 10vh;

  margin-top: 40px;

  color: #f6f6f6;
  font-size: 1.5em;

  appearance: none;
  border: none;
  outline: none;
  background: none;

  box-shadow: 0px 0px 16px rgba(0, 0, 0, 0.25);
  background-color: rgba(255, 255, 255, 0.5);
  border-radius: 16px 0px 16px 16px;

  transition: 0.3s;
}
.red {
  background-color: rgba(255, 0, 0, 0.5);
  transition: 0.3s;
}

.green {
  background-color: rgba(0, 255, 55, 0.5);
  transition: 0.3s;
}

.grey {
  background-color: rgba(128, 128, 128, 0.5);
  transition: 0.3s;
}
</style>