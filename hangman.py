import sys
import os

word = []
new = []

initial = input("Word: ")
for char in initial:
    if char.isalpha() == False and char != " ":
        print("Only Use Letters and Spaces")
        sys.exit(1)
    word += char
lives = 10
used = []

def choice():
    os.system("clear")
    global new
    global used
    global lives
    amount = 0
    for char in word:
        if char.isalpha() == True:
            print("_", end=' ')
        else:
            print(" ", end=' ')
    guess = input("\nGuess: ")
    if (len(guess) != 1) or (guess.isalpha() == False):
        choice()
    used += guess
    for i in range(len(word)):
        if word[i] == guess:
            new += guess
            amount += 1
        elif word[i] == " ":
            new += " "
        else:
            new += "_"
    for letter in new:
        print(letter, end=' ')
    print("\n")
    if amount == 0:
        lives -= 1
    draw(lives)
    if (check(new, word) == True):
        print("YOU WIN!")
        sys.exit(1)
    else:
        achoice()



def achoice():
    global new
    global used
    global lives
    amount = 0
    guess = input("Guess: ")
    if (len(guess) != 1) or (guess.isalpha() == False):
        achoice()
    if guess in used:
        print("You already guesssed that letter")
        achoice()
    used += guess
    for i in range(len(word)):
        if (word[i] == guess) and (new[i] == "_"):
            new[i] = word[i]
            amount += 1
    for letter in new:
        print(letter, end=" ")
    print("\n")
    if amount == 0:
        lives -= 1
    draw(lives)
    if (check(new, word) == True):
        print("\nYOU WIN!")
        sys.exit(1)
    else:
        achoice()


def check(new, old):
    if new == old:
        return True
    else:
        return False

def draw(lives):
    if lives == 10:
        print("        ------")
        print("        |     |")
        print("        |     ")
        print("        |     ")
        print("        |")
        print("        |")
        print("      -----")
    if lives == 9:
        print("        ------")
        print("        |     |")
        print("        |     0")
        print("        |     ")
        print("        |")
        print("        |")
        print("      -----")
    if lives == 8:
        print("        ------")
        print("        |     |")
        print("        |     0")
        print("        |     |")
        print("        |")
        print("        |")
        print("      -----")
    if lives == 7:
        print("        ------")
        print("        |     |")
        print("        |     0/")
        print("        |     |")
        print("        |")
        print("        |")
        print("      -----")
    if lives == 6:
        print("        ------")
        print("        |     |")
        print("        |    \\0/")
        print("        |     |")
        print("        |    ")
        print("        |")
        print("      -----")
    if lives == 5:
        print("        ------")
        print("        |     |")
        print("        |    \\0/")
        print("        |     |")
        print("        |    /")
        print("        |")
        print("      -----")
    if lives == 4:
        print("        ------")
        print("        |     |")
        print("        |    \\0/")
        print("        |     |")
        print("        |    / \\")
        print("        |")
        print("      -----")
    if lives == 3:
        print("        ------")
        print("        |     |")
        print("        |    \\0/")
        print("        |     |")
        print("        |    / \\")
        print("        |       o")
        print("      -----")
    if lives == 2:
        print("        ------")
        print("        |     |")
        print("        |    \\0/")
        print("        |     |")
        print("        |    / \\")
        print("        |   o   o")
        print("      -----")
    if lives == 1:
        print("        ------")
        print("        |   o |")
        print("        |    \\0/")
        print("        |     |")
        print("        |    / \\")
        print("        |   o   o")
        print("      -----")
    if lives == 0:
        print("YOU LOSE!")
        print("The correct word is ", end="")
        for letter in word:
            print(letter, end=" ")
        print("\n")
        sys.exit(1)
        
choice()