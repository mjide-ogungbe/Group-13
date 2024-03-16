import random

# Import the random module for generating random choices
user_name = input("Enter your name to begin: ")
print(f"Hello, {user_name}! Let's play Rock, Paper, Scissors.")

# List of options for the game
options = ["rock", "paper", "scissors"]

# Computer selects a random choice from the options
computer_choice = random.choice(options)

# User makes a choice
user_choice = input("Choose rock, paper, or scissors: ").lower()

# Validate user input
if user_choice not in options:
    print("Invalid choice. Please choose rock, paper, or scissors.")
else:
    # Compare choices to determine the winner
    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") \
        or (user_choice == "paper" and computer_choice == "rock") \
        or (user_choice == "scissors" and computer_choice == "paper"):
        print(f"{user_name} ({user_choice}) : Computer ({computer_choice}). You win!")
    else:
        print(f"{user_name} ({user_choice}) : Computer ({computer_choice}). Computer wins!")
        
