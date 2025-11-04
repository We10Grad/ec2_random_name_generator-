import random
import string

# Create list of accepted departments
accepted_departments = ["marketing", "accounting","finops",]

# Display authorized departments to the user
print("Only these departments are authorized to use this program: Marketing, Accounting, and FinOps")

# Get department name from user
while True:
    # Prompt user to enter department name
    department = input("Enter the department name \n")
    # Convert input to lowercase for case-insensitive comparison
    department = department.lower() 
    # Check if department is in the accepted list
    if department.lower() in accepted_departments:
        # Exit loop if valid department
        break
    else:
        # Ask user to try again if invalid
        print("Please enter a valid department: \n")

# Get number of instances from user
while True:
    # Prompt user to enter number of instances
    instance_number = input("Enter the number of instances to create \n")
    # Check if input is a valid number
    if instance_number.isdigit():
        # Convert string to integer
        instance_number = int(instance_number)
        # Exit loop if valid number
        break
    else: 
        # Ask user to try again if invalid
        print("Please enter a integer value") 

# Define the pool of characters to choose from (letters and digits)
characters = string.ascii_letters + string.digits

# Generate instance names
for x in range(instance_number):
    # Pick first random character
    random_character = random.choice(characters)
    # Add three more random characters to make 4 total
    random_character = random_character + random.choice(characters) + random.choice(characters) + random.choice(characters)
    # Combine department name with random characters
    ec2_name = department + random_character
    # Print the generated EC2 instance name
    print(ec2_name)