import pygame
import FEengine

# Set up the display
screen_width = 600
screen_height = 400
MAX_FPS = 15

# Initialize size
SQ_SIZE = player_width = player_height = 50

#Initialise image
IMAGES = {}
def loadImages():
    units = ['pUnit','eUnit']
    for unit in units:
        IMAGES[unit] = pygame.transform.scale(pygame.image.load("images/"+unit+".png"),(SQ_SIZE,SQ_SIZE))

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

    #Flags
    sqSelected = () #Init nothing being selected
    playerClicks = [] #Keep track of player clicks

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Player Select
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                mcol = location[0]//SQ_SIZE
                mrow = location[1]//SQ_SIZE

                if sqSelected == (mrow,mcol):
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (mrow,mcol)
                    playerClicks.append(sqSelected)

                if len(playerClicks) == 2:  
                    move = FEengine.Move(playerClicks[0],playerClicks[1],gs.board)
                    gs.makeMove(move)
                    sqSelected = () #Reset user clicks
                    playerClicks = [] #Reset user clicks
                

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
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((col * SQ_SIZE), (row * SQ_SIZE), SQ_SIZE, SQ_SIZE))
            else:
                pygame.draw.rect(screen, (196, 164, 132), pygame.Rect((col * SQ_SIZE), (row * SQ_SIZE), SQ_SIZE, SQ_SIZE))
        for col in range(2):
            pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(((5+col) * SQ_SIZE), (row * SQ_SIZE), SQ_SIZE, SQ_SIZE))
    
def drawUnits(screen,board):
    for row in range(8):
        for col in range(12):
            unit = board[row][col]
            if unit != "--":
                screen.blit(IMAGES[unit],pygame.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()