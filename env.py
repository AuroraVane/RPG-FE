import pygame
import FEengine

# Set up the display
screen_width = 600
screen_height = 400
MAX_FPS = 15

# Initialize size
square_width = player_width = player_height = 50

#Initialise image
IMAGES = {}
def loadImages():
    units = ['pUnit','eUnit']
    for unit in units:
        IMAGES[unit] = pygame.transform.scale(pygame.image.load("images/"+unit+".png"),(square_width,square_width))

# Game loop
def main():

    # Initialize Pygame
    pygame.init()

    #Display
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("RPG-FE")
    ICON = pygame.image.load('images/wp.png')
    pygame.display.set_icon(ICON)

    #System Requisites
    clock = pygame.time.Clock()
    gs = FEengine.GameState() #gamestate
    loadImages()

    running = True
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
                        col = (event.pos[0]) // square_width
                        row = (event.pos[1]) // square_width
                        player1_x = col * square_width
                        player1_y = row * square_width
                        player1_select = False
                        print(col,row)
                    elif player2_select:
                        col = (event.pos[0]) // square_width
                        row = (event.pos[1]) // square_width
                        player2_x = col * square_width
                        player2_y = row * square_width
                        player2_select = False

                    player1_color = (255, 0, 0)
                    player2_color = (0, 0, 255)

        drawGameState(screen,gs)

        clock.tick(MAX_FPS)
        pygame.display.flip()
        pygame.display.update()

    # Quit Pygame
    pygame.quit()

def drawGameState(screen,gs):
    drawBoard(screen) #Draw squares on the board
    drawUnits(screen,gs.board) #Draw Units on top of the squares

def drawBoard(screen):
    # Draw board
    # Render graphics
    screen.fill((0, 0, 0))
    for row in range(8):
        for col in range(12):
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((col * square_width), (row * square_width), square_width, square_width))
            else:
                pygame.draw.rect(screen, (196, 164, 132), pygame.Rect((col * square_width), (row * square_width), square_width, square_width))
        for col in range(2):
            pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(((5+col) * square_width), (row * square_width), square_width, square_width))
    
def drawUnits(screen,board):
    for row in range(8):
        for col in range(12):
            unit = board[row][col]
            if unit != "--":
                screen.blit(IMAGES[unit],pygame.Rect(col*square_width, row*square_width, square_width, square_width))

if __name__ == "__main__":
    main()