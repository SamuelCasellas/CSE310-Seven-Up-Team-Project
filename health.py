from constants import *

class Health():
    def __init__(self):
        self.health = ''
        self.difficulty = ''
        self.health_decrease = 0
        self.bar_decrease = 0

    def decrement_health(self):
        """Decreases player health, updates the health bar"""
        self.health -= 1
        self.bar_decrease += self.health_decrease

    def draw_health(self):
        """Displays the player health bar"""
        text = STATS_FONT.render("Health:", 1, WHITE)
        temp_surface = pygame.Surface(text.get_size())
        temp_surface.fill((149, 152, 156))
        temp_surface.blit(text, (0, 0))
        pygame.draw.rect(WIN, RED, (WIDTH/4, HEIGHT-15, WIDTH/2, 10))
        pygame.draw.rect(WIN, GREEN, (WIDTH/4, HEIGHT-15, WIDTH/2 - self.bar_decrease, 10))
        WIN.blit(temp_surface, (WIDTH/9, HEIGHT - 45))

    def determine_start_health(self, difficulty):
        """Decides on the players starting health based on difficulty chosen"""
        if difficulty == "hard":
            self.health = 5
        elif difficulty == "medium":
            self.health = 7
        else:
            self.health = 10

        self.health_decrease = WIDTH / 2 / self.health


    def get_health(self):
        """Returns amount of health player has left"""
        return self.health
