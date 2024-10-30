import pygame

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
WHITE = (255,255,255)
screen.fill(WHITE)
pygame.display.update()
aresnal_image = pygame.image.load("images/arsenal.png")
chealsea_image  = pygame.image.load("images/chealsea.png")
liverpool_image = pygame.image.load("images/liverpool.png")
man_c_image = pygame.image.load("images/man_c.png")
man_u_image = pygame.image.load("images/man_u.png")

screen.blit(aresnal_image,(50,10))
screen.blit(chealsea_image,(150,200))
screen.blit(liverpool_image,(150,300))
pygame.display.update()

while True:
    pass