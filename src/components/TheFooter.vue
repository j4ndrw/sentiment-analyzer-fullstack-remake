<template>
  <div>
    <h1 class="footer-text">
      Made by Andrei-Alin Murjan
    </h1>
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

.footer-text {
  display: flex;
  justify-content: center;
  align-items: center;



  text-align: center;

  margin-top: 2.5em;
  
  min-height: 10vh;

  appearance: none;
  border: none;
  outline: none;
  background: none;

  width: 35%;
  box-shadow: 0px 0px 16px rgba(0, 0, 0, 0.25);
  border-radius: 16px 16px 16px 16px;
  background-color: rgba(0, 0, 0, 0.30);
}
</style>