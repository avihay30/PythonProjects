def deleting_leftest_number(number):
    """ Function deleting_leftest_number gets a number
        and return a string of that number without the leftest digit.
    """
    return str(number)[1:]


def get_leftest_digit(number):
    """ Function get_leftest_digit gets a number
        and return the leftest digit of that number.
    """
    return int(str(number)[0])


def concatenate_unit_digit_to_number(number, digit):
    """ Function concatenate_unit_digit_to_number gets a number and a digit
        and return a the number with the digit in its units.
    """
    return int(str(number) + str(digit))


def left_circular_shift(list):
    """ Function left_circular_shift gets a list of integers
        and returns a left circular shift list.
    """
    # declaring an empty list, that will contain the shifted list.
    shifted_list = []
    # declaring a variable named "leftest_of_first_element"
    # that will contain the leftest digit of the element in index 0 in the list.
    leftest_of_first_element = 0
    # running in a loop length of "list" times.
    for i in range(len(list)):
        # calculating and saving in a variable the leftest digit of the list[i].
        leftest_digit = get_leftest_digit(list[i])
        # if its the first iteration.
        if i == 0:
            # saving the leftest digit of the first number for later on.
            leftest_of_first_element = leftest_digit
        else:
            # changing the element in place of i - 1
            # in the list to be 
            # shifted(leftest of list[i] to be digits of list[i-1]),
            # by calling the function "concatenate_unit_digit_to_number".
            shifted_list[i - 1] = concatenate_unit_digit_to_number(
                shifted_list[i - 1], leftest_digit)
        # deleting the leftest digit in the number list[i] 
        # in order to complete the left circular shift of that cell in the list.
        shifted_element = deleting_leftest_number(list[i])
        # appending to the list the complete shifted element.
        shifted_list.append(shifted_element)
    # dealing with the first cell that needs to add
    # its leftest digit to the last cell to his units.
    shifted_list[-1] = concatenate_unit_digit_to_number(
        shifted_list[-1], leftest_of_first_element)

    # returning the complete shifted_list.
    return shifted_list


# gets an input from the user of number of element.
number = int(input("Enter number of elements: "))
# declaring an empty list named "original_array".
original_array = []
# running in a loop "number" time.
for i in range(number):
    # every iterating getting an input
    # from the user about a element to add to the empty list.
    original_array.append(int(input("Enter element %s: " % i)))

# printing both lists, original and shifted.
print("\nOriginal array: \n%s" % original_array)
print("\nShifted array: \n%s" % left_circular_shift(original_array))
