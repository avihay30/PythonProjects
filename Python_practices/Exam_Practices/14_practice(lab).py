# 1-
def print_sorted(integers):
    """ Function print_sorted(recursive) gets a list of integers
        and prints the orders list(low to high).
    """
    if len(integers) == 1:
        print(integers[0], end=" ")
        return
    if integers[0] < integers[-1]:
        print(integers[0], end=" ")
        return print_sorted(integers[1:])
    else:
        print(integers[-1], end=" ")
        return print_sorted(integers[:-1])


def main():
    list_of_integers = []
    size_of_list = int(input("Enter size of integers list: "))

    for i in range(size_of_list):
        list_of_integers.append(input())
    print_sorted(list_of_integers)


main()


# 2-
def double(string):
    """ Function double(recursive) gets a string
        and returns the number of appearances of doubled small attached letters
    """
    if len(string) == 1:
        return 0
    if 96 < ord(string[0]) < 123 and string[0] == string[1]:
        return 1 + double(string[1:])
    return double(string[1:])


def main():
    number_of_appearances = double(input("Enter a string: "))
    print("The number of appearances of doubled small attached letters is:",
          number_of_appearances)


main()
