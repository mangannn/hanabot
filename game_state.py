

import random


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



class GameState:
    
	def __init__(self, num_players):

            self.deck = Deck()
            self.deck.shuffle()

            self.lives = 3
            self.clues = 8

            self.player_turn = 0

            self.played_in_colors = { c : 0 for c in colors}
            self.discard = set()

            self.player_hands = [[] for _ in range(num_players)]

            # deal hands

            for p in range(num_players):
                    for _ in range(4):
                            self.player_hands[p].append(self.deck.draw())

        def is_card_playable(card):
            return self.played_in_color[card[0]] == card[1] - 1

        def preform_move(self, move):
            self.play_card(0, 0)

        def play_card(self, player_id, card_position_in_hand):
            card = self.player_hands[player_id].pop(card_position_in_hand)
            
            if self.is_card_playable(card):
                self.played_in_colors[card[0]] += 1
            else:
                self.lives -= 1
                self.dicard.append(card)
                if self.lives <= 0:
                    print("AAAAAHHHH, dead")
                
