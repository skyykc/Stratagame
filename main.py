import pygame

pygame.init()

### Display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('HELLDIVERS 2: STRATAGAME')

clock = pygame.time.Clock()

font = pygame.font.Font('font\helldiversfont.otf', 36)

### Game states
STATE_MENU = 'menu'
current_state = STATE_MENU

### Surfaces

# Menu State
title_surf = font.render('HELLDIVERS 2: STRATAGAME', True, 'White')
title_rect = title_surf.get_rect(center=(400, 100))

# Play button
playtext_surf = font.render('START GAME', True, 'White')
playtext_rect = playtext_surf.get_rect(center=(400, 300))

playbutton_color = 0x6e6e6e
playbutton_surf = pygame.Surface((400, 80))
playbutton_surf.fill(playbutton_color)
playbutton_rect = playbutton_surf.get_rect(center=(400, 300))

# Quit button
quittext_surf = font.render('QUIT', True, 'White')
quittext_rect = quittext_surf.get_rect(center=(400, 400))

quittext_color = 0x6e6e6e
quitbutton_surf = pygame.Surface((200, 80))
quitbutton_surf.fill(quittext_color)
quitbutton_rect = quitbutton_surf.get_rect(center=(400, 400))

### Main loop

running = True
while running:
    dt = clock.tick(24) / 1000  # Delta time in seconds.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')

    if current_state == STATE_MENU:
        screen.blit(title_surf, title_rect)
        screen.blit(playbutton_surf, playbutton_rect)
        screen.blit(playtext_surf, playtext_rect)
        screen.blit(quitbutton_surf, quitbutton_rect)
        screen.blit(quittext_surf, quittext_rect)

        # Play button hover and click effects
        if event.type == pygame.MOUSEMOTION:
            if playbutton_rect.collidepoint(event.pos):
                playbutton_color = 0x595959
                playbutton_surf.fill(playbutton_color)
            else:
                playbutton_color = 0x6e6e6e
                playbutton_surf.fill(playbutton_color)
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if playbutton_rect.collidepoint(mouse_pos):
                playbutton_color = 'DarkGrey'
                playbutton_surf.fill(playbutton_color)

        # Quit button hover and click effects
        if event.type == pygame.MOUSEMOTION:
            if quitbutton_rect.collidepoint(event.pos):
                quittext_color = 0x595959
                quitbutton_surf.fill(quittext_color)
            else:
                quittext_color = 0x6e6e6e
                quitbutton_surf.fill(quittext_color)
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if quitbutton_rect.collidepoint(mouse_pos):
                running = False

    pygame.display.flip()

pygame.quit()