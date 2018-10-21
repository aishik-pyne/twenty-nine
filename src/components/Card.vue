<template>
  <div class="playingCard">
    <img :src="faceUp ? cardImg : cardBackImg" alt="" :class="orientation" srcset="" width="100%" height="100%" >
  </div>
</template>

<script>
export default {
  props: {
    rank: {
      type: String,
      validator: value => {
        return [
          "ace",
          "2",
          "3",
          "4",
          "5",
          "6",
          "7",
          "8",
          "9",
          "10",
          "jack",
          "queen",
          "king"
        ].includes(value);
      },
      required: true
    },
    suit: {
      type: String,
      validator: value => {
        return ["clubs", "diamonds", "hearts", "spades"].includes(value);
      },
      required: true
    },
    orientation: {
      type: String,
      validator: value => {
        return ["up", "down", "left", "right"].includes(value);
      },
      default: "up"
    },
    faceUp: {
      type: Boolean,
      default: false
    }
  },
  created() {
    if (["jack", "queen", "king"].includes(this.rank)) {
      this.cardImg = require(`../assets/svg-cards/${this.rank}_of_${
        this.suit
      }2.svg`);
    } else {
      this.cardImg = require(`../assets/svg-cards/${this.rank}_of_${
        this.suit
      }.svg`);
    }
    this.cardBackImg = require(`../assets/svg-cards/card_back.svg`);
  },
  data() {
    return {};
  }
};
</script>

<style lang="less">
@transition_time: 0.2s;
.playingCard {
  img {
    max-width: 100px;
    max-height: 200px;
  }
  .left {
    margin-bottom: -100px;
  }
  .right {
    margin-bottom: -100px;
  }
  &:hover {
    .left {
      transform: translate(20px, 0px) rotate(90deg);
    }
    .right {
      transform: translate(-20px, 0px) rotate(-90deg);
    }
    .up {
      transform: translate(0px, -20px) rotate(0deg);
    }
    .down {
      transform: translate(0px, 20px) rotate(180deg);
    }
  }
}
.left {
  transform: rotate(90deg);
  transition: @transition_time;
}
.right {
  transform: rotate(-90deg);
  transition: @transition_time;
}
.up {
  transform: rotate(0deg);
  transition: @transition_time;
}
.down {
  transform: rotate(180deg);
  transition: @transition_time;
}
</style>

