import Card from './Card'
import Deck from './Deck'
import Team from './Team'
import { PLAYABLE_CARDS, POINTS, SUITS } from './Utils'
class Game {
  /**
   * Players are indexed [0,1,2,3] in order of [bottom, right, top, left]
   */
  constructor() {
    this.teams = [new Team(), new Team()]
    this.turnStart = 0 // Player index to start the turn


    // Start a new game
    this.newGame()
  }
  reset() {

  }
  newGame() {
    this.deck = new Deck(PLAYABLE_CARDS)
    this.turnStart += 1
    this.trumpSet = false
    this.trumpRevealed = false

  }
  setTrump(suit) {
    if (SUITS.includes(suit)) {
      this.trump = suit
      this.trumpSet = true
    } else {
      throw TypeError('Not a valid suit')
    }
  }
  revealTrump() {
    this.trumpRevealed = true

  }
}

export default Game;