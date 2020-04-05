import Card from './Card'
import { POINTS } from './Utils'
class Team {
  constructor(points = 0) {
    this.points = points
    this.stack = []
  }
  get points() {
    return this.stack.reduce(
      (accumulator, card) => accumulator + POINTS[card.suit]
    )
  }
  addCards(cards) {
    if (cards.every((card) => card instanceof Card)) {
      this.stack.push(...cards)
    } else {
      throw TypeError('cards must be array of Cards')
    }
  }
  clearStack() {
    this.stack = []
  }
}

export default Team;