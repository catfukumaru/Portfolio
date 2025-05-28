chances = 10
import random
answer = random.randint(1,100)
print(f"""I am thinking of a number between 1 and 100.
You have {chances} guesses left. Take a guess.""")
got_correct = False
while chances > 0:
    print("> ", end = '')
    guess = int(input())
    chances -= 1
    if answer== guess:
        got_correct = True
        print("Yay! You guessed my number!")
        break
    elif guess > answer:
        print(f"""Your guess is too high.
You have {chances} guesses left. Take a guess.""")
    elif guess < answer:
        print(f"""Your guess is too low.
    You have {chances} guesses left. Take a guess.""")

if got_correct == False:
    print(f"\n\nThe right answer is {answer}")