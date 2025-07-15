#Jeremy Durdel
#Chapter 12 Lab 2
#07/12/2025

import os
import sys

data_set = set()

print("Unique Word Counter")

def main():
    user_file = input("\nEnter the name of the file you wish to process: ")

    if not os.path.isfile(user_file):
        user_file = wrong(user_file)
    with open(f"{user_file}", mode='r') as file:
        readers = file.read()
    data = readers.split()
    data_set.update(data)

    print(len(data_set))


def wrong(user_file):
    valid = False
    while not valid:
        print(f"The file {user_file} could not be found!")
        user_file = input("Enter the name of the file you wish "
                     "to process or type exit to quit: ")
        if user_file == "exit":
            print("\nThanks for using the program!")
            sys.exit()
        elif os.path.isfile(user_file):
            valid = True
    return user_file


main()