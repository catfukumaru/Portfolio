# a python ptoject
# A multiplayer game where players roll dice and accumulate scores.
import random 

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

# obtains the number of players
while True: 
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <=4:
            break
        else:
            print("must be between 2 and 4 players.")

    else:
        print("invalid, try again")


max_score = 10
player_scores= [0 for _ in range(players)] # adds a 0 to initialise the list.keeps the score of the players

while max(player_scores) < max_score: # simulates turns. breaks a player, could be more than one has a score above 50
    # it doesnt end unitl every player gets a turn so that it is fair. other wise the first player would be more likely to win
    # why it is fair. lets say that player 1 has the max score. but because the max value check in the players_score is done after the for loop is done complete all the other players have a chance at winnig too. other wise the first player would get 1 more turn compared to the others
    for player_idx in range(players): # controls the turn per player
        print("\nplayer", player_idx+1, "turn has begun")
        print("your ottal score is: ", player_scores[player_idx], "\n")
        current_score = 0

        while True: # turn ends when they get a one else they continue
            should_roll = input("would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done") # one is not added because it is the rule of the game that if 1 is gotten your turn ends and the score you have been acumulating is wiped out 
                current_score = 0
                break
            else:
                current_score +=value
                print("You rolled a", value)
            print("Your score is ", current_score )

        player_scores[player_idx] += current_score # adding the players score to their total score
        print("Your total score is ", player_scores[player_idx] )


# get the winnig players index
max_score = max(player_scores)
winnig_index = player_scores.index(max_score)
print("player number", winnig_index+1, "is the winner with a score of: ", max_score)