import pygame
import sys

height = 720
width = 1280
displaysurf = pygame.display.set_mode((width, height))
pygame.display.set_caption("TheKing")

player_surf = pygame.transform.scale(pygame.image.load('flappy bird.png').convert_alpha(), (80, 80))
player_rect = player_surf.get_rect()
player_rect.center = (width // 2, height // 2)  # Set the initial position of the player

bgImage = pygame.image.load('fpbg.jpg').convert()
bg_width = bgImage.get_width()
bg_x1 = 0
bg_x2 = bg_width
scroll_speed = 3


motion = 8
gravity = 80

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    bg_x1 -= scroll_speed
    bg_x2 -= scroll_speed
    
    if bg_x1 < -bg_width:
        bg_x1 = bg_width
    
    if bg_x2 < -bg_width:
        bg_x2 = bg_width

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
        player_rect.y -= motion  # Move the player up

    player_rect.y += gravity * clock.tick(60) / 1000  # Apply gravity to the player's position

    displaysurf.blit(bgImage, (bg_x1, 0))
    displaysurf.blit(bgImage, (bg_x2, 0))
    displaysurf.blit(player_surf, player_rect)

    pygame.display.update()
