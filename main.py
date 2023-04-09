

#from game_state import *

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

		self.new_player_to_play = 0

		# update player logs with an empty move
		self.update_player_logs(Move(), MoveResult())


	# returns the hans of openents to player
	# it is ordered as the player sees them from left to right
	def oppnent_hands_to_player(self, player_id):

		opponent_hands = []

		for i in range(self.num_players - 1):
			oppnoent_id = (player_id + 1 + i) % self.num_players
			oppnent_hands.append(list(self.game_state.player_hands[oppnoent_id]))

		return oppnent_hands

	def update_player_logs(self, move, move_result):

		for p in range(self.num_players):

			ti = TableInformation(len(self.game_state.deck.size()), self.game_state.lives, self.game_state.clues, dict(self.game_state.board), set(self.game_state.discard))

			players[p].update_log(ti, self.oppnent_hands_to_player(p), move, move_result)

	# asks the current player for a move and preforms that move
	# then give relevant infromation to each player
	# returns if game is still running
	def step(self):

		move = self.players[self.new_player_to_play].get_move()

		if not self.game_state.is_valid_move(move):
			print("PLAYER TRIED TO PREFORM INVALID MOVE!")
			return False

		move_result = self.game_state.preform_move(move)

		self.update_player_logs(move, move_result)

		self.new_player_to_play += 1

		return not move_result.is_game_end()



game = Game(3)

while game.step():
	print("Next move")