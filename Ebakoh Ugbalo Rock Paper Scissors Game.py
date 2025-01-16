import random

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    """Main function to run the Rock, Paper, Scissors game."""
    choices = ["rock", "paper", "scissors"]
    
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'quit' to exit the game.")

    while True:
        # Get the user's choice
        user_choice = input("Your choice: ").lower()
        
        if user_choice == "quit":
            print("Thanks for playing! Goodbye!")
            break
        elif user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        # Generate a random choice for the computer
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        # Determine and display the winner
        result = determine_winner(user_choice, computer_choice)
        print(result)
        print()

if __name__ == "__main__":
    main()
