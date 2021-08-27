import Card
import Player

myDeck = Card.Deck()
myDeck.shuffle()
# deck.show()

bob = Player.Player("Bob")
bob.sayHello()
bob.draw(myDeck, 5)
bob.showHand()

