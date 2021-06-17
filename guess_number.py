import random

def guess():
    high = x = int(input("Which should be the maximum number? "))
    random_number = random.randint(1,high)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        #print (guess)
        if (guess) < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    print(f'Yup! You won! My number was {random_number}!')
    
def computer_guess():
    low = 1
    high = int(input("Which should be the maximum number? "))
    #wrong = 0
    feedback = ''
    guesslist = [0]
    guess = 0
    while feedback != 'c':
        if high < low:
            print("I think that you gave me wrong suggestions, let's try again.")
            #wrong = 1
            break
        else:
            #print(f'DEBUG: Entro nel while, low:{low}, high:{high}, guess:{guess}, guesslist:{guesslist}') #debug
            guess = random.randint(low, high)
            while guess not in guesslist:
                feedback = input(f'I was thinking about {guess}. Is it too high (H), to low (L), or correct (C)?').lower()
                guesslist.append(guess)
                #print(f'DEBUG: low:{low}, high:{high}, guess:{guess}, guesslist:{guesslist}') #debug
        if feedback == 'h':
            high = guess
            #print(f'DEBUG: Entro nel H, low:{low}, high:{high}, guess:{guess}, guesslist:{guesslist}') #debug
        elif feedback == 'l':
            low = guess
            #print(f'DEBUG: Entro nel L, low:{low}, high:{high}, guess:{guess}, guesslist:{guesslist}') #debug
    #print(f'DEBUG: Entro nel guess = low = high, low:{low}, high:{high}, guess:{guess}, guesslist:{guesslist}') #debug
    print(f"I guessed your number. It's {guess}!")

while True:
    game = input("Which game you want to play? (C)omputer guesses a number or (Y)ou guess a number? ").lower()
    if game == 'c':
        computer_guess()
    elif game == 'y':
        guess()
    else:
        print ("Well, ok then, see you next time!")
        exit
    