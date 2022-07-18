import pygame
from constants import *
from button import Button


pygame.display.set_caption("Seven-Up Space")

class Display():
  #class to handle game WIN.
  
  def __init__(self):
    pass


  def draw_window(self):
    """Draws the background on game window"""

    #draw background
    WIN.blit(SPACE, (-10,0))
      
  def game_over(self, player_score):
    """Handles the screen when the game ends. 
      Displays the score of the game played"""
    BG = pygame.transform.scale(pygame.image.load(os.path.join(ASSET_PATH, "Pictures", "Backgrounds", "nebula.jpg")), (WIDTH,HEIGHT))
    WIN.blit(BG, (0, 0))
    game_over_text = FONT.render(f"GAME OVER", True, "#b68f40")
    score_text = FONT.render(f"TOTAL SCORE: {player_score}", True, "#b68f40")
    #Drawing elements
    WIN.blit(game_over_text, (WIDTH/2 - (game_over_text.get_width()/2), HEIGHT/9))
    WIN.blit(score_text, (WIDTH/2 - (score_text.get_width()/2), (HEIGHT/4)))
    
  def draw_pause_option(self):
    text = pygame.font.SysFont('Arial', 28).render("Press space to pause", 1, (173, 173, 173))
    WIN.blit(text, (WIDTH- text.get_width() - 5, 5))
