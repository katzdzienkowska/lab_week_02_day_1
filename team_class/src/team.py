class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0 #we have to hard code it, as there was no value in the original list provided

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player_name):
        for player in self.players:
            if player == player_name:
                return True
        return False
    #another way:
    #   if player_to_chack in self.players:
    #     return True
    #   else:
    #     return False

def play_game(self, game_won):
    if game_won == True:
        self.points += self.points + 3
 #another way:
 #  if game_won:
 #      self.points += 3   
    