import random
import string

def generate_random_string(length):
    """Generate a random string of letters and numbers"""
    # Define the pool of characters to choose from
    characters = string.ascii_letters + string.digits
    
    # Start with an empty string
    random_variable = ""
    
    # Add random characters one at a time
    for i in range(length):
        random_char = random.choice(characters)
        random_variable = random_variable + random_char
    
    return random_variable