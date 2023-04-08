import random


print("HANABOT START!")	


num_players = 3

colors = ['R', 'G', 'B', 'W', 'Y']


class Deck:
	
	def __init__(self):
		self.cards = []
		for c in colors:
			self.cards.append( (c, 1) )
			self.cards.append( (c, 1) )
			self.cards.append( (c, 1) )
			self.cards.append( (c, 2) )
			self.cards.append( (c, 2) )
			self.cards.append( (c, 3) )
			self.cards.append( (c, 3) )
			self.cards.append( (c, 4) )
			self.cards.append( (c, 4) )
			self.cards.append( (c, 5) )

	def draw(self):
		return self.cards.pop() 

	def shuffle(self):
		random.shuffle(self.cards)

	def print(self):
		for c in self.cards:
			print(c)

deck = Deck()
deck.shuffle()

print(deck)


player_hands = [[] for _ in range(num_players)]

print(player_hands)



# deal hands

for p in range(num_players):
	for _ in range(4):
		player_hands[p].append(deck.draw())



print(player_hands)

