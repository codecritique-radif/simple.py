import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fighting Game")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a background color
    screen.fill((255, 255, 255))

    # Update the game display
    pygame.display.update()

# Quit Pygame
pygame.quit()
This is just a starting point, and you can build upon it to create a more complex and interactive fighting game. You'll need to add characters, controls, collision detection, and animations to make it a full-fledged game. Additionally, you can incorporate sound effects, scoring, and different game modes to enhance the gameplay experience.





User
Make more complex

ChatGPT
Sure! Here's an example of a more complex fighting game using Pygame:

python
Copy code
import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fighting Game")

# Load game assets
background_image = pygame.image.load("background.png")
player_image = pygame.image.load("player.png")
enemy_image = pygame.image.load("enemy.png")

# Set initial positions for the player and enemy
player_x = 100
player_y = screen_height - player_image.get_height() - 50
enemy_x = screen_width - enemy_image.get_width() - 100
enemy_y = screen_height - enemy_image.get_height() - 50

# Set player movement variables
player_speed = 5
is_left_pressed = False
is_right_pressed = False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                is_left_pressed = True
            elif event.key == pygame.K_RIGHT:
                is_right_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                is_left_pressed = False
            elif event.key == pygame.K_RIGHT:
                is_right_pressed = False

    # Move the player based on keyboard input
    if is_left_pressed:
        player_x -= player_speed
    if is_right_pressed:
        player_x += player_speed

    # Ensure the player stays within the screen boundaries
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_image.get_width():
        player_x = screen_width - player_image.get_width()

    # Fill the screen with the background image
    screen.blit(background_image, (0, 0))

    # Draw the player and enemy on the screen
    screen.blit(player_image, (player_x, player_y))
    screen.blit(enemy_image, (enemy_x, enemy_y))

    # Update the game display
    pygame.display.update()

# Quit Pygame
pygame.quit()

