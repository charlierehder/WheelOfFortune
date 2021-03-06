import random

# CONSTRUCT VOWEL LIST
vowel_list = ['a', 'e', 'i', 'o', 'u']

def getWord():
    with open('phrases.txt', 'r') as f:
        return random.choice(f.readlines()).strip()

def spinWheel():
    rand_val = random.random()
    if rand_val < 0.29:
        return 500
    elif rand_val >= 0.29 and rand_val < 0.46:
        return 600
    elif rand_val >= 0.46 and rand_val < 0.58:
        return 650
    elif rand_val >= 0.58 and rand_val < 0.71:
        return 700
    elif rand_val >= 0.71 and rand_val < 0.75:
        return 800
    elif rand_val >= 0.75 and rand_val < 0.79:
        return 900
    elif rand_val >= 0.79 and rand_val < 0.83:
        return 5000
    elif rand_val >= 0.83 and rand_val < 0.91:
        return -1 # BANKRUPT
    else:
        return -2 # LOSE A TURN

def guessALetter(correct_word, display_list, vowel):
    
    # GET INPUT 
    while True:
        try:
            guess = input("Guess a letter: ").strip()
        except ValueError:
            print("Please guess a letter")
        else:
            if len(guess) > 1:
                print("You must guess a single letter")
            elif not vowel and guess in vowel_list:
                print("Nice try, but you have to guess a consonant")
            elif vowel and guess not in vowel_list:
                print("Please guess a vowel... You paid for it...")
            else:
                break # VALID LETTER

    # CHECK IF GUESS IS IN WORD
    guess_in_word = False
    for i,v in enumerate(correct_word):
        if v == guess:
            guess_in_word = True
            display_list[i] = guess

    return guess_in_word

def printMenu(correct_word, display_list, player_dict):

    # DISPLAY VISUAL AND MENU
    print("**" + ("*" * (len(correct_word)+2)) + "**")
    print("** " + "".join(display_list) + " **")
    print("**" + ("*" * (len(correct_word)+2)) + "**")
    print("| Player 1 | Player 2 | Player 3 |")
    print(f"|  ${str(player_dict[1][0]).zfill(5)}  |  ${str(player_dict[2][0]).zfill(5)}  |  ${str(player_dict[3][0]).zfill(5)}  |") 
    print("1. Spin the wheel - 2. Buy a vowel - 3. Guess a word")

def printRound3Menu(correct_word, display_list):

    # DISPLAY ROUND 3 VISUAL
    print("**" + ("*" * (len(correct_word)+2)) + "**")
    print("** " + "".join(display_list) + " **")
    print("**" + ("*" * (len(correct_word)+2)) + "**")
    print("1. Guess Consonant - 2. Guess Vowel - 3. Guess the word")


# BUILD PLAYER DICT W PLAYER ID AND ROUND TOTAL AND GAME TOTAL SET TO ZERO
player_dict = {}
player_dict[1] = [0,0]
player_dict[2] = [0,0]
player_dict[3] = [0,0]

