# Step 1: Import the random module for generating random choices
import random

# Step 2: Greet the user and get their name
user_name = input("Enter your name to begin: ")
print(f"Hello, {user_name}! Let's play Rock, Paper, Scissors.")

# Step 3: The game loop - allows the user to play multiple rounds
while True:
    # List of options for the game
    options = ["rock", "paper", "scissors"]
    
    # Step 4: Computer selects a random choice from the options
    computer_choice = random.choice(options)
    
    # Step 5: User makes a choice
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    
    # Validate user input
    if user_choice not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    # Step 6: Compare choices to determine the winner
    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") \
        or (user_choice == "paper" and computer_choice == "rock") \
        or (user_choice == "scissors" and computer_choice == "paper"):
        print(f"{user_name} ({user_choice}) : Computer ({computer_choice}). You win!")
    else:
        print(f"{user_name} ({user_choice}) : Computer ({computer_choice}). Computer wins!")

    # Step 7: Ask the user if they want to play again
    play_again = input("Play again? (yes/no): ").lower()
    
    # Break the loop if the user doesn't want to play again
    if play_again != "yes":
        print("Thanks for playing!")
        break


