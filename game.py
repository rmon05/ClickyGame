import random
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN

pygame.init()

# Set width and height
WIDTH = 1000
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)

# Create the screen
screen = pygame.display.set_mode(SIZE)
# Cursor
pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
# Caption
pygame.display.set_caption('Value Village Aim Labs')

# Create the clock
clock = pygame.time.Clock()

# Initialize the score
score = 0

# Initialize the fonts
text_font = pygame.font.SysFont('Gotham', 25, True, False)
play_button_font = pygame.font.SysFont('Gotham', 48, True, False)
instructions_font = pygame.font.SysFont('Gotham', 28, True, False)
title_font1 = pygame.font.SysFont('Gotham', 35, True, False)
title_font2 = pygame.font.SysFont('Gotham', 40, True, False)
load_font = pygame.font.SysFont('Gotham', 45, True, False)
game_over_font = pygame.font.SysFont('Gotham', 40, True, False)
# ---------------------------
# Initialize global variables
# crosshair
pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
# Level 1 Target
target_1_location = (200, 200)
target_1_radius = 50
target_1 = pygame.draw.circle(screen, (211, 211, 211), target_1_location,
                              target_1_radius)

# Level 2 target def
target_2_location = (200, 200)
target_2_radius = 40
target_2 = pygame.draw.circle(screen, (255, 0, 0), target_2_location,
                              target_2_radius)

# Level 3 target def
target_3_location = (200, 200)
target_3_radius = 30
target_3 = pygame.draw.circle(screen, (255, 0, 0), target_3_location,
                              target_3_radius)

# level 4 target def
target_4_location = (200, 200)
target_4_radius = 20
target_4 = pygame.draw.circle(screen, (0, 0, 0), target_4_location,
                              target_4_radius)
# secret easter egg of level 4
target_4_sun_location = (500, 75)
target_4_sun_radius = 75
target_4_sun = pygame.draw.circle(screen, (0, 0, 0), target_4_sun_location,
                                  target_4_sun_radius)
# variables for the easter egg
level_4_easter_egg_moon_location = (500, 75)
level_4_easter_egg_moon_radius = 75

# level 5 target def
target_5_location = (200, 200)
target_5_radius = 10
target_5 = pygame.draw.circle(screen, (0, 0, 0), target_5_location,
                              target_5_radius)

# Menu Buttoms
play_button = pygame.Rect(800, 500, 200, 100)  # (RIGHT SIDE)
instructions_button = pygame.Rect(0, 500, 200, 100)

# Game is running if running is True
running = True

# IF ON MENU PAGE
on_menu = True

# IF ON INSTRUCTIONS PAGE
instructions_page = False

while running and on_menu:

    #  EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == MOUSEBUTTONDOWN:
            play_hit = play_button.collidepoint(event.pos)
            instructions_hit = instructions_button.collidepoint(event.pos)
            if play_hit == 1:
                on_menu = False
            elif instructions_hit == 1 and instructions_page == False:
                instructions_page = True
            elif instructions_hit == 1 and instructions_page == True:
                instructions_page = False
        elif event.type == QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    #  DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command
    crosshair_cursor = pygame.SYSTEM_CURSOR_CROSSHAIR
    # changin the cursor_img
    # pygame.mouse.set_visible(False)
    # cursor_img_rect = cursor_img.get_rect()

    # BACKGROUND GRAPHICS

    # Bottom bar
    pygame.draw.rect(screen, YELLOW, [0, 500, 1000, 100], 0)
    # Sky background
    for i in range(10, 255, 1):
        pygame.draw.line(screen, (85, 0, i), [0, i - 10], [1000, i - 10], 5)
    # Setting sun
    pygame.draw.circle(screen, (255, 80, 0), [500, 300], 200)
    # Water background
    pygame.draw.rect(screen, (0, 0, 155), [0, 200, 1000, 100], 0)
    # Grass landscape
    pygame.draw.rect(screen, (0, 155, 0), [0, 300, 1000, 200], 0)
    # Bar holding up target
    pygame.draw.line(screen, (102, 51, 0), (500, 335), (500, 435), 7)
    # Target
    pygame.draw.circle(screen, RED, [500, 335], 30)
    pygame.draw.circle(screen, WHITE, [500, 335], 20)
    pygame.draw.circle(screen, RED, [500, 335], 10)

    if instructions_page:
        # draw the isntructions
        intruction_font = pygame.font.Font(None, 30)
        intruction_text = intruction_font.render(
            "Click on the circles as fast as you can to win!", True, (BLACK))
        screen.blit(intruction_text, [300, 550])

        # back button
        pygame.draw.ellipse(screen, (0, 0, 0), instructions_button, 0)
        back_text = play_button_font.render("BACK", True, (255, 255, 0))
        screen.blit(back_text, [45, 535])

    else:
        # play button
        pygame.draw.ellipse(screen, (0, 0, 0), play_button, 0)
        play_text = play_button_font.render("PLAY", True, (255, 255, 0))
        screen.blit(play_text, [850, 535])

        # Instruction Button
        pygame.draw.ellipse(screen, (0, 0, 0), instructions_button, 0)
        instructions_text = instructions_font.render("INSTRUCTIONS", True,
                                                     (255, 255, 0))
        screen.blit(instructions_text, [18, 540])

        # Title
        menu_page_title = title_font1.render("WELCOME TO THE IMPOSSIBLE,",
                                             True, BLACK)
        menu_page_title2 = title_font2.render("VALUE VILLAGE AIM TRAINER!",
                                              True, BLACK)
        screen.blit(menu_page_title, [250, 525])
        screen.blit(menu_page_title2, [250, 550])

    # DRAW

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(60)
    # ---------------------------

