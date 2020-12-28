def has_leading_zeros(number):
    """ Function has_leading_zeros gets a number
        and returns if the number has_leading_zeros
        (expect zero as one digit).
    """
    return len(number) > 1 and number.startswith("0")


def is_legal_ip(string):
    """ Function is_legal_ip get a string
        and returns if the string is legal ip or not.
    """
    # splitting the string by "." into a list.
    split_string = string.split(".")
    # checking if we have 4 decimal number.
    if len(split_string) != 4:
        return False
    # running on each element in the "split_string".
    for element in split_string:
        # checking if the element is valid.
        if element.isdigit() and 0 <= int(element) <= 255 \
                and not has_leading_zeros(element):
            continue
        else:
            # if not valid.
            return False
    return True


def main():
    """ Function main calls "is_legal_ip" function
        with hard-codded strings and prints the returned result.
    """
    print(is_legal_ip("192.168.1.1"))
    print(is_legal_ip("125.34.251.43"))
    print(is_legal_ip("001.23.45.123"))
    print(is_legal_ip("125.512.100.xy8"))
    print(is_legal_ip("125.512.."))
    print(is_legal_ip("192.168.0.1"))


main()
