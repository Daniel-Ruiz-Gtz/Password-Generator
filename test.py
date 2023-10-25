import random
import string

def generate_secure_password(input_string):
    # Define possible characters for the password
    special_characters = string.punctuation
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    
    # Calculate the length of the secure password
    password_length = max(12, len(input_string))
    
    # Assign weights to character groups
    num_special_characters = 2
    num_lowercase_letters = 2
    num_uppercase_letters = 2
    num_digits = password_length - num_special_characters - num_lowercase_letters - num_uppercase_letters
    
    # Generate the secure password
    password = input_string  # Include the input string as part of the password
    password += ''.join(random.choice(special_characters) for _ in range(password_length - len(input_string)))
    
    return password

# Example of usage
input_string = "Danielq.1"
secure_password = generate_secure_password(input_string)
print(secure_password)
