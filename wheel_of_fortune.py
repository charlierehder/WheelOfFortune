import random

def getWord():
    with open('words.txt', 'r') as f:
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


# BUILD PLAYER DICT W PLAYER ID AND ROUND TOTAL AND GAME TOTAL SET TO ZERO
player_dict = dict.fromkeys(range(1,4), [0,0])
print(player_dict)

for i in range(1,4): # ITERATE THROUGH ROUND 1-3
   
    # GET TARGET WORD FOR THE ROUND
    correct_word = getWord()

    # BUILD DISPLAY
    display_list = ['_'] * len(correct_word)

    # SET INITIAL ROUND VALUES FOR EACH ROUND
    player_dict[1][0] = 0 
    player_dict[1][0] = 0
    player_dict[1][0] = 0

    # INITALIZE CURRENT PLAYER
    current_player_id = 1

    word_guessed = False
    while not word_guessed: # LOOP OVER EACH PLAYER
        
        print(f"It's Player {current_player_id}'s turn")
        
        while True: # LOOP OVER EACH ACTION
            try:    
                # DISPLAY VISUAL AND MENU
                print("|" + ("-" * (len(correct_word)+2)) + "|")
                print("| " + "".join(display_list) + " |")
                print("|" + ("-" * (len(correct_word)+2)) + "|")
                print("1. Spin the wheel")
                print("2. Buy a vowel")
                print("3. Guess a word")
                option_num = int(input("Please select an option: "))
            except ValueError:
                print("Please give a valid input")
            else:
                if option_num == 1:
                    print(spinWheel())
                elif option_num == 2:
                    print("BuyAVowel()")
                elif option_num == 3: # GUESS WORD
                    
                    # GET PLAYER GUESS
                    guess = input("Guess the word: ").strip()

                    # CHECK GUESS
                    if guess == correct_word: # GUESSED CORRECTLY
                        print(f"You guessed correctly. 
                                You just earned ${player_dict[current_player_id[0]}")
                        player_dict[current_player_id][1] += player_dict[current_player_id][0]
                        word_guessed = True
                    else: # GUESS WAS INCORRECT
                        print("That was incorrect")
                else:
                    print("Please enter either '1', '2' or '3'")
            break
        current_player_id = current_player_id + 1 if current_player_id <= 2 else 1
