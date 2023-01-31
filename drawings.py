import pygame

def draw_ship(draw_hitbox):
  surf = pygame.Surface((100, 100))
  if draw_hitbox:
    surf.fill((0, 225, 225))
  else:
    surf.fill((0, 0, 0))

  p1 = (0, surf.get_height())
  p2 = (surf.get_width()/2, 0)
  p3 = (surf.get_width(), surf.get_height())
  p4 = (surf.get_width()/2, 0.9*surf.get_height())
  pygame.draw.polygon(surf, (0, 255, 0), [p1, p2, p3, p4], width=5)
  surf.convert()
  return surf

def draw_asteroid(draw_hitbox):
  surf = pygame.Surface((100, 100))
  if draw_hitbox:
    surf.fill((0, 255, 0))
  else:
    surf.fill((0, 0, 0))

  pygame.draw.ellipse(surf, (255, 255, 255), pygame.Rect(0, 0, surf.get_width(), surf.get_height()), 20)

  return surf

def draw_bullet():
  surf = pygame.Surface((100, 100))
  surf.fill((0, 255, 0))

  pygame.draw.rect(surf, (255, 0, 0), pygame.Rect(0, 0, surf.get_width(), surf.get_height()))

  return surf