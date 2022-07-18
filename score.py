from constants import *

class Score():
    def __init__(self):
        self.score = 0
        

    def update_score(self, added_score):
        """Adds points to player score"""
        self.score += added_score

    def draw_score(self) -> None:
        """Draws score on the screen"""
        text = STATS_FONT.render(f"Player score: {self.score}", 1, WHITE)
        WIN.blit(text, (30, 0))

    def get_score(self):
        """Returns player score"""
        return self.score