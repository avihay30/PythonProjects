def is_mirror(string, mirror_str):
    if len(string) == len(mirror_str):
        if string == "":
            return True
        if string[-1] == mirror_str[0]:
            return is_mirror(string[:-1], mirror_str[1:])
    return False


def main():
    strings = ["abcd", "$", "axcd", "edcba", "32z1yx"]
    mirrors = ["dcba", "$", "dcba", "abcde", "xyz123"]

    for i in range(len(strings)):
        is_str_mirror = is_mirror(strings[i], mirrors[i])
        print(mirrors[i], "is" if is_str_mirror else "not", "a mirror of", strings[i])


main()
