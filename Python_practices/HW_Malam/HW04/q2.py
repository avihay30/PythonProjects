def is_mirror(string, mirror_str):
    """ Function is mirror gets two strings and return whether
        they are mirror of each other.
    """
    # if length of the strings are not equal they are also no mirror of each other.
    if len(string) == len(mirror_str):
        if string == "":
            return True
        # checking equality of last and first chars.
        if string[-1] == mirror_str[0]:
            # sending to the function a smaller size of
            # strings(first/last char is cut according to string).
            return is_mirror(string[:-1], mirror_str[1:])
    return False


def main():
    """ Function main has an hard-codded lists and checks prints if elements
        in one list are mirror of the other list.
    """
    strings = ["abcd", "$", "axcd", "edcba", "32z1yx"]
    mirrors = ["dcba", "$", "dcba", "abcde", "xyz123"]

    for i in range(len(strings)):
        is_str_mirror = is_mirror(strings[i], mirrors[i])
        # prints whether the strings are mirror of each other,
        # according to the returned value of is_str_mirror.
        print(mirrors[i], "is" if is_str_mirror else "is not", "a mirror of", strings[i])


main()
