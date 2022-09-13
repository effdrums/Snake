import pygame, sys
from pygame.locals import QUIT
import time
import random


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
    self.rect.append(pygame.Rect(20,10,10,10))
    #self.rect.append(pygame.Rect(9,10,10,10))
    #self.rect.append(pygame.Rect(-2,10,10,10))

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

  def update(self,rect_apple):
    
    self.next_pos = [self.rect[0].x,self.rect[0].y]
    if self.direction == 1:
      if self.rect[0].colliderect(rect_apple):
        self.rect.append(pygame.Rect(self.rect[0].x-11,self.rect[0].y,10,10))
      
      self.move_right()
      
    elif self.direction == 2:
      if self.rect[0].colliderect(rect_apple):
        self.rect.append(pygame.Rect(self.rect[0].x+11,self.rect[0].y,10,10))
      self.move_left()
    elif self.direction == 3:
      if self.rect[0].colliderect(rect_apple):
          self.rect.append(pygame.Rect(self.rect[0].x,self.rect[0].y+11,10,10))
      self.move_up()
    elif self.direction == 4: 
      if self.rect[0].colliderect(rect_apple):
          self.rect.append(pygame.Rect(self.rect[0].x,self.rect[0].y-11,10,10))
      self.move_down()
    

snake = Snake()
snake.direction(1)

count = 0; 
rand_pos = [random.randint(0,400-10),random.randint(0,300-10)]

while True:

  DISPLAYSURF.fill(background_colour)

  snake.update( pygame.Rect(rand_pos,[10,10]))
  time.sleep(0.1)

  if count < 40: 
    count += 1
  elif count == 40:
    rand_pos = [random.randint(0,400-10),random.randint(0,300-10)]
    count = 0

  


  pygame.draw.rect(screen, (213, 52, 235), pygame.Rect(rand_pos,[10,10]))


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