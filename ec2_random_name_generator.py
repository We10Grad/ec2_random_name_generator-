import random
import string

# Get department name from user
department = input("Enter the department name \n")

# Get number of instances from user
instance_number = input("Enter the number of instances to create \n")

# Check if the input is a valid number
if instance_number.isdigit():
    instance_number = int(instance_number)
else:
    print("Please enter a integer value \n")
    exit()

# Define the pool of characters to choose from (letters and digits)
characters = string.ascii_letters + string.digits

# Generate instance names
for x in range(instance_number):
    random_character = random.choice(characters)
    random_character = random_character + random.choice(characters) + random.choice(characters) + random.choice(characters)
    ec2_name = department + random_character
    print(ec2_name)