# ---------------------------
# score requirements for access to level is 0
while running and score < 100:
    # Handle and process events
    for event in pygame.event.get():

        if event.type == KEYDOWN:
            # Exit loop if user clicks esc
            if event.key == K_ESCAPE:
                running = False

        elif event.type == MOUSEBUTTONDOWN:
            # Tests if the target was hit
            hit_target = target_1.collidepoint(event.pos)
            if hit_target == 1:
                score += 10

            # Update the target and target location if hit
            target_1_location = (random.randint(100,
                                                950), random.randint(100, 550))
            target_1 = pygame.draw.circle(screen, (211, 211, 211),
                                          target_1_location, target_1_radius)

        elif event.type == QUIT:
            # Exit loop if user cicks exit
            running = False

    #  DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command

    # Background
    for i in range(0, 200, 1):
        pygame.draw.line(screen, (0, 0, i), [0, 3 * i], [1000, 3 * i], 5)
    for i in range(50):
        rand_x = random.randint(0, 1000)
        rand_y = random.randint(0, 600)
        pygame.draw.circle(screen, (255, 255, 255), [rand_x, rand_y], 1)

    # Display new target location
    pygame.draw.circle(screen, (211, 211, 211), target_1_location,
                       target_1_radius)

    # Draw top bar
    pygame.draw.rect(screen, (255, 255, 255), [0, 0, 1000, 50], 0)

    # Update scoreboard
    score_text = text_font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, [5, 5])

    # Display level
    level_text = text_font.render("Level 1", True, (0, 0, 0))
    screen.blit(level_text, [925, 5])

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(60)

# Level up screen from 1-2
# How long the bar has been running for
bar_1_2 = 0
# Emmpty bar
level_1_2_bar = pygame.Rect(299, 299, 402, 52)
# Run
while running and bar_1_2 < 400:
    # Handle and process events
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # Exit loop if user clicks esc
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            # Exit loop if user cicks exit
            running = False

    progress_1_2_bar = pygame.Rect(300, 300, bar_1_2, 50)
    #  DRAWING
    screen.fill((int(bar_1_2/2), int(255-bar_1_2/3), int(bar_1_2/3)))  # always the first drawing command

    # Draw the bar
    pygame.draw.rect(screen, WHITE, level_1_2_bar, 1)
    pygame.draw.rect(screen, RED, progress_1_2_bar, 0)

    # #Loading Text
    load_title = load_font.render('LOADING NEXT LEVEL', True, BLACK)
    screen.blit(load_title, [310, 310])

    # Write levels
    lv_1_text = title_font2.render("1", True, RED)
    lv_2_text = title_font2.render("2", True, RED)
    screen.blit(lv_1_text, [250, 310])
    screen.blit(lv_2_text, [730, 310])

    # Update bar
    bar_1_2 += 1

    pygame.display.flip()
    clock.tick(60)
    
