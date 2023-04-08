class Player:
    def __init__(self):
        self.log = []
        self.states = []

    def get_move(self, state):
        print("You should know better than picking up a duck in a dungeon... You have created object of a super-class")
        return
        
    def update_log(self,player_information, move, result):
        self.log.append(move)
        self.states.append(state)
        return



class BotPlayer(Player):
    def __init__(self):
        super().__init__()
    
    def get_move(self,state):
        print("you have entered the subclass BotPlayer, too bad it is not implemented yet")
        return
        

class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
    
    def get_move(self,state):
        print("you have entered the subclass HumanPlayer, too bad it is not implemented yet")
        return
        
    


