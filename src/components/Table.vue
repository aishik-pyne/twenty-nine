<template>
  <div class="container" >
    <div class="row center-xs center-sm center-md center-lg">
      <div v-for="_card in this.players[0].hand" :key="_card.name" class="col">
         <Card  :rank=_card.rank :suit=_card.suit orientation="down"/>
      </div>
    </div>
    <div class="row">

      <div class="col-2 h-50">
        <Card v-for="_card in this.players[1].hand" :key="_card.name" :rank=_card.rank :suit=_card.suit orientation="left"/>
      </div>
      <div class="col-8"></div>
      <div class="col-2">
        <Card v-for="_card in this.players[2].hand" :key="_card.name" :rank=_card.rank :suit=_card.suit orientation="right" />
      </div>
    </div>
    <div class="row">
      <Card v-for="_card in this.players[3].hand" 
        :key="_card.name" 
        :rank=_card.rank 
        :suit=_card.suit 
        orientation="up" 
        face-up
        />
    </div>
  </div>
</template>

<script>
import Player from "../core/Player";
import Card from "./Card";
export default {
  props: {
    players: {
      type: Array,
      validator: array => {
        array.forEach(element => {
          if (!(element instanceof Player)) return false;
        });
        return true;
      }
    }
  },
  components: {
    Card
  },
  methods: {
    handleCardClick: (player, card) => {
      alert(player, card);
    }
  }
};
</script>

<style lang="less" >

</style>



