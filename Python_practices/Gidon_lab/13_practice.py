# 1-
def length_of_string(s):
    """ Function length_of_string gets a string and return the size of it."""
    # calling the same function with size -1 of "s" every summon.
    return 1 + length_of_string(s[1:]) if s != "" else 0


def main():
    text = "Experimental text to test recursive function."
    print("Length of string:\n%s\n is %d." % (text, length_of_string(text)))


main()


# 2-
def recursive_has_prefix(str1, prefix):
    """ Function recursive_has_prefix gets two string and checks
        if the "prefix" is prefix to the other and return a boolean answer.
    """
    # if "str1" is larger in size than the "prefix".
    if len(str1) >= len(prefix):
        # empty string always prefix to any string.
        if prefix == "":
            return 1
        # checking if first char in both string are equal.
        if str1[0] == prefix[0]:
            # calling my self if there is left to check in "prefix".
            return recursive_has_prefix(str1[1:], prefix[1:]) \
                if len(prefix) > 1 else 1


def main():
    isPrefix = True
    while isPrefix:
        str1 = input("Please enter a string: ")
        pref = input("Please enter a prefix string: ")
        isPrefix = recursive_has_prefix(str1, pref)
        if isPrefix:
            print("The text has the prefix")
        else:
            print("No prefix")
    print()


main()


# 3-
def is_palindrome(arr):
    """ Function is_palindrome gets a list and returns whether
        the list is palindrome or not.
    """
    # if list contains one element or less it's a palindrome by definition.
    if len(arr) > 1:
        if arr[0] == arr[-1]:
            # calling the function again in order to check
            # if all the rest of the element are equal.
            return is_palindrome(arr[1:-1])
        else:
            return False
    return True


def main():
    """ Function main gets a list from the user and
        checks if the list is palindrome by calling a util function.
    """
    while True:
        palindrome_list = []
        # gets a string with "," separating the numbers.
        string = input("Enter numbers separated by comma: ")
        # splitting the string into list of string numbers
        list_of_string = string.split(",")
        # converting the string numbers into integers.
        for i in range(len(list_of_string)):
            if list_of_string[i] != "":
                palindrome_list.append(int(list_of_string[i]))
        # prints the result to the user according to the returned value of "is_palindrome"
        print("The array is", "" if is_palindrome(palindrome_list)
        else "not", "a palindrome")

        is_retry = input("Try again? (y/n): ")
        # checking if to stop the endless loop
        if is_retry == "N" or is_retry == "n":
            print("Finish")
            break


main()


def is_sum(numbers_list, s):
    """ Function is_sum gets a list and sun 
        and checks if there is a possiblity to sum some numbers
        in list in order to get sum
    """
    print(numbers_list)
    if s == 0:
        return True
    if numbers_list == []:
        return False
    return is_sum(numbers_list[1:], s - numbers_list[0]) or \
           is_sum(numbers_list[1:], s)


print(is_sum([1, 3, 1, 2, 4, 0, 3], -8))


def fib(index, no1, no2, n):
    """Function that returns the n number in fib series"""
    if index == n - 2:
        return no1 + no2
    return fib(index + 1, no2, no1 + no2, n)


def fib_rec(n):
    """Function that returns the n number in fib series with recursion"""
    if (n <= 1):
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)
