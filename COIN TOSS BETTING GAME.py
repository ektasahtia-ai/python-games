import random

coins = 100

while coins > 0:
    print("Coins:", coins)

    guess = input("Heads or Tails? ")

    toss = random.choice(["heads", "tails"])

    if guess.lower() == toss:
        coins += 10
        print("You Won!")
    else:
        coins -= 10
        print("You Lost!")

    print("Result:", toss)