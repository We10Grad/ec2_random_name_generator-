
department = input("Enter the department name \n")

instance_number = input("Enter the number of instances to create \n")

import random
import string

# Define the pool of characters to choose from (letters and digits)
characters = string.ascii_letters + string.digits

# Define the desired length of the random string
random_string_length = 4

# Generate the random string
random_variable = ''.join(random.choice(characters) for _ in range(random_string_length))



ec2_name = department + instance_number + random_variable

print(ec2_name)