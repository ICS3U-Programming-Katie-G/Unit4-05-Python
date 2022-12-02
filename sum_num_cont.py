#!/usr/bin/env python3
# Created by: Katie G
# Created on: November 30th, 2022
# This program gets the number of terms the user
# would like to add up, then uses a while... loop to get the
# user number, check if it is valid input, then
# adds the number to the sum until the program has added
# the number of terms the user wanted. The sum,
# placed inside a working string, will be
# displayed back to the user along with all the numbers
# the user inputted to be added, so that the user
# can see all of the numbers they entered to be added along
# with the final output. If invalid information is entered
# during the loop for the user number, the program uses a
# continue statement to skip this iteration of the loop.


# this function will get the number of terms from
# the user, then uses a while... loop to add them up
# until the number of terms has been reached,
# then the function displays the sum back to the user,
# complete with error checking.
def main():
    # initializing the counter, sum string and and sum variables.
    counter = 0
    sum_string = "The product of "
    sum = 0

    # getting the user number of numbers they want to add.
    user_number_of_numbers = input("Hello! How many numbers would you like to add? ")

    # try...catch statement to catch invalid input
    try:
        user_number_of_numbers_int = int(user_number_of_numbers)
        # checking to see if the input is positive - cannot add negative
        # or 0 numbers together.
        if user_number_of_numbers_int > 0:
            # while... loop to add specified number of
            # numbers together.
            while counter < user_number_of_numbers_int:
                user_number = input(
                    "Please enter a number you’d like to add to the sum: "
                )
                # try...catch to ensure valid input
                try:
                    user_number_int = int(user_number)
                    sum = sum + user_number_int
                    counter = counter + 1
                    sum_string = sum_string + user_number + " + "
                    # checking to see if the counter has reached desired
                    # number.
                    if counter == user_number_of_numbers_int:
                        break
                except Exception:
                    print("Please enter a valid integer!")
                    continue
        else:
            print("Please enter a valid, positive integer!")
    except Exception:
        print("Please enter a valid, positive integer!")
    finally:
        sum_string = sum_string + " 0 = {}".format(sum)
        print("{}".format(sum_string))
        print("Thank you for using this program!")


if __name__ == "__main__":
    main()
