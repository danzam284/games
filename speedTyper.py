import pygame, random, sys
pygame.init()
pygame.font.init()
checker = 75
myfont = pygame.font.SysFont('arial', 30)
timerfont = pygame.font.SysFont('arial', 50)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
screen_height = 400
screen_width = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
timer = 0
mistakes = 0
screen.fill(WHITE)
sequence = ""
sequence2 = ""
sequence3 = ""
sequence4 = ""
sequence5 = ""
words = ["hello", "apple", "penguin", "armadillo", "a", "original", "nut", "from", "to", "of", "sand", "charge", "erupt", "picture",
"wall", "frame", "brake", "seven", "come", "out", "after", "tomorrow", "why", "igloo", "uranium", "phone", "amazing", "cool",
"chair", "door", "ugly", "knee", "elbow", "banana", "guitar", "trumpet", "ok", "can", "pillow", "thunder", "please", "shut", "up",
"podcast", "cherry", "phone", "blue", "back", "super", "glue", "bag", "bagel", "said", "olive", "french", "japan", "plane", "weight",
"soon", "almost", "about", "kill", "savor", "new", "how", "pop", "below", "store", "mexican", "burrito", "bowling", "eagle", "strike"
"bleeding", "compartment", "breakable", "calculation", "bludgeon", "glumly", "fight", "communion", "dismember", "glow", "burial",
"cage", "hamster", "dog", "food", "seed", "bed", "rest", "nap", "blue", "globe", "area", "country", "dispose", "trash", "ham", "in",
"tissue", "retainer", "clock", "text", "image", "sheet", "quiet", "angry", "sincere", "apologize", "letter", "bar", "lamp", "curse"]

for i in range (10):
    sequence  += random.choice(words)
    sequence  += " "
    sequence2 += random.choice(words)
    sequence2 += " "
    sequence3 += random.choice(words)
    sequence3 += " "
    sequence4 += random.choice(words)
    sequence4 += " "
    sequence5 += random.choice(words)
    sequence5 += " "

while True:
    timer = (pygame.time.get_ticks() / 1000)
    if (len(sequence) == 1) and (sequence2 != "") and (sequence2 != " "):
        sequence = sequence2
        sequence2 = sequence3
        sequence3 = sequence4
        sequence4 = sequence5
        sequence5 = ""
    if (len(sequence) == 1) and (sequence2 == "" or sequence2 == " "):
        print("You typed 50 words in " + str(timer) + "seconds which is " + str(50 / timer * 60) + " words per minute!")
        print("You had " + str(mistakes) + " mistakes.")
        sys.exit(1)
    next_key = sequence[0]
    timersurface = timerfont.render(str(timer), False, (255, 0, 0))
    textsurface = myfont.render(sequence, False, BLACK)
    textsurface2 = myfont.render(sequence2, False, BLACK)
    textsurface3 = myfont.render(sequence3, False, BLACK)
    textsurface4 = myfont.render(sequence4, False, BLACK)
    textsurface5 = myfont.render(sequence5, False, BLACK)
    screen.blit(timersurface, (230, 0))
    screen.blit(textsurface,(0, checker))
    screen.blit(textsurface2,(0, 2 * checker))
    screen.blit(textsurface3,(0, 3 * checker))
    screen.blit(textsurface4,(0, 4 * checker))
    screen.blit(textsurface5,(0, 5 * checker))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if (next_key == 'a'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_b:
                if (next_key == 'b'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_c:
                if (next_key == 'c'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_d:
                if (next_key == 'd'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_e:
                if (next_key == 'e'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_f:
                if (next_key == 'f'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_g:
                if (next_key == 'g'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_h:
                if (next_key == 'h'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_i:
                if (next_key == 'i'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_j:
                if (next_key == 'j'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_k:
                if (next_key == 'k'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_l:
                if (next_key == 'l'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_m:
                if (next_key == 'm'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_n:
                if (next_key == 'n'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_o:
                if (next_key == 'o'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_p:
                if (next_key == 'p'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_q:
                if (next_key == 'q'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_r:
                if (next_key == 'r'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_s:
                if (next_key == 's'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_t:
                if (next_key == 't'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_u:
                if (next_key == 'u'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_v:
                if (next_key == 'v'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_w:
                if (next_key == 'w'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_x:
                if (next_key == 'x'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_y:
                if (next_key == 'y'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_z:
                if (next_key == 'z'):
                    sequence = sequence[1:]
                else:
                    mistakes += 1
            if event.key == pygame.K_SPACE:
                if (next_key == ' '):
                    sequence = sequence[1:]
    pygame.display.flip()
    screen.fill(WHITE)
    clock.tick()

