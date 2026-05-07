# Stone Paper Scissors Game in Python

import random

# Choices list
choices = ["stone", "paper", "scissors"]

# Scores
user_score = 0
computer_score = 0

print("🎮 Welcome to Stone Paper Scissors Game!")

while True:
    print("\nChoose one:")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissors")

    user_choice = input("Enter your choice: ").lower()

    # Handle number input
    if user_choice == "1":
        user_choice = "stone"
    elif user_choice == "2":
        user_choice = "paper"
    elif user_choice == "3":
        user_choice = "scissors"

    # Validate input
    if user_choice not in choices:
        print("❌ Invalid choice! Try again.")
        continue

    # Computer choice
    computer_choice = random.choice(choices)

    print(f"\n🧑 You chose: {user_choice}")
    print(f"💻 Computer chose: {computer_choice}")

    # Game logic
    if user_choice == computer_choice:
        print("🤝 It's a tie!")

    elif (
        (user_choice == "stone" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "stone") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 You win this round!")
        user_score += 1

    else:
        print("😢 Computer wins this round!")
        computer_score += 1

    # Display scores
    print(f"\n📊 Score:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")

    # Play again option
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\n👋 Thanks for playing!")
        break