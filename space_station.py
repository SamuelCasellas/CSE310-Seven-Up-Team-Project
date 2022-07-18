from constants import *
import os
import pygame
from bullet import Bullet
from math import sin

class Space_Station():
  """Class to handle the space station object. The cannon will react to the userclass's controls. 
  This class will handle the visuals and the bullet objects.
  """

  
  def __init__(self):
    self.bullets = []
    self.target = {}
    self.mask = self.mask = pygame.mask.from_surface(SPACESTATION)
    self.x = WIDTH/2-(SPACESTATION_SIZE[0]/2) 
    self.y = self._centerY = HEIGHT-(SPACESTATION_SIZE[0]/2)+100


  def create_bullet(self, obj):
    """Creates a bullet object"""
    if len(obj.enemy_word) > 4:
      bullet = Bullet(obj.center[0] + 5, HEIGHT-10)
      self.bullets.append(bullet)
      self.target[bullet] = obj
    else:
      bullet = Bullet(obj.center[0], HEIGHT-10)
      self.bullets.append(bullet)
      self.target[bullet] = obj

  def draw_bullet(self):
    """Handles drawing more than one bullet on the screen at once"""
    for bullet in self.bullets:
      WIN.blit(bullet.img, (bullet.x, bullet.y))
            

  def space_station_collide(self, obj):
    """Checks if pixels overlap so objects look like they collide"""
    split = self.x / 6
    offset_left = 0 + split + split
    offset_right = WIDTH - split - split
    offset_height = (len(obj.enemy_word) - 3) * 5

    if obj.center[0] < 300:
      difference = 300 - obj.center[0]
      limit = difference * 1.176470 - 10
      if obj.y + offset_height > HEIGHT - limit:
        return True
    
    if obj.center[0] < 900 and obj.center[0] > 600:
      difference = 300 - obj.center[0] 
      limit = difference / 1.176470 - 10
      if obj.y + offset_height> HEIGHT - limit:
        return True

    if obj.x >= offset_left and obj.x <= offset_right and obj.y + offset_height > HEIGHT / 2 - 70:
      return True

  def check_bullet_hit(self, obj):
    """Checks to see if any bullet has hit an asteroid, if so then the bullet is removed"""
    for bullet in self.bullets:
      if bullet.y <= 0:
        self.bullets.remove(bullet)
      if bullet.y <= obj.y + 100 :
        self.bullets.remove(bullet)
        return True

  def handle_bullets(self):
    """Handles the bullet movement and velocity"""
    for bullet in self.bullets:
      bullet.y -= bullet.vel

  def animation(self, timer):
    self.y = (10 * sin(timer * 0.05)) // 2 + self._centerY
    WIN.blit(SPACESTATION, (self.x, self.y))

    







  
  

