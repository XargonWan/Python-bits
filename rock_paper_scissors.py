import random

user = 'a'

def play():
    global user
    user = input("What's your choice? (R)ock, (P)aper or (S)scissors? Or s(T)op playing: ")
    if user == 't':
        return 'Ok, see you next time!'

    computer = random.choice(['r', 'p', 's'])
    if computer == 'r':
        print("Jian, ken, pon!. I choose Rock.")
    elif computer == 'p':
        print("Jian, ken, pon! I choose Paper.")
    elif computer == 's':
        print("Jian, ken, pon! I choose Scissors.")
    
    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'
        
    
def is_win(player, opponent):
    # return true if the player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
    or (player == 'p' and opponent == 'r'):
        return True

while user != 't':
    print (play())