#Rock,scissors,paper game
import random

def get_user_choice():
    """Get and validate user's choice."""
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid choice! Please enter rock, paper, or scissors.")

def get_computer_choice():
    """Generate computer's random choice."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on game rules."""
    if user_choice == computer_choice:
        return "It's a tie!"
    
    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if winning_combinations[user_choice] == computer_choice:
        return "You win!"
    return "Computer wins!"

def play_game():
    """Main game function."""
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter 'q' to quit the game.")
    
    user_score = 0
    computer_score = 0
    
    while True:
        # Check if user wants to quit
        user_input = input("\nPress Enter to play or 'q' to quit: ").lower()
        if user_input == 'q':
            print(f"\nFinal Score - You: {user_score}, Computer: {computer_score}")
            print("Thanks for playing!")
            break
            
        # Get choices
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        # Display choices
        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        
        # Determine and display result
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
            
        print(f"Score - You: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    play_game()
