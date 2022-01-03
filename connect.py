import numpy, sys, pygame, time
pygame.init()
screen_height = 600
screen_width = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Connect 4')
clock = pygame.time.Clock()
board = [["_"]*7 for i in range(6)]
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (150, 0, 255)
turn = 1
slow = False
stop = False
font_text = pygame.font.SysFont('Courier New', 50)
red_win_text = font_text.render("RED WINS!", True, RED)
blue_win_text = font_text.render("BLUE WINS!", True, BLUE)
press = False
Go = True
    
def placement(row):
    global turn
    for i in range(6):
        if board[5 - i][row - 1] == "_":
            board[5 - i][row - 1] = turn
            if turn == 1:
                turn = 2
            else:
                turn = 1
            break
    check()


def draw_rectangles(mouse, pressed, stop):
    global slow, Go
    if Go:
        for x in range(7):
            for y in range(6):
                if board[y][x] == "_":
                    col = WHITE
                if board[y][x] == 1:
                    col = RED
                if board[y][x] == 2:
                    col = BLUE
                rect = pygame.Rect(x * 100 + 25, y * 100 + 50, 50, 50)
                pygame.draw.rect(screen, col, rect)
        button1 = pygame.Rect(37, 12, 25, 25)
        button2 = pygame.Rect(137, 12, 25, 25)
        button3 = pygame.Rect(237, 12, 25, 25)
        button4 = pygame.Rect(337, 12, 25, 25)
        button5 = pygame.Rect(437, 12, 25, 25)
        button6 = pygame.Rect(537, 12, 25, 25)
        button7 = pygame.Rect(637, 12, 25, 25)
        pygame.draw.rect(screen, PURPLE, button1)
        pygame.draw.rect(screen, PURPLE, button2)
        pygame.draw.rect(screen, PURPLE, button3)
        pygame.draw.rect(screen, PURPLE, button4)
        pygame.draw.rect(screen, PURPLE, button5)
        pygame.draw.rect(screen, PURPLE, button6)
        pygame.draw.rect(screen, PURPLE, button7)

        if (slow == False):
            global press
            if button1.collidepoint(mouse) and press and any(pressed):
                placement(1)
                #slow = True
            if button2.collidepoint(mouse) and press and any(pressed):
                placement(2)
                #slow = True
            if button3.collidepoint(mouse) and press and any(pressed):
                placement(3)
                #slow = True
            if button4.collidepoint(mouse) and press and any(pressed):
                placement(4)
                #slow = True
            if button5.collidepoint(mouse) and press and any(pressed):
                placement(5)
                #slow = True
            if button6.collidepoint(mouse) and press and any(pressed):
                placement(6)
                #slow = True
            if button7.collidepoint(mouse) and press and any(pressed):
                placement(7)
                #slow = True
        
        if stop:
            Go = False

        

def check():
    global stop
    boardHeight = len(board[0])
    boardWidth = len(board)

    #Player 1
    for y in range(boardHeight):
        for x in range(boardWidth - 3):
            if board[x][y] == 1 and board[x+1][y] == 1 and board[x+2][y] == 1 and board[x+3][y] == 1:
                screen.blit(red_win_text, (250, 200))
                stop = True

    for x in range(boardWidth):
        for y in range(boardHeight - 3):
            if board[x][y] == 1 and board[x][y+1] == 1 and board[x][y+2] == 1 and board[x][y+3] == 1:
                screen.blit(red_win_text, (250, 200))
                stop = True

    for x in range(boardWidth - 3):
        for y in range(3, boardHeight):
            if board[x][y] == 1 and board[x+1][y-1] == 1 and board[x+2][y-2] == 1 and board[x+3][y-3] == 1:
                screen.blit(red_win_text, (250, 200))
                stop = True

    for x in range(boardWidth - 3):
        for y in range(boardHeight - 3):
            if board[x][y] == 1 and board[x+1][y+1] == 1 and board[x+2][y+2] == 1 and board[x+3][y+3] == 1:
                screen.blit(red_win_text, (250, 200))
                stop = True

    #Player 2
    for y in range(boardHeight):
        for x in range(boardWidth - 3):
            if board[x][y] == 2 and board[x+1][y] == 2 and board[x+2][y] == 2 and board[x+3][y] == 2:
                screen.blit(blue_win_text, (250, 200))
                stop = True

    for x in range(boardWidth):
        for y in range(boardHeight - 3):
            if board[x][y] == 2 and board[x][y+1] == 2 and board[x][y+2] == 2 and board[x][y+3] == 2:
                screen.blit(blue_win_text, (250, 200))
                stop = True

    for x in range(boardWidth - 3):
        for y in range(3, boardHeight):
            if board[x][y] == 2 and board[x+1][y-1] == 2 and board[x+2][y-2] == 2 and board[x+3][y-3] == 2:
                screen.blit(blue_win_text, (250, 200))
                stop = True

    for x in range(boardWidth - 3):
        for y in range(boardHeight - 3):
            if board[x][y] == 2 and board[x+1][y+1] == 2 and board[x+2][y+2] == 2 and board[x+3][y+3] == 2:
                screen.blit(blue_win_text, (250, 200))
                stop = True

while Go:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                press = True

    mouse = pygame.mouse.get_pos() 
    pressed = pygame.mouse.get_pressed()
    draw_rectangles(mouse, pressed, stop)
    pygame.display.flip()
    clock.tick()
    if any(pressed):
        press = False

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    pygame.display.flip()
    clock.tick()
    