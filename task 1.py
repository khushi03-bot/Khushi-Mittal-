#Random Password Generator
import random
import string
def get_user_input():
    """Get password length and character type preferences from the user."""
    try:
        length = int(input("Enter the desired password length (minimum 8): "))
        if length < 8:
            print("Password length must be at least 8 characters. Setting to 8.")
            length = 8
    except ValueError:
        print("Invalid input. Setting password length to 8.")
        length = 8

    print("\nSelect character types to include (Y/N):")
    use_uppercase = input("Include uppercase letters? (Y/N): ").strip().upper() == 'Y'
    use_lowercase = input("Include lowercase letters? (Y/N): ").strip().upper() == 'Y'
    use_numbers = input("Include numbers? (Y/N): ").strip().upper() == 'Y'
    use_special = input("Include special characters? (Y/N): ").strip().upper() == 'Y'

    # Ensure at least one character type is selected
    if not (use_uppercase or use_lowercase or use_numbers or use_special):
        print("At least one character type must be selected. Enabling all types.")
        use_uppercase = use_lowercase = use_numbers = use_special = True

    return length, use_uppercase, use_lowercase, use_numbers, use_special

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    """Generate a random password based on user criteria."""
    # Define character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    special = string.punctuation

    # Build the character pool based on user selections
    char_pool = ''
    guaranteed_chars = []

    if use_uppercase:
        char_pool += uppercase
        guaranteed_chars.append(random.choice(uppercase))
    if use_lowercase:
        char_pool += lowercase
        guaranteed_chars.append(random.choice(lowercase))
    if use_numbers:
        char_pool += numbers
        guaranteed_chars.append(random.choice(numbers))
    if use_special:
        char_pool += special
        guaranteed_chars.append(random.choice(special))

    # Calculate remaining length after including guaranteed characters
    remaining_length = length - len(guaranteed_chars)
    if remaining_length < 0:
        print("Password length too short for selected character types. Adjusting length.")
        length = len(guaranteed_chars)
        remaining_length = 0

    # Generate the rest of the password
    password = guaranteed_chars
    for _ in range(remaining_length):
        password.append(random.choice(char_pool))

    # Shuffle the password to randomize character positions
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Random Password Generator")
    print("------------------------")
    
    # Get user input
    length, use_uppercase, use_lowercase, use_numbers, use_special = get_user_input()
    
    # Generate and display the password
    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
    print("\nGenerated Password:", password)

    # Basic password strength feedback
    print("\nPassword Strength:")
    if len(password) >= 12 and use_uppercase and use_lowercase and use_numbers and use_special:
        print("Strong: Password is long and includes all character types.")
    elif len(password) >= 8:
        print("Moderate: Password meets minimum length but could include more character types.")
    else:
        print("Weak: Consider increasing length or including more character types.")

if __name__ == "__main__":
    main()