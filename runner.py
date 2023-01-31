import pygame
import drawings
import movement
import player
import asteroid
import bullet
import random
import numpy as np
import time

class Runner:
  def __init__(self):
    self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    backgroundColor = (0, 0, 0)
    background = pygame.Surface(self.screen.get_size())
    background.fill(backgroundColor)
    self.background = background.convert()

    self.show_hitboxes = False

    self.player = player.Player(self.screen.get_width()/2, self.screen.get_height()/2, 0.005, 0.01, 0.1, 50, 50, drawings.draw_ship, self.show_hitboxes, movement.mover)
    self.allSprites = pygame.sprite.Group(self.player)

    self.asteroids = pygame.sprite.Group()
    self.bullets = pygame.sprite.Group()
    self.is_invincible = False

    self.clock = pygame.time.Clock()

    self.score = 0
    self.coins = 0
    self.font = pygame.font.Font(None, 30)

  def add_asteroid(self, position=None, size=None):

    side = random.choice(['left', 'right', 'up', 'down'])
    v_x = random.uniform(-0.4, 0.35)
    v_y = random.uniform(-0.4, 0.35)

    if size == None:
      my_size = random.uniform(1, 3)
    else:
      my_size = size

    if position == None:
      if side == 'left':
        x = 0
        y = random.uniform(0, self.screen.get_height())
      elif side == 'right':
        x = self.screen.get_width()
        y = random.uniform(0, self.screen.get_height())
      if side == 'up':
        x = random.uniform(0, self.screen.get_width())
        y = 0
      if side == 'down':
        x = random.uniform(0, self.screen.get_width())
        y = self.screen.get_height()
    else:
      x = position[0]
      y = position[1]



    a = asteroid.Asteroid(x, y, v_x, v_y, 30 * my_size, 30 * my_size, drawings.draw_asteroid, self.show_hitboxes, movement.mover)
    self.asteroids.add(a)
    self.allSprites.add(a)

  def add_bullet(self, angle=None):
    if angle == None:
      rad_angle = 2*np.pi*self.player.angle/360
    else:
      rad_angle = 2*np.pi*angle/360
    v_x = -0.9*np.sin(rad_angle)
    v_y = -0.9*np.cos(rad_angle)

    x = self.player.x + self.player.rect.width/2
    y = self.player.y + self.player.rect.height/2

    b = bullet.Bullet(x, y, v_x, v_y, 10, 10, drawings.draw_bullet())
    self.bullets.add(b)
    self.allSprites.add(b)

  def add_multishot(self):
    num_shots = 5
    num_iterations = 360 / num_shots
    for i in range(round(self.player.angle), round(self.player.angle + num_iterations)):
      self.add_bullet(i)

  def invincibility(self, time_):
    self.is_invincible = True
    time.sleep(time_)
    self.is_invincible = False

  def remove_coins(self, num_coins):
    self.coins -= num_coins

  def update_score(self):
    score_surf = pygame.Surface((600, 20))

    score_surf.fill((0, 0, 0))

    self.screen.blit(score_surf, (400, 0))

    pygame.display.update()


  def run(self):
    running = True

    time_since_asteroid = 0

    while running and not self.is_invincible:
      rate = self.clock.tick(500)
      time_since_asteroid += rate
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            running = False
          if event.key == pygame.K_SPACE:
            self.add_bullet()
          if event.key == pygame.K_e and self.coins >= 3:
            self.add_multishot()
            self.remove_coins(3)
          if event.key == pygame.K_f and self.coins >= 5:
            self.invincibility(5)
            self.remove_coins(5)

      if time_since_asteroid > 1000:
        self.add_asteroid()
        time_since_asteroid = 0

      asteroids = pygame.sprite.groupcollide(self.bullets, self.asteroids, True, False)
      for lis in asteroids.values():
        for asteroid in lis:
          self.score += 50
          self.coins += 2
          self.add_asteroid((asteroid.rect.x, asteroid.rect.y), asteroid.width / 60)
          self.add_asteroid((asteroid.rect.x, asteroid.rect.y), asteroid.width / 60)
          asteroid.kill()
          del asteroid


      if not self.is_invincible:
        if pygame.sprite.spritecollide(self.player, self.asteroids, False):
          print('You lost!')
          print(f'Your Score Is {self.score}')
          running = False

      self.allSprites.update(rate, self.screen.get_rect())
      self.screen.blit(self.background, (0, 0))

      sur = self.font.render('Score: ' + str(self.score), True, (255, 255, 255))
      self.screen.blit(sur, (10, 10))

      sur = self.font.render('Coins: ' + str(self.coins), True, (255, 255, 0))
      self.screen.blit(sur, (10, 35))

      sur = self.font.render('Press E for multishot for 3 coins', True, (255, 255, 0))
      self.screen.blit(sur, (self.screen.get_width() - 320, self.screen.get_height() - 55))

      sur = self.font.render('Press F to pause the game for 5 seconds for 5 coins', True, (255, 255, 0))
      self.screen.blit(sur, (self.screen.get_width() - 505, self.screen.get_height() - 30))



      self.allSprites.draw(self.screen)
      pygame.display.flip()

