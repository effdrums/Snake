import pygame, sys
from pygame.locals import QUIT
import time



pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('SNAKE')
background_colour = (59,150,80)
yellow = (204,197,92)
(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))
screen.fill(background_colour)

class Snake:
  rect = []
  color = yellow
  direction = 1 #1 reigt 2 left 3 up 4 down
  
  def __init__(self):
    print("init")
    self.rect.append(pygame.Rect(10,10,10,10))

  def move_right(self):
    for i in range(len(self.rect)):
      self.rect[i].move_ip(1,0)

  def move_left(self):
    for y in range(len(self.rect)):
      self.rect[y].move_ip(-1,0)

  def direction(self, dir):
    (self.direction) = dir
    print(dir)

  def update(self):
    if self.direction == 1:
      self.move_right()
    elif self.direction == 2:
      self.move_left()
    

snake = Snake()

while True:

  DISPLAYSURF.fill(background_colour)

  snake.update()
  time.sleep(0.01)
  
  pygame.draw.rect(screen, snake.color, snake.rect[0])
  
  for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
          snake.direction = 1
        if event.key == pygame.K_a:  
          snake.direction = 2
          
          
  pygame.display.update()