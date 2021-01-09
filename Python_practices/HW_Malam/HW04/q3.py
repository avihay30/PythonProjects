def is_alternately_sorted(int_list):
    print("in func:", int_list)
    if len(int_list) <= 2:
        return True
    if int_list[0] <= int_list[2]:
        if len(int_list) <= 3:
            return True
        if int_list[1] >= int_list[3]:
            return is_alternately_sorted(int_list[2:])
    return False


def main():
    list_length = int(input("Enter integers list size: "))
    integers_list = []

    for i in range(list_length):
        integers_list.append(int(input("%s. " % i)))

    print(integers_list)
    print("" if is_alternately_sorted(integers_list) else "not", "alternately sorted")


main()
