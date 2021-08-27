import Card
import Player



myDeck = Card.Deck()
myDeck.shuffle()
# deck.show()



bob = Player.Player("Bob")
bob.sayHello()
bob.draw(myDeck, 2)
bob.showHand()
player_total = 0
for card in bob.hand:
    player_total = player_total + card.value
    

house = Player.Player("house")
house.draw(myDeck, 2)
house_total = 0
for card in house.hand:
    house_total = house_total + card.value

print(f"Bobs total is {player_total}")
print(f"House total is {house_total}")
