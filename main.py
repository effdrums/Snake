import pygame, sys
from pygame.locals import QUIT



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
  
  def __init__(self):
    print("init")
    self.rect.append(pygame.Rect(10,10,10,10))

snake = Snake()

while True:

  pygame.draw.rect(screen, snake.color, snake.rect[0])
  
  for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()
  pygame.display.update()