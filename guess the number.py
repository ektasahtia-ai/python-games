import random

print("🎮 Welcome to Guess the Number Game!")

# Computer chooses random number
number = random.randint(1, 100)

attempts = 0

while True:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1

    if guess < number:
        print("📉 Too low! Try again.")

    elif guess > number:
        print("📈 Too high! Try again.")

    else:
        print("🎉 Correct! You guessed the number.")
        print("🏆 Total attempts:", attempts)
        break