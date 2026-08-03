import json
from pathlib import Path


class ScoreManager:
    """ Handles saving and loading high scores. """

    def __init__(self):
        self.score_file = Path("high_scores.json")
        self.high_scores = self.load_high_scores()
    

    def load_high_scores(self):
        """ Loads saved high scores. """

        if self.score_file.exists():
            with open(self.score_file) as f:
                return json.load(f)

        return [0] * 10


    def save_high_scores(self):
        """ Saves high scores. """

        with open(self.score_file, "w") as f:
            json.dump(self.high_scores, f)
    

    def add_score(self, score):
        """ Adds a score to leaderboard. """

        self.high_scores.append(score)
        self.high_scores.sort(reverse=True)
        self.high_scores = self.high_scores[:10]
        self.save_high_scores()