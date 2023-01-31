import pygame
import player

def mover():
  keys_pressed = pygame.key.get_pressed()
  moves = {}
  moves['down'] = keys_pressed[pygame.K_s]
  moves['up'] = keys_pressed[pygame.K_w]
  moves['right'] = keys_pressed[pygame.K_d]
  moves['left'] = keys_pressed[pygame.K_a]

  return moves

def mover_p2():
  keys_pressed = pygame.key.get_pressed()
  moves = {}
  moves['down'] = keys_pressed[pygame.K_LEFT]
  moves['up'] = keys_pressed[pygame.K_UP]
  moves['right'] = keys_pressed[pygame.K_RIGHT]
  moves['left'] = keys_pressed[pygame.K_LEFT]

#pos, width, height, runner, speed, controls
# player2 = player.Player([100, 100], 30, 30, self, 5, [pygame.K_t, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_r, pygame.K_y])
# player3 = player.Player([100, 100], 30, 30, self, 5, [pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_u, pygame.K_o])
# player3 = player.Player([100, 100], 30, 30, self, 5, [pygame.K_8, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_9])