<template>
  <div class="sentence-wrapper">
    <div class="sentence-box">
      <input
        type="text"
        class="sentence-input"
        placeholder="Your sentence goes here (150 chars max)"
        maxlength="150"
        required
        autocomplete="on"
        v-model="sentence"
        @keyup.enter="analyzeSentence"
      />
    </div>
    <p :class="sentence.length <= 0 ? 'no-display' : ''">
      {{ 150 - sentence.length }} chars left
    </p>
    <button @click="analyzeSentence" class="sentence-judge-btn">Judge</button>
    <div class="entered-sentence">
      <form>
        <h1 class="main-text" v-if="sentence !== ''">{{sentence}}</h1>
        <h1 class="main-text" v-else>Your sentence will appear here...</h1>
      </form>
    </div>
    <Status :status="statusData.message" :color="statusData.color"/>
    <p :class="statusData.message === 'Waiting for you to enter your sentence' ? 'no-display' : `polarity-message ${statusData.color}`">
      Polarity: {{ polarity }}
    </p>
  </div>
</template>

<script>
import Status from "./Status";

export default {
  components: {
    Status,
  },

  data() {
    return {
      sentence: "",
      statusData: {
        message: "Waiting for you to enter your sentence",
        color: ""
      },
      polarity: 0,
    };
  },

  methods: {
    evaluatePrediction(prediction) {
      this.polarity = parseFloat(prediction).toFixed(2);
      if(parseFloat(prediction) < 0.45) {
        if(parseFloat(prediction) < 0.30) {
          this.statusData.message = "Why so negative today? Chill out!";
          this.statusData.color = "red";
        } else {
          this.statusData.message = "Hmm... I'm think you said something mean, but I am not too sure.";
          this.statusData.color = "red";
        }
      } else if(parseFloat(prediction) > 0.60) {
          if(parseFloat(prediction) > 0.75) {
            this.statusData.message = "Such a positive sentence! :)";
            this.statusData.color = "green";
          } else {
            this.statusData.message = "I have no idea what's the meaning of what you said, but I'm sure it's something nice :D";
            this.statusData.color = "green";
          }
      } else {
          this.statusData.message = "I don't know how to judge this... I think this is a neutral sentence!";
          this.statusData.color = "grey";
      }
    },
    analyzeSentence() {
      // TODO: send request to backend where model is stored.
      fetch("/predict", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.sentence),
      })
      .then(res => res.json())
      .then(data => this.evaluatePrediction(data));
    },

    clearInput() {
      this.sentence = "";
      this.chars.numChars = 150;
    }
  },
};
</script>

<style>

input {
  transition: 0.3s;
}

.sentence-wrapper {
  text-align: center;
}

.sentence-box,
.sentence-wrapper {
  width: 100%;
}

p.no-display {
  color: rgba(0, 0, 0, 0);
  background-color: rgba(0, 0, 0, 0);
  transition: all 0.3s;
}

p {
  display: block;
  text-align: center;
  width: 30%;

  padding: 1em;

  margin-bottom: 10px;

  transition: all 0.3s;

  color: #ffffff;
  font-size: 1.2em;

  appearance: none;
  border: none;
  outline: none;
  background: none;

  background-color: rgba(255, 255, 255, 0.5);
  border-radius: 0px 0px 16px 16px;
}

.sentence-wrapper,
.sentence-box {
  transition: 0.3s;
}

.sentence-box {
  min-height: 10vh;
}

.sentence-box,
.sentence-input {
  display: block;
  width: 100%;
  padding: 20px;

  color: #313131;
  font-size: 1.2em;

  appearance: none;
  border: none;
  outline: none;
  background: none;

  box-shadow: 0px 0px 16px rgba(0, 0, 0, 0.25);
  background-color: rgba(255, 255, 255, 0.5);
  border-radius: 16px 16px 0px 16px;

  transition: all 0.3s;
}

.sentence-input:focus,
.sentence-box {
  border-radius: 16px 0px 16px 0px;
  width: 90%;
}

.sentence-judge-btn {
  display: block;

  width: 25%;
  min-height: 10vh;

  font-size: 2em;
  color: white;
  text-shadow: 3px 3px 7px rgba(0, 0, 0, 0.75);

  appearance: none;
  border: none;
  outline: none;
  background: none;

  box-shadow: 0px 0px 16px rgba(0, 0, 0, 0.25);
  background-color: rgba(255, 255, 255, 0.5);
  border-radius: 5px 5px 5px 5px;

  transition: 0.2s;
}

.sentence-judge-btn:hover {
  box-shadow: 0px 0px 16px rgba(0, 0, 0, 0.5);
  background-color: rgba(255, 255, 255, 0.65);
  cursor: pointer;
}

.main-text {
  display: block;
  text-align: center;

  width: 100%;
  
  font-size: 3em;
  word-wrap: break-word;
  background: none;
}

.entered-sentence {
  display: flex;
  justify-content: center;
  align-items: center;

  width: 95%;
  height: auto;


  min-height: 15vh;

  margin-top: 30px;
  padding: 15px 15px;

  appearance: none;
  border: none;
  outline: none;

  color: none;

  box-shadow: 0px 0px 16px rgba(255, 255, 255, 0.5);
  background-color: rgba(255, 255, 255, 0.75);
  border-radius: 16px 0px 16px 0px;

  transition: 0.3s;
}

.entered-sentence {
  font-size: 0.5em;
}

.polarity-message {
  width: 60%;

}
</style>