# score requirements for access to level 2 is 100
while running and score < 210:
    #  EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == MOUSEBUTTONDOWN:
            hit_target = target_2.collidepoint(event.pos)
            if hit_target == 1:
                score += 10

            # Update the target and target location
            target_2_location = (random.randint(100,
                                                950), random.randint(100, 550))
            target_2 = pygame.draw.circle(screen, (255, 0, 0),
                                          target_2_location, target_2_radius)

        elif event.type == QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    #  DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command
    # Background
    pygame.draw.rect(screen, (102, 51, 0), [0, 50, 1000, 600], 0)

    # Display new target location
    pygame.draw.circle(screen, (255, 0, 0), target_2_location, target_2_radius)

    # Update scoreboard
    score_text = text_font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, [5, 5])

    # Display level
    level_text = text_font.render("Level 2", True, (0, 0, 0))
    screen.blit(level_text, [925, 5])

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(60)

# Level up screen from 2-3
# How long the bar has been running for
bar_2_3 = 0
# Emmpty bar
level_2_3_bar = pygame.Rect(299, 299, 402, 52)
# Run
while running and bar_2_3 < 400:
    # Handle and process events
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # Exit loop if user clicks esc
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            # Exit loop if user cicks exit
            running = False

    progress_2_3_bar = pygame.Rect(300, 300, bar_2_3, 50)
    #  DRAWING
    screen.fill(BLACK)  # always the first drawing command

    # Draw the bar
    pygame.draw.rect(screen, WHITE, level_2_3_bar, 1)
    pygame.draw.rect(screen, RED, progress_2_3_bar, 0)
    # #Loading Text
    load_title = load_font.render('LOADING NEXT LEVEL', True, BLACK)
    screen.blit(load_title, [310, 310])
    # Write levels
    lv_2_text = title_font2.render("2", True, GREEN)
    lv_3_text = title_font2.render("3", True, GREEN)
    screen.blit(lv_2_text, [250, 310])
    screen.blit(lv_3_text, [730, 310])

    # Update bar
    bar_2_3 += 1

    pygame.display.flip()
    clock.tick(60)

# score requirements for access to level 3 is 210
while running and score < 330:
    #  EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == MOUSEBUTTONDOWN:
            hit_target = target_3.collidepoint(event.pos)
            if hit_target == 1:
                score += 10

            # Update the target and target location
            target_3_location = (random.randint(100,
                                                950), random.randint(100, 550))
            target_3 = pygame.draw.circle(screen, (255, 0, 0),
                                          target_3_location, target_3_radius)

        elif event.type == QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    #  DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command
    # Drawing variables

    # Background
    pygame.draw.rect(screen, (102, 204, 255), [0, 50, 1000, 600], 0)
    # The sun
    pygame.draw.circle(screen, YELLOW, [60, 90], 40, 0)
    # mountain
    pygame.draw.polygon(screen, (86, 89, 87),
                        [[150, 600], [850, 600], [500, 250]], 0)
    # Snowy tip
    pygame.draw.polygon(screen, (WHITE), [[500, 250], [400, 350], [600, 350]],
                        0)
    # Random bits of snow
    for i in range(60):
        rand_x = random.randint(0, 1000)
        rand_y = random.randint(0, 600)
        pygame.draw.circle(screen, (WHITE), [rand_x, rand_y], 3)

    # Display new target location
    pygame.draw.circle(screen, (255, 0, 0), target_3_location, target_3_radius)

    # Update scoreboard
    score_text = text_font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, [5, 5])

    # Display level
    level_text = text_font.render("Level 3", True, (0, 0, 0))
    screen.blit(level_text, [925, 5])

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(60)

# Level up screen from 3-4
# How long the bar has been running for
bar_3_4 = 0
# Emmpty bar
level_3_4_bar = pygame.Rect(299, 299, 402, 52)
# Run
while running and bar_3_4 < 400:
    # Handle and process events
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # Exit loop if user clicks esc
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            # Exit loop if user cicks exit
            running = False

    progress_3_4_bar = pygame.Rect(300, 300, bar_3_4, 50)
    #  DRAWING
    screen.fill(BLACK)  # always the first drawing command

    # Draw the bar
    pygame.draw.rect(screen, WHITE, level_3_4_bar, 1)
    pygame.draw.rect(screen, RED, progress_3_4_bar, 0)

    # Loading Text
    load_title = load_font.render('LOADING NEXT LEVEL', True, BLACK)
    screen.blit(load_title, [310, 310])

    # Write levels
    lv_1_text = title_font2.render("3", True, WHITE)
    lv_2_text = title_font2.render("4", True, WHITE)
    screen.blit(lv_1_text, [250, 310])
    screen.blit(lv_2_text, [730, 310])

    # Update bar
    bar_3_4 += 1

    pygame.display.flip()
    clock.tick(60)

