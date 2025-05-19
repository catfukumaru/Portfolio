# dealer function
# generate 2 random numbers
import random


def roll_die():
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    return dice_1,dice_2

def even_odd(die):
    dice_1, dice_2 = die
    if (dice_1 + dice_2) % 2 == 0:
        return True # the sum of the number are even
    return False

# player
def ask_parity(): # asks if the sum is odd or even
    string = """The dealer slams the cup on the floor, still covering the
dice and asks for your bet.
\n\tCHO (even) or HAN (odd)?"""
    print(string)
    guess = input("> ")
    return guess

def place_bet(starting_amount):
    print(f"You have {starting_amount:.0f} mon. How much do you bet? (or QUIT)")
    bet = input("> ")
    if bet.isdigit():
        return int(bet)
    if bet.isalpha():
        return bet



# bet
def calc_winning(amount, bet):
    winning = bet * 1.9
    winning -= 40  # this is the fee
    amount += winning
    return amount

def calc_losing(amount, bet):
    amount -= bet
    return amount

def game():
    introduction = """Cho-Han, by Al Sweigart al@inventwithpython.com. This is my attempt.\n
In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.\n"""
    print(introduction)
    bet = 0
    stop_game = ''
    initial_amount = 5000

    while  initial_amount > 0:

        bet = place_bet(initial_amount)
        if type(bet) == str:
           if bet.upper() == "QUIT":
               break

        print("The dealer swirls the cup and you hear the rattle of dice.")
        die = roll_die()
        actual_parity = even_odd(die)
        player_guess = ask_parity()


        dice1, dice2 = die

        if actual_parity == True and player_guess.lower() == 'cho': #winning # the issue was that i forgot the brackets in .lower()
            win_lose_text = f"""{'GO' if dice1%2==0 else 'HAN'} - {'GO' if dice2%2==0 else 'HAN'}
            {dice1} - {dice2}
            You won! You take {float(bet) * 1.9:.0f} mon.
            The house collects a 40 mon fee.""" # :.0f for no decimal places
            print(win_lose_text)
            initial_amount = calc_winning(initial_amount, bet)

        if actual_parity == False and player_guess.lower() == "cho":   #losing
            win_lose_text = f"""{'GO' if dice1%2==0 else 'HAN'} - {'GO' if dice2%2==0 else 'HAN'}
            {dice1} - {dice2}
            You lose! You lose {bet} mon."""
            print(win_lose_text)
            initial_amount = calc_losing(initial_amount, bet)

        if actual_parity == False and player_guess.lower() == "han": #winning
            win_lose_text = f"""{'GO' if dice1%2==0 else 'HAN'} - {'GO' if dice2%2==0 else 'HAN'}
            {dice1} - {dice2}
            You won! You take {float(bet) * 1.9:.0f} mon.
            The house collects a 40 mon fee.""" # :.0f for no decimal places
            print(win_lose_text)
            initial_amount = calc_winning(initial_amount, bet)

        if actual_parity == True and player_guess.lower() == "han":   #losing
            win_lose_text = f"""{'GO' if dice1%2==0 else 'HAN'} - {'GO' if dice2%2==0 else 'HAN'}
            {dice1} - {dice2}
            You lose! You lose {bet} mon."""
            print(win_lose_text)
            initial_amount = calc_losing(initial_amount, bet)

    print("You have no money left. The game has ended.")

if __name__ == "__main__":
    game()











