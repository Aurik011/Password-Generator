import random

print("WELCOME TO THE SIMPLE PASSWORD GENERATOR TOOL")

character="QWERTYUIOPqwertyuiopASDFGHJKLasdfghjklZXCVBNMzxcvbnm1234567890!@#$%^&*()"
# SYMBOLS AND NUMBERS ONLY PASSWORDS 1234567890!@#$%^&*()
# ALPHABETS ONLY PASSWORDS QWERTYUIOP qwertyuiopASDFGHJKLasdfghjklZXCVBNMzxcvbnm

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

prompt = input("Do you want to generate character only passwords? ") # prompt for more
if prompt.lower() != "yes":
    quit() # quits the program

character="QWERTYUIOPqwertyuiop"

print("Okay, Generating passwords for the second time: ")
print("Character only passwords: ")

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

prompt = input("Do you want to number and symbols only passwords? ") # prompt for more
if prompt.lower() != "yes":
    quit() # quits the program

character="1234567890!@#$%^&*()"

print("Okay, Generating passwords for the second time: ")
print("Numbers and Symbols only passwords: ")

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
