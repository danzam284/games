import random, os, sys, time, pygame
from playsound import playsound
def print_row(board):
    r = 0
    ytrack = 20
    for row in board:
        c = 0
        xtrack = 125
        for space in row:
            square = pygame.Rect(xtrack, ytrack, 48, 48)
            squares.append([square, space, r, c])
            xtrack += 50
            square_text = myfont.render(str(space), False, (255, 0, 0))
            screen.blit(square_text, (xtrack - 40, ytrack))
            pygame.draw.rect(screen, WHITE, square)
            c += 1
        ytrack += 50
        r += 1


def check_spot(board, squares, pos):
    i = 0
    for square in squares:
        if squares[i][0].collidepoint(pos):
            b = squares[i][1]
            squares.remove(squares[i])
            i -= 1
            if b == "M" and round != 1:
                os.system("Clear")
                print("YOU LOSE!")
                squares = []
                mode = "setup"
                return mode
            if b == " ":
                check_spot(board, squares, (pos[0] + 50, pos[1]))
                check_spot(board, squares, (pos[0] - 50, pos[1]))
                check_spot(board, squares, (pos[0], pos[1] + 50))
                check_spot(board, squares, (pos[0], pos[1] - 50))
                check_spot(board, squares, (pos[0] + 50, pos[1] + 50))
                check_spot(board, squares, (pos[0] + 50, pos[1] - 50))
                check_spot(board, squares, (pos[0] - 50, pos[1] + 50))
                check_spot(board, squares, (pos[0] - 50, pos[1] - 50))
        i += 1

def print_text(board):
    ytrack = 20
    for row in board:
        xtrack = 175
        for space in row:
            square_text = myfont.render(str(space), False, (255, 0, 0))
            screen.blit(square_text, (xtrack - 40, ytrack))
            xtrack += 50
        ytrack += 50

def assign(board, row, col):
    amt = 0
    if board[row][col] != "M":
        if row != 0 and col != 0 and board[row - 1][col - 1] == "M":
            amt += 1
        if row != 0 and board[row - 1][col] == "M":
            amt += 1
        if row != 0 and col != 14 and board[row - 1][col + 1] == "M":
            amt += 1
        if col != 0 and board[row][col - 1] == "M":
            amt += 1
        if col != 14 and board[row][col + 1] == "M":
            amt += 1
        if row != 14 and col != 0 and board[row + 1][col - 1] == "M":
            amt += 1
        if row != 14 and board[row + 1][col] == "M":
            amt += 1
        if row != 14 and col != 14 and board[row + 1][col + 1] == "M":
            amt += 1
        if amt == 0:
            board[row][col] = " "
        else:
            board[row][col] = amt

def check_win(board, flags):
    if len(squares) != 0:
        return False
    check = True
    if numMines != len(flags):
        return False
    for flag in flags:
        if board[flag[2]][flag[3]] != "M":
            return False
    return True



rows, cols = (15, 15)
mines = 30
board = [["_" for i in range(cols)] for j in range(rows)]
numMines = 0
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
BLACK = (0,0,0)
WHITE = (255,255,255)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (125, 125, 125)]
size_width = 1000
size_height = 1000
screen = pygame.display.set_mode((size_width, size_height))
pygame.display.set_caption("Minesweeper")
myfont = pygame.font.SysFont('Comic Sans MS', 30)
startfont = pygame.font.SysFont('Times New Roman', 50)
image = pygame.image.load(r'/Users/danzam284/Desktop/Code/minesweeperMine.jpg')
image = pygame.transform.scale(image, (48, 48))
squares = []
flags = []
mode = "setup"
submode = "none"
round = 0
timer = 0


while True:
    if mode == "start":
        start_text = startfont.render("Press Enter To Start", False, random.choice(colors))
        screen.blit(start_text, (300, 362))
    if submode == "win":
        win_text = startfont.render("YOU WIN!!!!", False, random.choice(colors))
        screen.blit(win_text, (355, 117))
    if submode == "lose":
        win_text = startfont.render("YOU LOSE!!!", False, random.choice(colors))
        screen.blit(win_text, (355, 117))
    if mode == "setup":
        timer = 0
        round = 0
        screen.fill(BLACK)
        print_text(board)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "M":
                    screen.blit(image, (125 + 50 * j, 20 + 50 * i))
        pygame.display.flip()
        if submode == "lose":
            #playsound('/Users/danzam284/Desktop/Code/Explosion6.wav')
            time.sleep(2)
        board = [["_" for i in range(cols)] for j in range(rows)]
        numMines = 0
        mines = 30
        flags = []
        squares = []
        for i in range(mines):
            row, col = (random.randint(0, 14), random.randint(0, 14))
            if board[row][col] == "_":
                board[row][col] = "M"
                numMines += 1
            else:
                mines += 1
        for i in range(rows):
            for j in range(cols):
                assign(board, i, j)
        print_row(board)
        mode = "start"


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            mode = "game"
            submode = "none"
        if mode == "game":
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    round += 1
                    pos = pygame.mouse.get_pos()
                    if check_spot(board, squares, pos) == "setup":
                        mode = "setup"
                        submode = "lose"
                if event.button == 3:
                    #playsound('/Users/danzam284/Desktop/Code/Randomize5-[AudioTrimmer.com].wav')
                    done = False
                    pos = pygame.mouse.get_pos()
                    for square in squares:
                        if square[0].collidepoint(pos):
                            done = True
                            squares.remove(square)
                            flags.append(square)
                    for flag in flags:
                        if flag[0].collidepoint(pos) and not done:
                            squares.append(flag)
                            flags.remove(flag)

        if check_win(board, flags):
            os.system("Clear")
            print("YOU WIN!")
            mode = "setup"
            submode = "win"
            #playsound('/Users/danzam284/Desktop/Code/Powerup18.wav')

        screen.fill(BLACK)
        print_text(board)
        for square in squares:
            pygame.draw.rect(screen, WHITE, square[0])
        for flag in flags:
            pygame.draw.rect(screen, (0, 0, 255), flag[0])
            screen.blit(image, (flag[0].left, flag[0].top))
        timer_text = screen.blit(startfont.render(str(timer), False, (0, 255, 0)), (0, 0))
    pygame.display.flip()
    clock.tick()
