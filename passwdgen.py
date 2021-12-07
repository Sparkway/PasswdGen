import string
import random
import time
from colorama import Fore, Back, Style
import tkinter

def passwdgen():

    letters = list(string.ascii_letters)
    special = list('&#!?%$=+@')
    number = list(string.digits)
    characters = list(letters)

    # User Input
    # Length of the password
    try:
        length = int(input("Passwd length : " + Fore.BLUE))
    except:
        print("only numbers")
        exit()

    # Numbers or not
    number_choice = input(Style.RESET_ALL + "Numbers (y/n) : " + Fore.BLUE)
    if number_choice == 'y':
        characters += list(number)
    elif number_choice == 'n':
        pass
    else:
        print("y/n only")
        exit()

    # Special charaters or not
    special_choice = input(Style.RESET_ALL + "Special characters (y/n) : " + Fore.BLUE)
    if special_choice == 'y':
        characters += list(special)
    elif special_choice == 'n':
        pass
    else:
        print("y/n only")
        exit()

    print(Style.RESET_ALL + "\nPassword is being generated")
    progression = "=====================>"
    for char in progression:
        print(Fore.RED + char, end="" + Style.RESET_ALL)
        time.sleep(0.05)
        
    print("\nHere's your password : ")

    # Generating the password
    random.shuffle(characters)
    password = []

    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)
    print(Fore.GREEN + "".join(password) + Style.RESET_ALL)

passwdgen()