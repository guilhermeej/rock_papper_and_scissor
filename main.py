# imports
from random import randint
from time import sleep

# header

print('='*28)
print('THE RULES OF THIS GAME:')
print('Rock beats scissors (crushing or breaking them).\nScissors beats paper (cutting it).\nPaper beats rock (wrapping it).\nPRESS [4] TO QUIT')
print('='*28)



draw = 0 # Value is incremented if draw in the round
player_score = 0 # Value is incremented if player wins the round
machine_score = 0 # Value is incremented if machine wins the round
while True:
    player_choice = int(input('[1] Rock\n[2] Papper\n[3] Scissors\nType your choice... ')) # requesting player option
    
    while player_choice < 1 or player_choice > 4: # preventing bugs with a while loop
        player_choice = int(input('[1] Rock\n[2] Papper\n[3] Scissors\nType your choice... '))
    machine_choice = randint(1,3) # randomic choice of machine, this value is changed in every round

    # applying the game rule
        
    if player_choice == machine_choice:
        draw += 1
        print('Draw! The choices are the same\n')
    elif (player_choice == 1 and machine_choice == 2) or (player_choice == 2 and machine_choice == 3) or (player_choice == 3 and machine_choice == 1):
        machine_score += 1
        print('You lost this round...\nTry again!')
    else:
        player_score += 1
        print('You won this round, keep it up!')
    if player_choice == 4: # quit option
        print(f'Player score = {player_score}\nMachine score = {machine_score}\nDraws = {draw}\nThanks for using my program! ass: @machine.gui')
        break
    
