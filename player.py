import pygame
import numpy as np

class Player(pygame.sprite.Sprite):
  def __init__(self, x, y, a, d, rotate_rate, width, height, surf, hitboxes, alg):
    pygame.sprite.Sprite.__init__(self)

    self.hitboxes = hitboxes
    surf_ = surf(hitboxes)
    self.surf = surf
    self.surface = pygame.transform.smoothscale(surf_, (width, height))
    self.image = self.surface

    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.x = x
    self.y = y

    self.v_x = 0
    self.v_y = 0
    self.a = a
    self.d = d

    self.width = width
    self.height = height

    self.rotate_rate = rotate_rate

    self.angle = 0
    self.alg = alg

  def update(self, rate, bounds):
    moves = self.alg()
    if moves['left']:
      self.angle += self.rotate_rate*rate
    if moves['right']:
      self.angle -= self.rotate_rate*rate

    self.angle = self.angle % 360

    self.image = pygame.transform.rotate(self.surface, self.angle)
    self.rect = self.image.get_rect()

    if moves['up'] and not moves['down']:
      rad_angle = 2*np.pi*self.angle/360
      self.v_x -= self.a*np.sin(rad_angle)*rate
      self.v_y -= self.a*np.cos(rad_angle)*rate

      self.v_x = np.clip(self.v_x, -1, 1)
      self.v_y = np.clip(self.v_y, -1, 1)

    if moves['down'] and not moves['up']:
      rad_angle = np.pi*self.angle/180
      self.v_x += self.a*np.sin(rad_angle) * rate
      self.v_y += self.a*np.cos(rad_angle)*rate

      self.v_x = np.clip(self.v_x, -1, 1)
      self.v_y = np.clip(self.v_y, -1, 1)

    # Slows down
    self.v_x -= np.sign(self.v_x)*self.d/2
    self.v_y -= np.sign(self.v_y)*self.d/2

    self.x += self.v_x*rate
    self.y += self.v_y*rate


    if self.x < -self.rect.width/2:
      self.x = bounds.width - self.rect.width/2
    if self.x + self.rect.width/2 > bounds.width:
      self.x = -self.rect.width/2

    if self.y < -self.rect.height/2:
      self.y = bounds.height - self.rect.height/2
    if self.y + self.rect.height/2 > bounds.height:
      self.y = -self.rect.height/2

    self.rect.x = self.x
    self.rect.y = self.y





    

    