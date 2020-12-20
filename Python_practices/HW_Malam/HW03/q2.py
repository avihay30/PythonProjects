def has_leading_zeros(number):
    if len(number) > 0 and number.startswith("0"):
        return True
    return False


def is_legal_ip(string):
    split_string = string.split(".")
    if len(split_string) != 4:
        return False
    for element in split_string:
        if element.isdigit() and 0 <= int(element) <= 255 \
                and not has_leading_zeros(element):
            continue
        else:
            return False
    return True


def main():
    print(is_legal_ip("192.168.1.1"))
    print(is_legal_ip("125.34.251.43"))
    print(is_legal_ip("001.23.45.123"))
    print(is_legal_ip("125.512.100.xy8"))
    print(is_legal_ip("125.512.."))
    print(is_legal_ip("192.168.0.1"))


main()
