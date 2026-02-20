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
STATE_GAME = 'game'
current_state = STATE_MENU

### Surfaces

# Menu State
title_surf = font.render('HELLDIVERS 2: STRATAGAME', True, 'White')
title_rect = title_surf.get_rect(center=(400, 100))

# Super Earth logo with color
orig = pygame.image.load('graphics/logo_super_earth.png').convert_alpha()
mask = pygame.mask.from_surface(orig)
colored = mask.to_surface(setcolor=(hex(0x017191e)), unsetcolor=(0,0,0,0))

super_earth_surf = pygame.transform.rotozoom(colored, 0, 0.02)
super_earth_rect = super_earth_surf.get_rect(center=(400, 300))

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

quitbutton_color = 0x6e6e6e
quitbutton_surf = pygame.Surface((200, 80))
quitbutton_surf.fill(quitbutton_color)
quitbutton_rect = quitbutton_surf.get_rect(center=(400, 400))

# Game State
start_time = 0

### Main loop

running = True
while running:
    dt = clock.tick(24) / 1000  # Delta time in seconds.

    # process every event that has occurred this frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if current_state == STATE_MENU:
            # hover effects for both buttons
            if event.type == pygame.MOUSEMOTION:
                if playbutton_rect.collidepoint(event.pos):
                    playbutton_color = 0x595959
                    playbutton_surf.fill(playbutton_color)
                else:
                    playbutton_color = 0x6e6e6e
                    playbutton_surf.fill(playbutton_color)

                if quitbutton_rect.collidepoint(event.pos):
                    quitbutton_color = 0x595959
                    quitbutton_surf.fill(quitbutton_color)
                else:
                    quitbutton_color = 0x6e6e6e
                    quitbutton_surf.fill(quitbutton_color)

            # clicks
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if playbutton_rect.collidepoint(event.pos):
                    playbutton_color = 0x2f2f2f
                    playbutton_surf.fill(playbutton_color)
                    current_state = STATE_GAME
                    start_time = pygame.time.get_ticks()  # Time when the game state starts
                elif quitbutton_rect.collidepoint(event.pos):
                    running = False

        elif current_state == STATE_GAME:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                current_state = STATE_MENU

    # drawing happens after input processing
    screen.fill(hex(0x12141a))

    if current_state == STATE_MENU:
        # Draw menu
        screen.blit(super_earth_surf, super_earth_rect)
        screen.blit(title_surf, title_rect)
        screen.blit(playbutton_surf, playbutton_rect)
        screen.blit(playtext_surf, playtext_rect)
        screen.blit(quitbutton_surf, quitbutton_rect)
        screen.blit(quittext_surf, quittext_rect)
    elif current_state == STATE_GAME:
        # Draw game state
        screen.blit(super_earth_surf, super_earth_rect)
        current_time = (15000 - (pygame.time.get_ticks() - start_time))
        if current_time > 10000:
            score_surf = font.render(f'{current_time // 1000}', True, hex(0xffee00))
            score_rect = score_surf.get_rect(center=(400, 100))
        elif current_time >= 0:
            score_surf = font.render(f'{current_time / 1000:.1f}', True, hex(0xff8d5d))
            score_rect = score_surf.get_rect(center=(400, 100))
        else:
            score_surf = font.render('TIMES UP!', True, hex(0xff8d5d))
            score_rect = score_surf.get_rect(center=(400, 100))
        screen.blit(score_surf, score_rect)

    pygame.display.flip()

pygame.quit()