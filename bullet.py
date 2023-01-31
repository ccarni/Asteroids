import pygame

class Bullet(pygame.sprite.Sprite):
  def __init__(self, x, y, v_x, v_y, width, height, surf):
    pygame.sprite.Sprite.__init__(self)

    self.image = pygame.transform.smoothscale(surf, (width, height))

    self.rect = self.image.get_rect(center=(width/2, height/2))
    self.rect.x = x
    self.rect.y = y
    self.x = x
    self.y = y

    self.v_x = v_x
    self.v_y = v_y

  def update(self, rate, bounds):
    self.x += self.v_x*rate
    self.y += self.v_y*rate

    self.rect.x = self.x
    self.rect.y = self.y

    if self.x < -self.rect.width/2:
      self.remove(self.groups())
      del self
      return
    if self.x + self.rect.width/2 > bounds.width:
      self.remove(self.groups())
      del self
      return

    if self.y < -self.rect.height/2:
      self.remove(self.groups())
      del self
      return
    if self.y + self.rect.height/2 > bounds.height:
      self.remove(self.groups())
      del self
      return

    