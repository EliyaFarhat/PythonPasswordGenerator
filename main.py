# Name: Eliya Farhat
# ID: 501164593

"""
Problem: Make a program that outputs a randomly generated password containing a mix of letters, numbers, and/or special
characters, the length of the password, and the chance of guessing the password (1/n).
Ask the user to input a password length, the length should be greater than 8 characters and less than
16 characters. The user should also be able to generate a password of only letters if they wish to do so.
If the first character of the password happens to be a lower case 'a', 'b', 'c', 's' or 'q', swap it with
the last character in the password and print 'Swapped!'. Finally, output the password, the length, and the chance
of guessing this password (1/n).
"""

# Random module allows for the use of the random.choice() function, this is what we will use to select a random char.
import random

# Defines a string of letters, numbers, and special characters that we will select randomly for the password.
# A list would also work.
# There are a total of 72 choices, this comes to use for the probability.
character_choices = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*_+'
# Defines a string of only letters, for the letters only passwords.
# 52 total choices.
only_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


# Function for generating a password, this function has a parameter of length, which takes the value the user selected.
def generate_password(length, type):
    # Initialize the string the password will be generated to.
    # We want it to be empty since we want it to be randomly generated.
    password = ""

    # Recall, type == 2 means that the password is mixed.
    if type == 2:
        # This for loop runs for the length the user selected.
        for x in range(length):
            # Each iteration adds a random character from character_choices using the random.choice() function.
            password += random.choice(character_choices)
    # Recall, type == 1 means that the password is made only of letters.
    if type == 1:
        # This for loop runs for the length the user selected.
        for i in range(length):
            # Each iteration adds a random character from character_choices using the random.choice() function.
            password += random.choice(only_letters)
    # This conditional statement checks if the char at index 0(first char of password) is an a,b,c,s or q.
    if password[0] == "s" or password[0] == "q" or password[0] == "a" or password[0] == "b" or password[0] == "c":
        # Since string are immutable, we can't directly change the chars in the string password.
        # So, we must convert the string into a list using the list() function.
        swap = list(password)
        # Swap the char at index 0 with the char at index -1, which is the last index.
        swap[0], swap[-1] = swap[-1], swap[0]
        # Once the list is successfully swapped, use the join() function to convert the list back to a string.
        password = ''.join(swap)
        # Now we can print that the string has been swapped and print the new string.
        print("Swapped!")
        print("Password:", password)
        print("Length:", length)
    # If the password does not begin with an a,b,c,s or q, we can just print the password that was generated.
    else:
        print("Password:", password)
        print("Length:", length)


# Function to calculate the probability of guessing the password.
# Again, the parameter is the length of the password, as the probability is dependant on it.
def probability(length, type):
    # Since there are 72 choices for the mixed password, each char has a 1 in 72 chance of being selected.
    if type == 2:
        total_possible = 72 ** length
        print("There is a 1 in", total_possible, "chance of guessing this mixed password.")
    # Since there are 52 choices for the mixed password, each char has a 1 in 72 chance of being selected.
    if type == 1:
        total_possible = 52 ** length
        print("There is a 1 in", total_possible, "chance of guessing this only letter password.")


# This is the condition that determines whether the password will be generated or not.
# If the length is 9 - 15 digits (inclusive) long then the password will be generated.
def test_length(pass_length):
    if pass_length > 15 or pass_length < 9:
        return True
    else:
        return False


# Using a "while True" loop for a menu system allows for the program to loop forever until the user decides to exit.
# "Exiting" the loop will result in the program closing/ending.
while True:
    # Instructs the user on the program and how to exit it if needed.
    print("\nWelcome, would you like to generate a password?")
    # Allows and asks for the user input.
    choice = input("Enter a '1' to continue and a '2' to exit.")
    # The "choice" will be used for determining which conditional statement is used.

    # Making the choice into an int from a string allows the user to enter anything without having the program crash.
    # If choice was = int(input()), then anything except an int would crash the program.
    # If the user enters a '2', the while loop will end.
    if int(choice) == 2:
        print("Program closed.")
        # The while loop breaks using the loop control statement 'break'.
        # You could also set a condition to break and have the condition be met within this if statement.
        break
    # If the user enters a '1', the password will be generated if certain conditions are met.
    elif int(choice) == 1:
        # Informs the user of the password length condition.
        print("\nNote: The password must be greater than 8 characters and less than 16.")
        # Input for length of the password.
        pass_length = int(input("How long would you like the password to be?"))
        # Allows the user to generate a password with only letters.
        pass_type = int(input(("Enter a '1' for a password with only letters, and a '2' for a mixed password: ")))
        # Uses the truth value from the function test_length
        if test_length(pass_length):
            # The user is brought back to the start of the while loop if this condition is met.
            # No 'break' statement means that the while loop will continue to run.
            print("Invalid length, try again.")
        # If the length is within the specified range, call the function.
        else:
            # This function is responsible for generating the password and swapping the first char if needed.
            generate_password(pass_length, pass_type)
            # This function is responsible for calculating and printing the probability.
            probability(pass_length, pass_type)
    # If the user inputs a choice other than '1' or '2' they are brought back to the start of the while loop.
    else:
        print("Invalid choice, try again.")
