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
      # draws the bullet
      WIN.blit(self.img, (self.x, self.y))

    def move(self, vel):
      # moves bullet towards asteroid
      self.y += vel

    def off_screen(self, height):
      # checks if the bullet is off screen
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return self.collide(obj)

    def collide(self, obj):
      pass
        # # Checks if pixels overlap so objects look like they collide
        # offset_x = self.x - obj.x
        # offset_y = self.y - obj.y
        # return obj.mask.overlap(self.mask, (offset_x, offset_y)) != None
  

