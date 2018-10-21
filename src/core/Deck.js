import lodash from 'lodash'
import Card from './Card'
class Deck {
  constructor(ranks = null, suits = null) {
    this.ranks = ranks || ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
    this.suits = suits || ["clubs", "diamonds", "hearts", "spades"]
    this.cards = this.suits.flatMap(suit => {
      return this.ranks.map(rank => {
        return new Card(rank, suit)
      })
    })
  }

  shuffle() {
    this.cards = lodash.shuffle(this.cards);
  }

  sort() {
    
  }
  deal(count) {
    if (count <= this.cards.length)
      return this.cards.splice(0, count)
    else 
      throw Error('Deck out of cards')
  }
}
export default Deck;