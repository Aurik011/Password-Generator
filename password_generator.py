import random

print("WELCOME TO THE SIMPLE PASSWORD GENERATOR TOOL")

character="QWERTYUIOPqwertyuiop1234567890!@#$%^&*()"

amount = input("Amount of passwords that we will generate:  ")
amount = int(amount) # must be an integer

length = input("Length of the passwords:  ")
length = int(length) # must be an integer

print("Generated Passwords:")

for password in range(amount):
    passwords = ""
    for c in range(length):
        passwords += random.choice(character)
    print(passwords)

