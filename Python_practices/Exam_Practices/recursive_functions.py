def number_of_digits(number):
    if number < 10:
        return number
    return 1 + number_of_digits(number // 10)


# 1-
def sum_from_one_to_number(n):
    """ Function gets a number and returns the sum of 1 to that number
        (Ex. n = 3, returns 1+2+3=6)
    """
    if n == 1:
        return n
    return n + sum_from_one_to_number(n - 1)


# 2-
def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)


# 2 modified-
def multiply_digits(number):
    if number < 10:
        return number
    return number % 10 * multiply_digits(number // 10)


# 3-
def multiply_of_evens_to_number(n):
    """ Function gets a number and returns the multiply of all evens to that number
        (Ex. n = 6, returns 2*4*6=48)
    """
    if n <= 1:
        return 1
    if n % 2 == 0:
        return n * multiply_of_evens_to_number(n - 2)
    return multiply_of_evens_to_number(n - 1)


# 3 modified-
def multiply_even_digits(number):
    if number < 10 and (number % 10) % 2 == 0:
        return number
    # if last digit is even.
    if (number % 10) % 2 == 0:
        return number % 10 * multiply_even_digits(number // 10)
    return multiply_even_digits(number // 10)


# 4-
def multiply_of_non_divided_by_3_or_5_to_number(n):
    """ Function gets a number and returns the multiply of all non divided by 3 or 5
        to that number (Ex. n = 6, returns 1*2*4=8)
    """
    if n == 1:
        return n
    if not ((n % 10) % 5 == 0 or (n % 10) % 3 == 0):
        return n * multiply_of_non_divided_by_3_or_5_to_number(n - 1)
    return multiply_of_non_divided_by_3_or_5_to_number(n - 1)


# 4 modified-
def multiply_digits_non_divided_by_3_or_5(number):
    # if last digit is not divided by 3 or 5.
    if not ((number % 10) % 5 == 0 or (number % 10) % 3 == 0):
        if number > 10:
            return number % 10 * multiply_digits_non_divided_by_3_or_5(number // 10)
        return number
    if number < 10:
        return 1
    return multiply_digits_non_divided_by_3_or_5(number // 10)


# 5-
def average_of_one_to_number(n):
    # stupid af. (but required...)
    if n == 1:
        return 1
    return 0.5 + average_of_one_to_number(n - 1)


# 6-
def fibonacci_number(n):
    if n <= 2:
        return 1
    return fibonacci_number(n - 1) + fibonacci_number(n - 2)


# 7-
def fibonacci_number_iterative(n):
    first_number = 1
    second_number = 1
    # fibonacci starts with 1,1,2,3...(that why n-2)
    for i in range(n - 2):
        first_number, second_number = second_number, first_number + second_number

    return second_number


# 8-
def series_number_1(n):
    """ Function series_number_1 gets a n(location in the series),
        and returns the value in the series.
        series definition is G(1) = 1, G(2) = 2, G(n>2) = 2G(n-1)/G(n-2)
    """
    if n <= 2:
        return n
    # all natural n so using "//" in order to not get decimal
    return 2 * series_number_1(n - 1) // series_number_1(n - 2)


# 9-
def series_number_2(n):
    """ Function series_number_2 gets a n(location in the series),
        and returns the value in the series.
        series definition is H(1) = 1, H(2) = 2, H(3)=3, H(n>3) = (H(n-1)+H(n-2))/(2H(n-3))
    """
    if n <= 3:
        return n
    return (series_number_2(n - 1) + series_number_2(n - 2)) / (2 * series_number_2(n - 3))


# 10-
def series_number_3(n):
    """ Function series_number_3 gets a n(location in the series),
        and returns the value in the series.
        series definition is I(1) = 3, I(n>1) = Sqrt(2*I(n-1))
    """
    if n <= 1:
        return 3
    return (2 * series_number_3(n - 1)) ** 0.5


# 11-
def multiply_elements_in_list(integers_list):
    if len(integers_list) == 1:
        return integers_list[0]
    return integers_list[-1] * multiply_elements_in_list(integers_list[:-1])


# 12-
def max_number_in_list(integers_list):
    if len(integers_list) == 1:
        return integers_list[0]
    if integers_list[0] > integers_list[-1]:
        return max_number_in_list(integers_list[:-1])
    return max_number_in_list(integers_list[1:])


# 13-
def bubble_sort_smallest(integers_list, length):
    """ Function bubble_sort_smallest gets a list and it's length
        and returns a list that have smallest n in slot 0.
    """
    if length == 0:
        return integers_list
    if integers_list[0] > integers_list[length - 1]:
        integers_list[0], integers_list[length - 1] = integers_list[length - 1], integers_list[0]

    return bubble_sort_smallest(integers_list, length - 1)


# 13 extension-
def bubble_sort(integers_list):
    integers_list = bubble_sort_smallest(integers_list, len(integers_list))
    sorted_list = [integers_list[0]]
    for i in range(len(integers_list) - 1):
        integers_list = bubble_sort_smallest(integers_list[1:], len(integers_list[1:]))
        sorted_list.append(integers_list[0])
    return sorted_list


# 14-
def gcd(number1, number2):
    if number2 == 0:
        return number1
    return gcd(number2, number1 % number2)


# 15-
def max_multiply_in_lists(list1, list2):
    """ Function gets two equally sized list and returns the maximum multiplication
        of element on the same index
    """
    if len(list1) == 1:
        return list1[0] * list2[0]

    if list1[0] * list2[0] < list1[-1] * list2[-1]:
        return max_multiply_in_lists(list1[1:], list2[1:])
    return max_multiply_in_lists(list1[:-1], list2[:-1])


# 16-
def sum_digits(number):
    if number < 10:
        return number
    return number % 10 + sum_digits(number // 10)


# 17-
def print_reversed_number(number):
    """ Function gets positive number and prints a revered number"""
    if number < 10:
        print(number)
        return
    print(number % 10, end="")
    return print_reversed_number(number // 10)


# 18-
def reverse_number(number):
    """ Function gets positive number and returns a revered number"""
    if number < 10:
        return number
    return (number % 10) * (10 ** (number_of_digits(number) - 1)) + \
        reverse_number(number // 10)


# 19-
def print_chars_in_odd_place(string):
    if len(string) == 1:
        return
    print(string[1], end="")
    return print_chars_in_odd_place(string[2:])


# 20-
def print_chars_in_odd_place_in_reverse(string):
    if len(string) == 1:
        return
    print_chars_in_odd_place_in_reverse(string[2:])
    print(string[1], end="")


# 21-
def raise_to_power(base, exponent):
    if exponent == 1:
        return base
    if exponent % 2 == 0:
        return raise_to_power(base * base, exponent / 2)
    return base * raise_to_power(base, exponent - 1)


# 22-
def sum_all_odd_fractions_to_number(n):
    """ Function gets a number and returns a sum of all odd 1/n (from 1 to n) """
    if n == 0:
        return n
    if n % 2 != 0:
        return 1 / n + sum_all_odd_fractions_to_number(n - 1)
    return sum_all_odd_fractions_to_number(n - 1)


# 23-
def get_number_of_attached_letters_in_string(string, letter1, letter2):
    """ Function gets a string, and two chars, and returns the number of times
        the first char is followed by the second.
    """
    if len(string) <= 1:
        return 0
    if string[0] == letter1 and string[1] == letter2:
        return 1 + get_number_of_attached_letters_in_string(string[2:], letter1, letter2)
    return get_number_of_attached_letters_in_string(string[1:], letter1, letter2)


# 24-
def get_second_biggest_number(integers_list):
    if len(integers_list) == 2:
        return integers_list[0] if integers_list[0] < integers_list[1] else integers_list[1]
    if integers_list[0] > integers_list[1]:
        integers_list.append(integers_list[0])
    return get_second_biggest_number(integers_list[1:])


# 25-
def is_up(number):
    if number < 10:
        return True
    if number % 10 > (number % 100) // 10:
        return is_up(number // 10)
    return False


# 26-
def sort_one_element(integers_list, length):
    if length == 0:
        return integers_list
    if integers_list[0] > integers_list[length - 1]:
        integers_list[0], integers_list[length - 1] = integers_list[length - 1], integers_list[0]

    return sort_one_element(integers_list, length - 1)


# 27-
def sort_list(integers_list):
    integers_list = sort_one_element(integers_list, len(integers_list))
    sorted_list = [integers_list[0]]
    for i in range(len(integers_list) - 1):
        integers_list = sort_one_element(integers_list[1:], len(integers_list[1:]))
        sorted_list.append(integers_list[0])
    return sorted_list


def test_all():
    assert number_of_digits(18654) == 5
    assert sum_from_one_to_number(6) == 21
    assert factorial(5) == 120
    assert multiply_digits(2242) == 32
    assert multiply_of_evens_to_number(6) == 48
    assert multiply_even_digits(22198) == 32
    assert multiply_of_non_divided_by_3_or_5_to_number(6) == 8
    assert multiply_digits_non_divided_by_3_or_5(532082) == 32
    assert average_of_one_to_number(5) == 3.0
    assert fibonacci_number(9) == 34
    assert fibonacci_number_iterative(9) == 34
    assert series_number_1(4) == 4
    assert series_number_2(4) == 2.5
    assert series_number_3(3) == (2 * (2 * 3) ** 0.5) ** 0.5
    assert multiply_elements_in_list([1, 2, 4, 4]) == 32
    assert max_number_in_list([8, 0, 9, 6]) == 9
    assert bubble_sort_smallest([15, 5, -9, 0], 4) == [-9, 5, 0, 15]
    assert bubble_sort([15, 5, -9, 0]) == [-9, 0, 5, 15]
    assert gcd(91, 7) == 7
    assert max_multiply_in_lists([1, 4, -7], [1, -6, -7]) == 49
    assert sum_digits(910622) == 20
    assert reverse_number(169) == 961
    assert raise_to_power(2, 8) == 256
    assert sum_all_odd_fractions_to_number(4) == 4 / 3
    assert get_number_of_attached_letters_in_string("Hellolo Warlord", "l", "o") == 3
    assert get_second_biggest_number([7, 0, 3, -7]) == 3
    assert is_up(17032) is False
    assert sort_one_element([9, 2, 3, 6], 4) == [2, 3, 6, 9]
    assert sort_list([9, 6, 3, 2]) == [2, 3, 6, 9]


def main():
    # print(number_of_digits(18654))  # = 5
    # print(sum_from_one_to_number(6))  # = 21
    # print(factorial(5))  # 120
    # print(multiply_digits(2242))  # = 32
    # print(multiply_of_evens_to_number(6))  # = 48
    # print(multiply_even_digits(22198))  # = 32
    # print(multiply_of_non_divided_by_3_or_5_to_number(6))  # = 8
    # print(multiply_digits_non_divided_by_3_or_5(532082))  # = 32
    # print(average_of_one_to_number(5))  # = 3.0
    # print(fibonacci_number(9))  # = 34
    # print(fibonacci_number_iterative(9))  # = 34
    # print(series_number_1(4))  # = 4
    # print(series_number_2(4))  # = 2.5
    # print(series_number_3(3))  # = sqrt(2 * sqrt(2*3)) = 2.2133
    # print(multiply_elements_in_list([1, 2, 4, 4]))  # = 32
    # print(max_number_in_list([8, 0, 9, 6]))  # = 9
    # print(bubble_sort_smallest([15, 5, -9, 0], 4))  # = [-9, 5, 0, 15]
    # print(bubble_sort([15, 5, -9, 0]))  # = [-9, -2, 0, 5, 15]
    # print(gcd(91, 7))  # = 7
    # print(max_multiply_in_lists([1, 4, -7], [1, -6, -7]))  # = 49
    # print(sum_digits(910622))  # = 20
    # print_reversed_number(169)  # = 961
    # print(reverse_number(169))  # = 961
    # print_chars_in_odd_place("Hello World")  # = "el ol"
    # print_chars_in_odd_place_in_reverse("Hello World")  # = "lo le"
    # print(raise_to_power(2, 8))  # = 256
    # print(sum_all_odd_fractions_to_number(4))  # = 1 + (1/3) =~ 1.33
    # print(get_number_of_attached_letters_in_string("Hellolo Warlord", "l", "o"))  # = 3
    # print(get_second_biggest_number([7, 0, 3, -7]))  # = 3
    # print(is_up(17032))  # = False
    # print(sort_one_element([9, 2, 3, 6], 4))  # = [2, 3, 6, 9]
    # print(sort_list([9, 6, 3, 2]))  # = [2, 3, 6, 9]
    return


main()
test_all()
