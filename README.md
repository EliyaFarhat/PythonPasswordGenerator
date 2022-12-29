# PythonPasswordGenerator
A random password generator that using parameters.
## The Code
### Before We Begin

A lot of websites today require a password that has the following: 8 < characters < 16, a capital letter, numbers, and a special character. To be able to make the most out of this program we are going to handle cases where some or all of these parameters are required and generate the passwords accordingly. We will also be utilising a menu system to allow the user to continue to generate passwords until they are satisfied.

Note: The output will be displayed in the terminal, the GUI version is still under construction.

### Part 1: General Setup and Creating the Menu
The first thing we need to add to the program is the **random** module. We can then create two strings that will serve as the possible characters we are able to select.
```python
# Random module allows for the use of the random.choice() function, this is what we will use to select a random char.
import random

# Defines a string of letters, numbers, and special characters that we will select randomly for the password.
# A list would also work.
# There are a total of 72 choices, this comes to use for the probability.
character_choices = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*_+'
# Defines a string of only letters, for the letters only passwords.
# 52 total choices.
only_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
```
A good way to create a functioning menu is to implement a "while True" loop that with conditional statements that are activated with inputs. We will gather one input, but offer two choices. We will ask the user whether they want to generate a password or exit the program using the "break" method.

If the user decides to generate a password, we will ask them whether they want a password with only letters or a mixed password. We will then ask them for the desired length, remembering that they may only generate a password 9 - 15 characters long (inclusive).

```python
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
        if pass_length > 15 or pass_length < 9:
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
```

### Part 2: Creating the Functions
You may have noticed that the code above containe some functions we have not yet defined. Let's fix this.

Let's start with generating the password. This function will take in the two parameters we asked for earlier, the length and type of password. We can generate the password by selecting a random index from the string and appending it to an empty string. We will then finish by printing the new password and length.

```python
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
    print("Password:", password)
    print("Length:", length)
```
Let's define a function that prints the probability of guessing the password. The statistical calculations are self-explanatory so the method will not be explained here.

```python
def probability(length, type):
    # Since there are 72 choices for the mixed password, each char has a 1 in 72 chance of being selected.
    if type == 2:
        total_possible = 72 ** length
        print("There is a 1 in", total_possible, "chance of guessing this mixed password.")
    # Since there are 52 choices for the mixed password, each char has a 1 in 72 chance of being selected.
    if type == 1:
        total_possible = 52 ** length
        print("There is a 1 in", total_possible, "chance of guessing this only letter password.")
```

### The End
Congratulations on making the program! A simple GUI tutorial using tkinter will be uploaded in the future using this same code.

