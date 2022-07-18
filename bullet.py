from constants import *


class Bullet():

    def __init__(self, x, y):
        self.size = (30,45)
        self.image = pygame.image.load(os.path.join(ASSET_PATH, "Pictures", "Bullet", "new_bullet.png"))
        self.img = pygame.transform.rotate(pygame.transform.scale(self.image, self.size), 270)
        self.x = x
        self.y = y
        self.vel = 45
        self.mask = self.mask = pygame.mask.from_surface(self.img)
      

    def draw(self):
      """Draws the bullet"""
      WIN.blit(self.img, (self.x, self.y))

    def move(self, vel):
      """Moves bullet towards asteroid"""
      self.y += vel

    def off_screen(self, height):
      """Checks if the bullet is off screen"""
      return not(self.y <= height and self.y >= 0)

