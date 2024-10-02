# importing random, allow you to generate random numbers
import random

# defining the rolling function
def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value, max_value)
    return roll
#value=roll()
#print(value)

#setting the players, max 4, checking if it is valid number
while True:
    players=input('Enter the number of players (2-4): ')
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
           
            break
        else:
             print('Must be between 2 - 4 players')
    else:
        print('Invalid, try again')

#print (players)

max_score=50;
# putting 0 in every single player list that we have, can pui 'i' instead of '_' if you care, will get [0,0,...]
player_score=[0 for _ in range(players)]

# looping through the game
while max(player_score) < max_score:
    
    for player_idx in range(players):
        print('\nPlayer number2', player_idx + 1, 'turn just started!')
        print('your total score is: ', player_score[player_idx], '\n')
        current_score=0

        while True:
            should_roll=input('Would you like to roll (y)?')
            if should_roll.lower() != 'y':
                break

            value=roll()
            if value == 1:
                print(' you rolled 1! turn done!')
                current_score =0
                break
            else:
                current_score+=value
                print('You rolled: ', value)  
            print('your score is: ', current_score) 

        player_score[player_idx] += current_score
        print('Your total score is: ', player_score[player_idx])

max_score=max(player_score)
winning_idx=player_score.index(max_score)
print('Player number ', winning_idx+1, 'is the winner with a score of: ', max_score)