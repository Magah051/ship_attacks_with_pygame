import pygame;


pygame.init

x = 1280
y = 720

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption("Ship Attacks")

bg = pygame.image.load('images/bg.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (x,y))

alien = pygame.image.load('images/spaceship.png').convert_alpha()
alien = pygame.transform.scale(alien, (50,50))

playerImg = pygame.image.load('images/space.png').convert_alpha()
playerImg = pygame.transform.scale(playerImg, (50,50))
playerImg = pygame.transform.rotate(playerImg, -90)

pos_alien_x = 500
pos_alien_y = 360

pos_player_x = 200
pos_player_y = 300


rodando = True

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    
    screen.blit(bg,(0,0))

    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width, 0))
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))
    
    x-=1

    screen.blit(alien, (pos_alien_x, pos_alien_y))
    screen.blit(playerImg, (pos_player_x, pos_alien_y))

    pygame.display.update()