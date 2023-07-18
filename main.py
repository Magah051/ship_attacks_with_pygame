import pygame;


pygame.init

x = 1280
y = 720

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption("Ship Attacks")

bg = pygame.image.load('images/bg.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (x,y))

rodando = True

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    
    screen.blit(bg,(0,0))
    pygame.display.update()