for round_num in range(1,4): # ITERATE THROUGH ROUND 1-3
   
    # GET TARGET WORD FOR THE ROUND
    correct_word = getWord()

    # BUILD DISPLAY
    display_list = ['_'] * len(correct_word)
    for i,v in enumerate(correct_word):
        if v == " ":
            display_list[i] = " "

    # SET INITIAL ROUND VALUES FOR EACH ROUND
    player_dict[1][0] = 0 
    player_dict[2][0] = 0
    player_dict[3][0] = 0

    # INITALIZE CURRENT PLAYER
    current_player_id = 1

    print(correct_word)

    print(f"------ ROUND {round_num} ------")

    if round_num != 3: # ROUND 1 AND 2

        word_guessed = False
        while not word_guessed: # LOOP OVER EACH PLAYER
            
            print(f"It's Player {current_player_id}'s turn")
            while True: # LOOP OVER EACH ACTION
                try:    
                    printMenu(correct_word, display_list, player_dict)
                    option_num = int(input("Please select an option: "))
                except ValueError:
                    print("Please give a valid input")
                else:
                    if option_num == 1: # SPIN WHEEL

                        print("Spinning...")
                        outcome = spinWheel()
                        if outcome == -1: # BANKRUPT
                            player_dict[current_player_id][0] = 0
                            print("You went bankrupt")
                            break
                        elif outcome == -2: # LOSE A TURN
                            print("You lost a turn")
                            break
                        else: # GOT MONEY 
                            player_dict[current_player_id][0] += outcome
                            print(f"You recieved ${outcome}")

                        if not guessALetter(correct_word, display_list, vowel=False):
                            print("That letter was not on the board")
                            break
                        print("That letter was correct")

                    elif option_num == 2: # BUY A VOWEL

                        if player_dict[current_player_id][0] - 250 > 0:
                            print("Alright, you're buying a vowel")
                            player_dict[current_player_id][0] -= 250
                            if not guessALetter(correct_word, display_list, vowel=True):
                                print("That letter was not on the board")
                                break
                            print("That letter was correct")
                        else:
                            print("You can't buy a vowel right now")

                    elif option_num == 3: # GUESS WORD
                        
                        # GET PLAYER GUESS
                        guess = input("Guess the word: ").strip()

                        # CHECK GUESS
                        if guess == correct_word: # GUESSED CORRECTLY
                            print(f"You guessed correctly. You just earned ${player_dict[current_player_id][0]}")
                            player_dict[current_player_id][1] += player_dict[current_player_id][0]
                            word_guessed = True
                        else: # GUESS WAS INCORRECT
                            print("That was incorrect")
                        break

                    else:
                        print("Please enter either '1', '2' or '3'")

            current_player_id = current_player_id + 1 if current_player_id <= 2 else 1

    else: # ROUND 3

        # FIND PLAYER WITH MAX BANK
        current_player_id = 1
        for i in range(1,4):
            if player_dict[i][1] > player_dict[current_player_id][1]:
                current_player_id = i

        print(f"Player {current_player_id} has made it to the final round")

        for i,v in enumerate(correct_word):
            if v == "r":
                display_list[i] = "r"
            elif v == "s":
                display_list[i] = "s"
            elif v == "t":
                display_list[i] = "t"
            elif v == "l":
                display_list[i] = "l"
            elif v == "n":
                display_list[i] = "n"
            elif v == "e":
                display_list[i] = "e"

        print("You can guess up to 3 consonants and 1 vowel. Some of the letters have already been revealed for you.")

        allowed_consonants = 3
        allowed_vowels = 1

        while True:

            try:
                printRound3Menu(correct_word, display_list)
                option_num = int(input("Please choose an option: ")) 
            except ValueError:
                print("Please choose a valid option")
            else:
                if option_num == 1: # GUESS A CONSONANT
                    
                    if allowed_consonants > 0:
                        allowed_consonants -= 1
                        if guessALetter(correct_word, display_list, vowel=False):
                            print("That letter was in the word")
                        else:
                            print("That letter was not in the word")
                    else:
                        print("You can't guess anymore consonants")

                elif option_num == 2: # GUESS A VOWEL

                    if allowed_vowels > 0:
                        allowed_vowels -= 1
                        if guessALetter(correct_word, display_list, vowel=True):
                            print("That letter was in the word")
                        else:
                            print("That letter was not in the word")
                    else:
                        print("You can't guess anymore vowels")

                elif option_num == 3: # GUESS FINAL WORD

                    guess = input("Guess the final word: ").strip()
                    if guess == correct_word:
                        print("YOU JUST WON $8 TRILLION! CONGRATS")
                    else:
                        print("You did not win the final cash prize")
                    break
                else:
                    print("Please choose a valid option")

