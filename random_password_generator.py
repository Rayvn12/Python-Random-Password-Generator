# Create a program that generates a random password based on user perference 
# for length and character types (letters, numbers, and symbols)

# Password rules:
# 1. The password must be at least 4 characters long.
# 2. The password must include letters, numbers, and symbols based on user preference.

import random

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    if length <= 0:
        return "Length must be a positive integer."
    elif length < 4:
        return "Length must be at least 4 to include all character types."
    elif not (use_letters or use_numbers or use_symbols):
        return "At least one character type must be selected."
    else:
        characters = ''
        if use_letters:
            characters += 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if use_numbers:
            characters += '0123456789'
        if use_symbols:
            characters += '!@#$%^&*()-_=+[]{}|;:,.<>?'

        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    
def main():
    print("Welcome to the Random Password Generator!")
    try:
        # Get user input for password length and character types
        length = int(input("Enter the desired password length (minimum 4): "))
        # Get user preferences for character types
        use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        # Include numbers? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        # Include symbols? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
# This code generates a random password based on user preferences for length and character types.
