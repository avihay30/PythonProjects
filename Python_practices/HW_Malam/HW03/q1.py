def my_split(str, ch):
    new_list = []
    new_string = ""
    for char in str:
        if char != ch:
            new_string += char
        else:
            new_list.append(new_string)
            new_string = ""
    new_list.append(new_string)
    return new_list


def main():
    string = "This is an example of how split works"
    print(my_split(string, " "))
    print(my_split(string, "s"))
    print(my_split(string, "x"))
    print(my_split(string, "y"))


main()
