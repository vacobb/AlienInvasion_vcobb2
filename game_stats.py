class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.high_score = 0
        self.reset_stats()


    def reset_stats(self):
        self.ships_remaining = self.settings.player_lives   # ships_left in tutorial
        self.score = 0
        self.level = 1
    