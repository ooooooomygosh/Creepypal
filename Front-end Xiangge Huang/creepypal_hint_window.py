import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 300, 100  # Size of the hint window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Creepypal Hint Window')

# Set the position of the window to the top-right corner
window_position = (pygame.display.Info().current_w - screen_width, 0)
pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)
pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)
pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

# Set up font
font = pygame.font.SysFont(None, 36)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (e.g., white)
    screen.fill((255, 255, 255))

    # Render the hint text
    hint_text = font.render('Xiangge-Huang try to Display', True, (0, 0, 0))
    screen.blit(hint_text, (10, 10))

    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()
