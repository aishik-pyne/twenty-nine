<template>
  <div id="app" class="h-100">
    <div class="container-fluid h-100">
      <!-- <div class="row">
        <div class="col-md-1 col-lg-2" v-for="_card in this.deck.cards" :key="_card">
          <Card  :rank=_card.rank :suit=_card.suit />
        </div>
      </div> -->
      <Table :players="players"></Table>
    </div>
  </div>
</template>

<script>
import Table from './components/Table'
import Deck from './core/Deck'
import Player from './core/Player'
// import 'flexboxgrid'
import 'bootstrap/dist/css/bootstrap.css'
export default {
  name: 'app',
  components: {
    Table
  },
  created() {
    this.deck = new Deck(["jack", "9", "ace", "10", "king", "queen", "8", "7"])
    this.deck.shuffle()
    this.players = []
    this.players.push(new Player(this.deck.deal(8)))
    this.players.push(new Player(this.deck.deal(8)))
    this.players.push(new Player(this.deck.deal(8)))
    this.players.push(new Player(this.deck.deal(8)))
  },
  data() {
    return {
      suits: ["clubs", "diamonds", "spades", "hearts"]
    }
  }
}
</script>

<style>

</style>
