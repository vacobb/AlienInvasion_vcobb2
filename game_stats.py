""" Alien Invaders - Track 2 (Custom Assets)
Vaughn Cobb
This is a reskin of the classic Alien Invaders arcade game. 
Starter code was taken from Alien Invaders tutorial completed in class
24-July-2026 """

class GameStats:
    """ Handles logic for game stats. """
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.high_score = 0
        self.reset_stats()


    def reset_stats(self):
        """ Resets stats to default on new game. """
        self.ships_remaining = self.settings.player_lives
        self.score = 0
        self.level = 1
    