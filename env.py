import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 640
screen_height = 440
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("RPG-FE")

# Initialize size
square_width = square_height = 50
border_width = border_height = 20
running = True

# Initialize player positions
player1_x = border_width
player1_y = border_height
player2_x = screen_width - square_width - border_width
player2_y = screen_height - square_height - border_height

player_width = square_width
player_height = square_height

player1_color = (255, 0, 0)
player2_color = (0, 0, 255)

# Flags
player1_select = False
player2_select = False

# Game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player Select
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect(player1_x, player1_y, player_width, player_height).collidepoint(event.pos):
                player1_color = (255, 255, 0)  # Change player 1 color to yellow
                player2_color = (0, 0, 255)
                player1_select = True
                player2_select = False
            elif pygame.Rect(player2_x, player2_y, player_width, player_height).collidepoint(event.pos):
                player2_color = (255, 255, 0)  # Change player 2 color to yellow
                player1_color = (255, 0, 0)
                player2_select = True
                player1_select = False
            else:
                if player1_select:
                    col = (event.pos[0] - border_width) // square_width
                    row = (event.pos[1] - border_height) // square_height
                    player1_x = border_width + col * square_width
                    player1_y = border_height + row * square_height
                    player1_select = False
                elif player2_select:
                    col = (event.pos[0] - border_width) // square_width
                    row = (event.pos[1] - border_height) // square_height
                    player2_x = border_width + col * square_width
                    player2_y = border_height + row * square_height
                    player2_select = False

                player1_color = (255, 0, 0)
                player2_color = (0, 0, 255)

    # Render graphics
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(0, 0, screen_width, screen_height))
    # Draw chessboard
    for row in range(8):
        for col in range(12):
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(border_width + (col * square_width), border_height + (row * square_height), square_width, square_height))
            else:
                pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(border_width + (col * square_width), border_height + (row * square_height), square_width, square_height))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, screen_width, border_height))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, border_width, screen_height))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, screen_height - border_height, screen_width, border_height))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(screen_width - border_width, 0, border_width, screen_height))
    pygame.draw.rect(screen, player1_color, pygame.Rect(player1_x, player1_y, player_width, player_height))
    pygame.draw.rect(screen, player2_color, pygame.Rect(player2_x, player2_y, player_width, player_height))

    pygame.display.flip()

# Quit Pygame
pygame.quit()