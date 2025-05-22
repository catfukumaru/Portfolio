import sys

intro_text = """Collatz Sequence, by Al Sweigart al@inventwithpython.com
2. Generates numbers for the Collatz sequence, given a starting number.
3. More info at: https://en.wikipedia.org/wiki/Collatz_conjecture
4. View this code at https://nostarch.com/big-book-small-python-projects
5. Tags: tiny, beginner, math"""

print(intro_text + "\n")
n = 0
while True:
    n = input("Enter a starting number (greater than 0) or QUIT:\n> ")
    if n == "QUIT":
        print("program has ended")
        sys.exit()
    if n.isdecimal():
        n = int(n)
        break

sequence = [n]
while n>0:
    if n %2 == 0: # correct
        n = int(n / 2)
        sequence.append(n)
        if n == 1:
            break
    if n %2 != 0: # correct
        n = n * 3 + 1
        sequence.append(n)

for i in range(len(sequence)):
    if i == len(sequence)-1: # this is the last index
        print(f"{sequence[i]} ")
    else:
        print(f"{sequence[i]}, ", end=" ")