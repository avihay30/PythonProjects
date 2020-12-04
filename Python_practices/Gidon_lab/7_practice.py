import math


def is_number_has_different_digits(num):
    """ Function is_number_has_different_digits receives a natural number,
        and return boolean value if the number has a repeated digits.
    """
    # calculating the number of digits in the received number.
    number_of_digits = int(math.log10(num)) + 1
    # iterating over each digit an checking if it is 
    # equal to the other digits in the number.
    for i in range(number_of_digits):
        for j in range(number_of_digits):
            # excluding the case that i == j because they are
            # representing the same digit.
            if i != j:
                if str(num)[i] == str(num)[j]:
                    return False
    return True


def is_pairs_are_not_consecutive_numbers(num):
    """ Function is_pairs_are_not_consecutive_numbers receives a
        natural number, and return boolean value if every pair of digits are
        not consecutive numbers 
    """
    digit = num % 10
    while num >= 10:
        num //= 10
        next_digit = num % 10
        # checking if the pair is consecutive numbers.
        if abs(digit - next_digit) == 1:
            return False
        digit = next_digit
    return True


# getting an input from the user.
number = int(input("Enter positive integer (no less than 2 digits): "))

# checking if the number is not well mixed number or has less than 2 digit
# or negative and printing the appropriate output to the user.
if number <= 12:
    if number < 10:
        print("The number must be positive and have at least 2 digits")
    else:
        print(number, "is NOT well-mixed number")
# checking if the number is above the maximum possible well mixed number.
elif number > 9753186420:
    print(number, "is NOT well-mixed number")
else:
    # checking if both function returns true according to received number
    # and printing the result to the user.
    if is_pairs_are_not_consecutive_numbers(number) and \
            is_number_has_different_digits(number):
        print(number, "is well-mixed number")
    else:
        print(number, "is NOT well-mixed number")
