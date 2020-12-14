#!/usr/bin/env python3

# Created by Sean McLeod
# Created on December 2020
# This program is the number guessing game

import random


def main():
    # this function can tell the user if the number they guessed is correct

    # process
    random_number = random.randint(0, 9)  # a number between 0 and 9

    # process & output
    while True:
        # input
        guessed_string = input("Guess a number between 0 to 9: ")

        try:
            guessed_number = int(guessed_string)

            if guessed_number >= 0 and guessed_number <= 9:
                if guessed_number == random_number:
                    print("You are correct!!")
                    break
                elif guessed_number > random_number:
                    print("Try smaller!", "\n")
                else:
                    print("Try larger!", "\n")
            else:
                print("Please enter a positive integer between 0 and 9", "\n")

        except Exception:
            print("This is not an integer", "\n")


if __name__ == "__main__":
    main()
