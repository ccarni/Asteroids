import pygame


class Asteroid(pygame.sprite.Sprite):
  def __init__(self, x, y, v_x, v_y, width, height, surf, hitbox, alg):
    pygame.sprite.Sprite.__init__(self)

    self.hitbox = hitbox
    surf_ = surf(self.hitbox)
    self.surf = surf
    self.image = pygame.transform.smoothscale(surf_, (width, height))

    self.rect = self.image.get_rect(center=(width/2, height/2))
    self.rect.x = x
    self.rect.y = y
    self.x = x
    self.y = y

    self.width = width
    self.height = height

    self.v_x = v_x
    self.v_y = v_y

    self.alg = alg

  def update(self, rate, bounds):
    moves = self.alg()

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

    self.rect.x = round(self.x)
    self.rect.y = round(self.y)
