import math


def deleting_leftest_number(number, number_of_digits):
    module_divider = int("1" + "0"*(number_of_digits - 1))
    return number % module_divider


def get_leftest_digit(number, number_of_digits):
    divider = int("1" + "0"*(number_of_digits - 1))
    return number // divider


def add_unit_digit_to_number(number, digit):
    return int(str(number)+str(digit))


def left_circular_shift(list):
    shifted_list = []
    leftest_of_first_element = 0
    for i in range(len(list)):
        number_of_digits = int(math.log10(list[i])) + 1
        leftest_digit = get_leftest_digit(list[i], number_of_digits)
        if i == 0:
            leftest_of_first_element = leftest_digit
        if i != 0:
            shifted_list[i - 1] = add_unit_digit_to_number(shifted_list[i - 1], leftest_digit)
        shifted_element = deleting_leftest_number(list[i], number_of_digits)
        shifted_list.insert(i, shifted_element)
    shifted_list[-1] = add_unit_digit_to_number(shifted_list[-1], leftest_of_first_element)
    return shifted_list


number = int(input("Enter number of elements: "))
original_array = []
for i in range(number):
    original_array.append(int(input("Enter element %s: " % i)))

print("Original array: \n%s" % original_array)
print("Shifted array: \n%s" % left_circular_shift(original_array))

