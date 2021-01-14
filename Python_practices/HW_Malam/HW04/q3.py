def is_alternately_sorted(int_list):
    """ Function is_alternately_sorted is a recursive function that
        gets a list of integers and returns whether the list is alternately sorted.
    """
    # if list size is smalled/equal to 2 it's alternately sorted by definition.
    if len(int_list) <= 2:
        return True
    # checking the first and second even slots if they are sorted.
    if int_list[0] <= int_list[2]:
        # checking if the second odd slot is not exists.
        if len(int_list) <= 3:
            return True
        # if there is to check between odd slots, checking if they are sorted.
        if int_list[1] >= int_list[3]:
            # calling the function without the first even and odd slots.
            return is_alternately_sorted(int_list[2:])
    return False


def main():
    """ Function main gets a list of integers from the user and
        prints whether the list is alternately sorted.
    """
    list_length = int(input("Enter integers list size: "))
    integers_list = []
    # getting from user all list element according to inputted list size.
    for i in range(list_length):
        integers_list.append(int(input("%s. " % i)))

    print()
    print(integers_list)
    # printing the result whether the list is alternately sorted,
    # according to returned value from "is_alternately_sorted" function.
    print("" if is_alternately_sorted(integers_list) else "not", "alternately sorted")


main()