# score requirements for access to level 4 is 330

# variables for the easter egg
level_4_easter_egg_moon_location = (500, 75)
level_4_easter_egg_moon_radius = 75
# if the easter_egg has been clicked
easter_egg = False

while running and score < 460:
    #  EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == MOUSEBUTTONDOWN:
            hit_target = target_4.collidepoint(event.pos)
            if hit_target == 1:
                score += 10

            # Update the target and target location
            target_4_location = (random.randint(100,
                                                950), random.randint(100, 550))
            target_4 = pygame.draw.circle(screen, (255, 0, 0),
                                          target_4_location, target_4_radius)

            hit_sun = target_4_sun.collidepoint(event.pos)
            if hit_sun == 1:
                easter_egg = True
        elif event.type == QUIT:
            running = False

    if easter_egg:
        screen.fill(WHITE)  # always the first drawing command
        # Background
        pygame.draw.rect(screen, (102, 51, 0), [0, 50, 1000, 600], 0)
        # sand
        pygame.draw.rect(screen, (133, 99, 57), [0, 50, 1000, 600], 0)
        # water
        pygame.draw.rect(screen, (6, 47, 143), [0, 50, 1000, 400], 0)
        # sky
        pygame.draw.rect(screen, (4, 10, 54), [0, 50, 1000, 250], 0)
        #stars in the night sky
        for i in range(50):
            rand_x = random.randint(0, 1000)
            rand_y = random.randint(50, 250)
            pygame.draw.circle(screen, (255, 255, 0), [rand_x, rand_y], 1)
        # moon
        pygame.draw.circle(screen, (168, 167, 167), level_4_easter_egg_moon_location, level_4_easter_egg_moon_radius, 0)
        # Moon fix
        pygame.draw.rect(screen, (255, 255, 255), [400, 0, 500, 50])
    else:
        #  DRAWING
        screen.fill(WHITE)  # always the first drawing command
        # Drawing code variables
        level_4_background_sun_radius = 75
        level_4_background_sun_location = (500, 75)
        # Background
        pygame.draw.rect(screen, (102, 51, 0), [0, 50, 1000, 600], 0)
        # sand
        pygame.draw.rect(screen, (243, 185, 97), [0, 50, 1000, 600], 0)
        # water
        pygame.draw.rect(screen, (17, 149, 237), [0, 50, 1000, 400], 0)
        for i in range(50):
            rand_x = random.randint(0, 1000)
            rand_y = random.randint(50, 450)
            pygame.draw.circle(screen, (255, 255, 255), [rand_x, rand_y], 1)
        for i in range(10):
            rand_x = random.randint(0, 1000)
            rand_length = random.randint(0, 500)
            rand_y = random.randint(50, 450)
            pygame.draw.line(screen, WHITE, [rand_x, rand_y],
                                [rand_x + rand_length, rand_y], 1)
        # sky
        pygame.draw.rect(screen, (79, 199, 255), [0, 50, 1000, 250], 0)
        # sun
        pygame.draw.circle(screen, (255, 255, 0), level_4_background_sun_location,
                            level_4_background_sun_radius, 0)
        # line 1
        point1 = 410, 60
        point2 = 330, 60
        pygame.draw.line(screen, YELLOW, point1, point2, 3)
        # line 2
        point1 = 410, 105
        point2 = 350, 150
        pygame.draw.line(screen, YELLOW, point1, point2, 3)
        # line 3
        point1 = 500, 165
        point2 = 500, 230
        pygame.draw.line(screen, YELLOW, point1, point2, 3)
        # line 4
        point1 = 590, 60
        point2 = 670, 60
        pygame.draw.line(screen, YELLOW, point1, point2, 3)
        # line 5
        point1 = 590, 105
        point2 = 650, 150
        pygame.draw.line(screen, YELLOW, point1, point2, 3)
        # line 6
        point1 = 445, 145
        point2 = 410, 205
        pygame.draw.line(screen, YELLOW, point1, point2, 3)
        # line 7
        point1 = 555, 145
        point2 = 590, 205
        pygame.draw.line(screen, YELLOW, point1, point2, 3)
        # sun leaderboard fix
        pygame.draw.rect(screen, (255, 255, 255), [400, 0, 500, 50])

    # Display new target location
    pygame.draw.circle(screen, (255, 0, 0), target_4_location, target_4_radius)

    # Update scoreboard
    score_text = text_font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, [5, 5])

    # Display level
    level_text = text_font.render("Level 4", True, (0, 0, 0))
    screen.blit(level_text, [925, 5])

    pygame.display.flip()
    clock.tick(60)

