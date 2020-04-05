class Player {
  constructor(cards = []) {
    this.hand = cards
    this.sortHand()
  }
  sortHand() {
    const comparator = (a,b) => {
      if (a.suit === b.suit) {
        const priority = {
          "jack": 0,
          "9": 1,
          "ace": 2,
          "10": 3,
          "king": 4, 
          "queen": 5, 
          "8": 6, 
          "7": 7 
        } 
        return priority[a.rank] > priority[b.rank]
      } else {
        return a.suit > b.suit
      }
    }
    this.hand.sort(comparator)
  }
}

export default Player;