

from game_state import *

print("HANABOT START!")	


class TableInformation:
    
	def __init__(self, ds, l, c, b, d):

        self.deck_size = ds # int : number of cards in the draw pile
        self.lives = l 		# int : lives left
        self.clues = c 		# int : clues left
        self.board = b 		# dict(color -> int) : mapping colors to number of cards played in that color
        self.discard = d 	# set(card) : discarded cards


class Game:


	def __init__(self, n):

		self.num_players = n

		self.game_state = GameState(self.num_players)

		self.players = [DumbPlayer(i, self.num_players) for i in range(self.num_players)]

		self.current_player = 0


	# returns the hans of openents to player
	# it is ordered as the player sees them from left to right
	def oppnent_hands_to_player(player_id):

		opponent_hands = []

		for i in range(self.num_players - 1):
			oppnoent_id = (player_id + 1 + i) % self.num_players
			oppnent_hands.append(list(game_state.player_hands[oppnoent_id]))

		return oppnent_hands

	# asks the current player for a move and preforms that move
	# then give relevant infromation to each player
	# returns if game is still running
	def step(self):

		move = players[current_player].get_move()

		if not game_state.is_valid_move(move):
			print("PLAYER TRIED TO PREFORM INVALID MOVE!")
			break

		move_result = game_state.preform_move(move)

		for p in range(num_players):

			ti = TableInformation(len(game_state.deck.size()), game_state.lives, game_state.clues, dict(game_state.board), set(game_state.discard))

			players[p].update_log(ti, oppnent_hands_to_player(p), move, move_result)

		return not move_result.is_game_end()


game = Game(3)

while game.step():
	print("Next move")