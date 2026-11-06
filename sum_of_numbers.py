#!/usr/bin/env python3
# Created By: Bryson Grant
# Date: 11 06, 2026
# This program adds all the numbers from 0 to the number inputted by the user


def main():
    # Get number from user
    user_number = input("Enter a number: ")
    # See if order inputted is a string
    try:
        user_number_int = int(user_number)
    except ValueError:
        print("{} is not a valid number".format(user_number))
    if user_number_int < 0:
        print("{} is not a valid number".format(user_number))
    # Initialize sum variable
    sum_of_numbers = 0
    counter = 0
    # Add all numbers from 1 to the number inputted by the user
    while counter <= user_number_int:
        print("Tracking {} times through the loop".format(counter))
        sum_of_numbers = sum_of_numbers + counter
        counter = counter + 1
    # Display sum of numbers to user
    print(
        "The sum of all numbers from 0 to {} is {}".format(
            user_number_int, sum_of_numbers
        )
    )


if __name__ == "__main__":
    main()
