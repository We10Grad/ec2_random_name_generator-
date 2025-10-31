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
    print("Please enter a integer value")
    exit()

# Define the pool of characters to choose from (letters and digits)
characters = string.ascii_letters + string.digits

# Define the desired length of the random string
random_string_length = 4

# Generate instance names
for i in range(instance_number):
    # Start with an empty string
    random_variable = ""
    
    # Add 4 random characters one at a time
    for j in range(random_string_length):
        random_char = random.choice(characters)
        random_variable = random_variable + random_char
    
    # Create the EC2 name
    ec2_name = department + "-" + random_variable
    
    # Print the instance name
    print(ec2_name)