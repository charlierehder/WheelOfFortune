import random

def getWord():
    with open('words.txt', 'r') as f:
        return random.choice(f.readlines()).strip()

for i in range(1,4): # ITERATE THROUGH ROUND 1-3
   
    # GET TARGET WORD FOR THE ROUND
    display_list = getWord()
    print("".join(display_list))

    word_guessed = False
    while not word_guessed: # LOOP OVER EACH PLAYER

        while True: # LOOP OVER EACH ACTION
            try:    
                print("----------------")
                print("WHEEL OF FORTUNE")
                print("----------------")
                print("1. Spin the wheel")
                print("2. Buy a vowel")
                print("3. Guess a word")
                option_num = int(input("Please select an option: "))
            except ValueError:
                print("Please give a valid input")
            else:
                if option_num == 1:
                    print("SpinWheel()")
                elif option_num == 2:
                    print("BuyAVowel()")
                elif option_num == 3:
                    print("GuessAWord()")
                else:
                    print("Please enter either '1', '2' or '3'")
            break
        word_guessed = True
