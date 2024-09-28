import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 400, 200  # Increased size for more elements
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

# Button setup
button_color = (0, 128, 255)
button_rect = pygame.Rect(10, 50, 100, 40)
button_text = font.render('Click Me', True, (255, 255, 255))

# Text input setup
input_box = pygame.Rect(10, 100, 140, 40)
input_color = (0, 0, 0)
input_text = ''
active = False

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print("Button clicked!")
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
        elif event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    print(input_text)
                    input_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

    # Fill the screen with a color (e.g., white)
    screen.fill((255, 255, 255))

    # Render the hint text
    hint_text = font.render('Xiangge-Huang try to Display', True, (0, 0, 0))
    screen.blit(hint_text, (10, 10))

    # Draw the button
    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, (button_rect.x + 10, button_rect.y + 5))

    # Draw the input box
    pygame.draw.rect(screen, input_color, input_box, 2)
    input_surface = font.render(input_text, True, input_color)
    screen.blit(input_surface, (input_box.x + 5, input_box.y + 5))

    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()