# Level up screen from 4-5
# How long the bar has been running for
bar_4_5 = 0
# Emmpty bar
level_4_5_bar = pygame.Rect(299, 299, 402, 52)
# Run
while running and bar_4_5 < 400:
    # Handle and process events
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # Exit loop if user clicks esc
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            # Exit loop if user cicks exit
            running = False

    progress_4_5_bar = pygame.Rect(300, 300, bar_4_5, 50)
    #  DRAWING
    screen.fill(BLACK)  # always the first drawing command

    # Draw the bar
    pygame.draw.rect(screen, WHITE, level_4_5_bar, 1)
    pygame.draw.rect(screen, BLACK, progress_4_5_bar, 0)

    # #Loading Text
    load_title = load_font.render('TURN BACK NOW', True, WHITE)
    screen.blit(load_title, [310, 310])

    # Write levels
    lv_1_text = title_font2.render("4", True, WHITE)
    lv_2_text = title_font2.render("5", True, WHITE)
    screen.blit(lv_1_text, [250, 310])
    screen.blit(lv_2_text, [730, 310])

    # Update bar
    bar_4_5 += 1

    pygame.display.flip()
    clock.tick(60)

# score requirements for access to level 5 460
# counter for level 5
random_counter = 0
while running:
    #  EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == MOUSEBUTTONDOWN:
            hit_target = target_5.collidepoint(event.pos)
            if hit_target == 1:
                score += 10

            # Update the target 5 and target 5 location
            target_5_location = (random.randint(100,
                                                950), random.randint(100, 550))
            target_5 = pygame.draw.circle(screen, (0, 0, 255),
                                          target_5_location, target_5_radius)

        elif event.type == QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    #  DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command

    # Background
    # Smoke
    for i in range(60):
        rand_x = random.randint(0, 1000)
        rand_y = random.randint(0, 500)
        darkness = random.randint(0, 255)
        pygame.draw.circle(screen, (darkness, darkness, darkness),
                           [rand_x, rand_y], 125)
    # Volcano
    pygame.draw.polygon(screen, BLACK,
                        [[0, 500], [1000, 500], [550, 300], [450, 300]], 0)
    pygame.draw.rect(screen, BLACK, [0, 500, 1000, 100], 0)
    # Flame bits
    for i in range(100):
        rand_x = random.randint(450, 550)
        y = 300
        # Spray up
        while y >= 0:
            pygame.draw.circle(screen, (255, random.randint(0, 255), 0),
                               [rand_x, y], 3)
            y -= 1
    # Random bits
    for i in range(60):
        rand_x = random.randint(0, 1000)
        rand_y = random.randint(0, 600)
        pygame.draw.circle(screen, (255, random.randint(0, 255), 0),
                           [rand_x, rand_y], 2)

    # Update new target location
    if random_counter % 30 == 0:
        target_5_location = (random.randint(100,
                                            950), random.randint(100, 550))
        target_5 = pygame.draw.circle(screen, (0, 0, 255), target_5_location,
                                      target_5_radius)
    # Update the counter
    random_counter = random_counter + 1 % 30

    # Display new target location
    pygame.draw.circle(screen, (255, 0, 0), target_5_location, target_5_radius)

    # Update scoreboard
    score_text = text_font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, [5, 5])

    # Display level
    level_text = text_font.render("Level 5", True, (0, 0, 0))
    screen.blit(level_text, [925, 5])

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(120)
    # ---------------------------

in_game = True
while in_game:
    #  EVENT HANDLING
    for event in pygame.event.get():
        if event.type == QUIT:
            in_game = False
    screen.fill(BLACK)
    game_over_text1 = game_over_font.render("GAME OVER, you damn panzy", True,
                                            (WHITE))
    game_over_text2 = game_over_font.render(
        "You hella trash, hit up some aimlabs then come", True, (WHITE))
    screen.blit(game_over_text1, [250, 400])
    screen.blit(game_over_text2, [150, 500])

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(60)
    # ---------------------------

pygame.quit()
