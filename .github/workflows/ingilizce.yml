import random
import string

def generate_password(length=16, use_uppercase=True, use_numbers=True, use_symbols=True):
    """
    Function to generate a random password.
    :param length: Length of the password (default 16)
    :param use_uppercase: Include uppercase letters? (default True)
    :param use_numbers: Include numbers? (default True)
    :param use_symbols: Include symbols? (default True)
    :return: A randomly generated password.
    """
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if len(characters) == 0:
        raise ValueError("You must select at least one character type!")
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the length of your password (default 16): ") or 16)
        use_uppercase = input("Include uppercase letters? (Y/n): ").strip().lower() != 'n'
        use_numbers = input("Include numbers? (Y/n): ").strip().lower() != 'n'
        use_symbols = input("Include symbols? (Y/n): ").strip().lower() != 'n'
        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
