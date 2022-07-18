import random
from constants import *

class Asteroid():

    EXPLOSION = [pygame.image.load(f"Assets/Pictures/explosion/expl_01_000{n}.png") if 10 > n else \
        pygame.image.load(f"Assets/Pictures/explosion/expl_01_00{n}.png") for n in range(24)]

    def __init__(self, enemy_word, x, y, num, answer):
        self.num = num
        self.used_image = asteroid_images[num]
        self.enemy_word = enemy_word
        self.answer = answer
        self.size = (200, 200)
        self.rotation = 0
        self.x = x
        self.y = y
        self.center = (self.x, self.y)
        self.mask = pygame.mask.from_surface(self.used_image)
        self.destroyed = False
        self.destroyed_image = 0
        self.disappear = False

    def size_by_word(self):
        """Increases the size of the asteroid based on the length of the word"""
        length = len(self.enemy_word)
        size = length * 20 + 150
        self.size = (size, size - length * 9)

    def handle_movement(self):
        """Moves the asteroids based on the set velocity.
            Updates the center of the asteroid and calculates offset of the center based on the different 
            asteroid images"""
        self.y += ASTEROID_VEL
        if self.num == 0:
            offset_x = len(self.enemy_word) * 10
            self.center = (self.size[0]/2+self.x - offset_x, self.size[1]/2+self.y - 30)

        if self.num == 1:
            offset_x = len(self.enemy_word) * 10
            self.center = (self.size[0]/2+self.x - offset_x, self.size[1]/2+self.y - 20)

        if self.num == 2:
            offset_x = len(self.enemy_word) * 10
            self.center = (self.size[0]/2+self.x - offset_x, self.size[1]/2+self.y - 20)

    
    def draw_asteroid(self):
        """Draws the asteroid on the screen and draws the text on top of the asteroid"""
        if not self.destroyed:
            rock_img = pygame.transform.scale(self.used_image, self.size)
            # img_copy = pygame.transform.rotate(rock_img, self.rotation)
            # WIN.blit(img_copy, (self.x - int(img_copy.get_width() / 2), self.y - int(img_copy.get_height()/2)))
            WIN.blit(rock_img, (self.x, self.y))          
            word_text = ROCK_FONT.render(self.enemy_word, 1, WHITE)
            WIN.blit(word_text, self.center)
        else:
            get_img = Asteroid.EXPLOSION[self.destroyed_image]
            rock_img = pygame.transform.scale(get_img, self.size)
            WIN.blit(rock_img, (self.x, self.y))          
            self.destroyed_image += 1
            if self.destroyed_image >= len(Asteroid.EXPLOSION):
                self.disappear = True
