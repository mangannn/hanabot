
from player import Player

from itertools import pairwise


COLORS = ['R', 'G', 'B', 'W', 'Y']
VALUES = [1, 2, 3, 4, 5]
NUM_OF_EACH_VALUE_DICT = {1:3, 2:2, 3:2, 4:2, 5:1}
NUM_OF_EACH_COLOR = sum(NUM_OF_EACH_VALUE_DICT.values())

HAND_SIZE = 4




class UnseenCards:

    def __init__(self):

        self.num_of_card_type = { color : dict(NUM_OF_EACH_VALUE_DICT) for color in COLORS }

        self.num = len(COLORS) * NUM_OF_EACH_COLOR



    def saw_new_card(self, card):
        self.num_of_card_type[card[0]][card[1]] -= 1
        self.num -= 1

    def number_left_of_card_type(self, color, value):
        return self.num_of_card_type[color][value]

    def number_left_of_card_type(self, card):
        return self.number_left_of_card_type(card[0], card[1])

    def values_left_in_color(self, color):
        ret = []
        for value in range(1, 5 + 1):
            if self.num_of_card_type[color][value] > 0:
                ret.append(value)
        return ret

    def colors_left_in_value(self, value):
        ret = []
        for color in COLORS:
            if self.num_of_card_type[color][value] > 0:
                ret.append(color)
        return ret


    def reduce_type_combo(self, possible_colors, possible_values):

        new_possible_colors = set()
        new_possible_values = set()

        for color in possible_colors:
            for value in possible_values:
                if self.number_left_of_card_type(color, value) > 0:
                    new_possible_colors.add(color)
                    break

        for value in possible_values:
            for color in possible_colors:
                if self.number_left_of_card_type(color, value) > 0:
                    new_possible_values.add(value)
                    break

        return [new_possible_colors, new_possible_values]


def is_card_playable(board, color, value):
    return self.board[color] == value - 1


def prob_card_is_playable(card_id, board, unseen_cards, possible_colors, possible_values):

    num_possible_cards = 0
    num_possible_playable_cards = 0

    for color in possible_colors:
        for value in possible_values:
            num_of_type_combo = unseen_cards.number_left_of_card_type(color, value)
            if num_of_type_combo > 0:
                num_possible_cards += num_of_type_combo
                if is_card_playable(board, color, value):
                    num_possible_playable_cards += num_of_type_combo

    return num_possible_playable_cards / num_possible_cards


def is_card_played(board, color, value):
    return self.board[color] >= value

def prob_card_is_already_played(card_id, board, unseen_cards, possible_colors, possible_values):

    num_possible_cards = 0
    num_possible_played_cards = 0

    for color in possible_colors:
        for value in possible_values:
            num_of_type_combo = unseen_cards.number_left_of_card_type(color, value)
            if num_of_type_combo > 0:
                num_possible_cards += num_of_type_combo
                if is_card_played(board, color, value):
                    num_possible_playable_cards += num_of_type_combo

    return num_possible_playable_cards / num_possible_cards


class InformationBuildingPlayer(Player):

    def __init__(self):
        super().__init__()

        # keeps track of unseen cards
        # this consists of cards in the deck and cards on the players hand
        self.unseen_cards = UnseenCards()

        # information about cards on the hand
        self.hand_knowlage = [[set(COLORS), set(VALUES)] for _ in range(HAND_SIZE)]


        # update the first seen cards


    def update_knowlage(self, old_info, new_info):

        
        if # clue given to a opponent

            # no information was given to player

            # do nothing

        else:

            # update info about own hand


            if # player played a card

                card_id = # card that was played

                # remove card_id
                self.hand_knowlage.pop(card_id)
                self.hand_knowlage.append([set(COLORS), set(VALUES)])



            if # saw new card
                self.unseen_cards.saw_new_card(card)
            else if # got clue

                indicated_cards = # cards from clue

                if # color clue

                    indicated_color = #

                    for card_id in range(HAND_SIZE):
                        if card_id in indicated_cards:
                            self.hand_knowlage[card_id][0].clear()
                            self.hand_knowlage[card_id][0].add(indicated_color)
                        else:
                            self.hand_knowlage[card_id][0].discard(indicated_color)

                else if # value clue

                    indicated_value = #

                    for card_id in range(HAND_SIZE):
                        if card_id in indicated_cards:
                            self.hand_knowlage[card_id][1].clear()
                            self.hand_knowlage[card_id][1].add(indicated_value)
                        else:
                            self.hand_knowlage[card_id][1].discard(indicated_value)


            # new information was given, need to update card information

            for card_id in range(HAND_SIZE):
                self.hand_knowlage[card_id] = self.unseen_cards.reduce_type_combo(self.hand_knowlage[card_id][0], self.hand_knowlage[card_id][1])

    
    def get_move(self):

        # last 3 turns, or less if there has been less
        for old_info, new_info in pairwise(self.log[-(num_players + 1):]):
            self.update_knowlage(old_info, new_info)



        calculated_prob_cards_are_playable = [prob_card_is_playable(board, self.unseend_cards, self.hand_knowlage[card_id][0], self.hand_knowlage[card_id][1]) for card_id in range(HAND_SIZE)]
        calculated_prob_cards_are_played = [prob_card_is_already_played(board, self.unseend_cards, self.hand_knowlage[card_id][0], self.hand_knowlage[card_id][1]) for card_id in range(HAND_SIZE)]


        # is there a good card to play
        if max(calculated_prob_cards_are_playable) == 1:

            card_id = calculated_prob_cards_are_playable.index(1)
            
            return # play card card_id


        if table_information.clues > 0:

            # is there a good enough clue to give

            for opponent_id in opponent_hands:
                opponents_playable_cards = [is_card_playable(board, opponent_hands[opponent_id][card_id]) for card_id in range(HAND_SIZE):

                # go over all possible clues
                # select thouse only applying to playable cards
                # prioritise the ones with most cards
                # prioritise thouse including the lowest numbers

                # if there is such return that move
                


        # is there a good card to discard
        if max(calculated_prob_cards_are_played) == 1:

            card_id = calculated_prob_cards_are_played.index(1)
            
            return # discard card card_id


        # is there a good enough card to play
        acceptable_probability = 1 - 0.15 * (table_information.lives - 1)
        if max(calculated_prob_cards_are_playable) > acceptable_probability:

            # select card with highest probability of being playable

            card_id = calculated_prob_cards_are_playable.index(max(calculated_prob_cards_are_playable))

            return # play card with card_id


        # discard card with hightest probability to be already played
        card_id = calculated_prob_cards_are_played.index(max(calculated_prob_cards_are_played))

        return # discard card_id
        