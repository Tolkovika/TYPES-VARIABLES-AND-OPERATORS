import random

computer = random.randint(1, 6)
you = int(input("Guess the dice roll (1 to 6): "))

print(f"Computer rolled: {computer}")
print(f"You won: {you == computer}")
