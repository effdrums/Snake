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
  next_pos = [20,10]
  
  def __init__(self):
    print("init")
    self.rect.append(pygame.Rect(20,10,10,10))
    self.rect.append(pygame.Rect(9,10,10,10))
    self.rect.append(pygame.Rect(-2,10,10,10))

  def move_right(self):
    #for y in range(len(self.rect)):
      self.rect[0].move_ip(11,0)

  def move_left(self):
    #for y in range(len(self.rect)):
      self.rect[0].move_ip(-11,0)
  
  def move_down(self):
    #for y in range(len(self.rect)):
      self.rect[0].move_ip(0,11)

  def move_up(self):
    #for y in range(len(self.rect)):
      self.rect[0].move_ip(0,-11)

  def direction(self, dir):
    (self.direction) = dir
    print(dir)

  def update(self):
    self.next_pos = [self.rect[0].x,self.rect[0].y]
    print(self.direction)
    if self.direction == 1:
      self.move_right()
    elif self.direction == 2:
      self.move_left()
    elif self.direction == 3: 
      self.move_up()
    elif self.direction == 4: 
      self.move_down()
    

snake = Snake()
snake.direction(1)

while True:

  DISPLAYSURF.fill(background_colour)

  snake.update()
  time.sleep(0.1)

  pygame.draw.rect(screen, (255,0,0), snake.rect[0])
  
  for rects in range(len(snake.rect)-1):
    aux_pos = snake.rect[rects+1].topleft
    snake.rect[rects+1].topleft = snake.next_pos
    pygame.draw.rect(screen, snake.color, snake.rect[rects+1])
    snake.next_pos = aux_pos
  
  for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
          snake.direction = 1
        if event.key == pygame.K_a:  
          snake.direction = 2
        if event.key == pygame.K_s:  
          snake.direction = 4
        if event.key == pygame.K_w:  
          snake.direction = 3
          
  pygame.display.update()