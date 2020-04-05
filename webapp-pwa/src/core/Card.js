class Card {
  constructor(rank, suit) {
    this.rank = rank
    this.suit = suit
    this.name = `${this.rank}of${this.suit}`
  }
}
export default Card;