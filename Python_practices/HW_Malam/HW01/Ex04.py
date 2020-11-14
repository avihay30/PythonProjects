# Ex 04 - getting a positive integer number from the user, and splitting it
# into group of three digits(if possible) and dividing each digit by 3 and checking
# if all the three digits has different remainders.
# if so the program print's "OK", if not "ERROR"
import math

# getting a positive integer number from the user.
number = input("Insert number: ")
# calculating the number of digits in that number.
digits = int(math.log10(int(number)))+1

# printing "OK" if there is only 1 digit.
if digits == 1:
    print("OK")

# checking the possibility if the number has 2 digits.
elif digits == 2:
    # checking if they have different remainders and if so printing "OK".
    if int(number[0]) % 3 != int(number[1]) % 3:
        print("OK")
    # if they have the same remainder printing "ERROR"
    else:
        print("ERROR")

# we used else here for readability,
# it's not really necessary because if we put that "for" below
# above the first "if" it would work the same
else:
    # running over all the digits in the number
    # and checking each group of three digit separately.
    # we used "range(digits - 2)" because it's the last iteration we need to check.
    for i in range(digits - 2):
        # saving the remainders of each digit in a variable.
        first_digit_remainder = int(number[i]) % 3
        second_digit_remainder = int(number[i+1]) % 3
        third_digit_remainder = int(number[i+2]) % 3
        # checking if all the three digits have different remainders.
        if (first_digit_remainder != second_digit_remainder) and \
                (first_digit_remainder != third_digit_remainder) and \
                (second_digit_remainder != third_digit_remainder):
            # if true - skipping to the next iteration.
            continue
        # we used else here for readability, because we put "continue" in the above line,
        # we don't really need that "else", if the above "if" is true it will skip over it anyway.
        else:
            # printing "ERROR" if 2 or more digits have the same remainder.
            print("ERROR")
            # exiting the loop.
            break
    # printing "OK" if each digit in group of three in the whole number has different remainder.
    else:
        print("OK")
