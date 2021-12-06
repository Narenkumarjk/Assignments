#The familiar game of Rock, Paper, Scissors is played like this:
#at the same time, two players display one of three symbols:
#a rock, paper, or scissors.
#A rock beats scissors,
#scissors beat paper by cutting it, and paper beats rock by covering it.

import random

sys_list = ['Rock','Paper','Scissor']
sys_score =0
usr_score = 0

# Get user input for Best of 3 or Best of 5 games.
def get_usr_choice_for_no_of_games():
    try:
        var1 = int(input("Choose 3 to play best of '3 or 5 to play best of '5': "))
        if var1 not in (3 , 5):
            print("you input is Invalid enter correct choice 3 or 5: ")
            var1 = get_usr_choice_for_no_of_games()
    except ValueError:
        print ("you input is Invalid enter correct choice: ")
        var1=get_usr_choice_for_no_of_games()
    return var1

# Get user value.
def get_usr_input():
    usr_inp = input("please enter your choice 'Rock','Paper' or 'Scissor' :")
    if usr_inp not in sys_list:
        print("you input is Invalid enter correct choice 'Rock','Paper' or 'Scissor' :")
        usr_inp = get_usr_input()
    return usr_inp

# function for system to pick one random value from sys_list
def sys_random_pick():
    random_pick = random.sample(sys_list, 1)
    return random_pick

# tie breaker function invoked when user input and system input are same.
def tie_breaker():
    usr_input =''
    sys_input =''
    usr_input = get_usr_input()
    print('usr_input', usr_input)
    var2 = sys_random_pick()
    sys_input = str(var2[0])
    print('sys_input', sys_input)
    return usr_input,sys_input

# Validate the  User Input and system input and assign the score.
def validate_results(usr_inp, sys_inp,usr_score,sys_score):
    #print("inside Validate: ",usr_score,sys_score)
    tie_flg = 'N'
    if usr_input == 'Rock' and sys_inp == 'Scissor':
        usr_score = usr_score+1
    elif usr_input == 'Scissor' and sys_inp == 'Paper':
        usr_score = usr_score + 1
    elif usr_input == 'Paper' and sys_inp == 'Rock':
        usr_score = usr_score + 1
    elif usr_input == sys_inp:
        usr_score =usr_score
        sys_score =sys_score
        tie_flg = 'Y'
    else:
        sys_score = sys_score +1

    return  usr_score,sys_score,tie_flg


usr_choice = get_usr_choice_for_no_of_games()
print('User choose {} games' .format(usr_choice))

for i in range(usr_choice):
    usr_input = get_usr_input()
    print('usr_input', usr_input)
    var2 =  sys_random_pick()
    sys_inp = str(var2[0])
    print('sys_inp', sys_inp)
    usr_score, sys_score,tie_flg = validate_results(usr_input, sys_inp,usr_score,sys_score)
    while tie_flg =='Y':
        print("your answers are tied:")
        usr_input, sys_input = tie_breaker()
        if usr_input != sys_input:
            #print("After tie run", usr_score, sys_score, usr_input, sys_input)
            usr_score, sys_score, tie_flg = validate_results(usr_input, sys_input, usr_score, sys_score)
            tie_flg = 'N'
        #print("After tie validation", usr_score, sys_score)



print ('User Score is : {} and System Score is: {}' .format(usr_score,sys_score))

