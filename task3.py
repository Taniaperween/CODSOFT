import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters for good strength.")
        return ""

    # Define possible characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Ask user for password length
try:
    user_length = int(input("Enter desired password length: "))
    password = generate_password(user_length)
    if password:
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")





