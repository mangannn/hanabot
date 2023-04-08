class Move:
    def __init__(self):
        pass


class Clue(Move):
    def __init__(self, clue, card_ID, player_ID):
        super().__init__()
        if (isinstance(clue, int)):
            self.color = None
            self.number = clue
        else:
            self.number = None
            self.color = clue

        self.card_ID = card_ID
        self.player_ID


class Play(Move):
    def __init__(self, card, card_ID, player_ID):
        super().__init__()
        self.card_ID = card_ID
        self.card = card
        self.player_ID = player_ID


class Discord(Move):
    def __init__(self, card, card_ID, player_ID):
        super().__init__()
        self.card_ID = card_ID
        self.card = card
        self.player_ID = player_ID