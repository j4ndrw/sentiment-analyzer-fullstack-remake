<template>
  <div>
    <h1 class="footer-text">
      Made by Andrei-Alin Murjan
      <div class="images">
        <a href="https://www.github.com/j4ndrw/" target="blank">
          <img src="https://cdn.afterdawn.fi/v3/news/original/github-logo.png" alt="GitHub"/>
        </a>
        <a href="https://www.linkedin.com/in/andrei-alin-murjan-812908197/" target="blank">
          <img src="https://cdn.icon-icons.com/icons2/2201/PNG/512/linkedin_logo_square_icon_134016.png"/>
        </a>
      </div>
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

img {
  display: flex;
  justify-content: space-between;
  align-items: center;
  
  width: 1.6em;
  height: 1.6em;

  border: 1px solid rgba(0, 0, 0, 0.65);

  appearance: none;
  outline: none;
  background: none;

  background-color: rgba(0, 0, 0, 0.45);
}

.footer-text {
  display: flex;
  justify-content: center;
  align-items: center;

  padding: 1em;

  text-align: center;

  margin-top: 0.3em;
  
  min-height: 10vh;

  font-size: 2em;

  appearance: none;
  border: none;
  outline: none;
  background: none;

  width: 100%;
  box-shadow: 0px 0px 16px rgba(0, 0, 0, 0.25);
  border-radius: 16px 16px 16px 16px;
  background-color: rgba(0, 0, 0, 0.30);
}

.images {
  display: inline-flex;
  margin-left: 2em;
}
</style>