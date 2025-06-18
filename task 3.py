#Number Guessing Game
import random

def number_guessing_game():
    # Generate random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        try:
            # Get user's guess
            guess = int(input("\nEnter your guess (1-100): "))
            attempts += 1
            
            # Validate input
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
                
            # Check guess and provide hints
            if guess == target_number:
                print(f"Congratulations! You've guessed the number {target_number} in {attempts} attempts!")
                break
            elif guess < target_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
                
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
if __name__ == "__main__":
    number_guessing_game()