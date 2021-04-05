from random import shuffle
def shuffle_list(my_list):
    shuffle(my_list)
    return (my_list)
my_list=['','O','']

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("pick a number:0,1 or 2")
    return int(guess)


def check_guess(my_list,guess):
    if my_list[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(my_list)
#initiallist
my_list=['','O','']

#shufflelist
mixedup_list = shuffle_list(my_list)

#userlist
guess=player_guess()

 #checklist
check_guess(mixedup_list,guess)