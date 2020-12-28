def my_split(str, ch):
    """ Function my_split gets a string and char,
        and returns a list of substrings, and the char as a 
        divider(the divider doesn't included). 
    """
    new_list = []
    new_string = ""
    # running on each char in the "str"
    for char in str:
        if char != ch:
            # if chars are not equal concatenating the char to "new_string"
            new_string += char
        else:
            # if equal, adding "new_string" to the list.
            new_list.append(new_string)
            new_string = ""
    # adding the last "new_string"
    new_list.append(new_string)
    return new_list


def main():
    """ Function main calls the "my_place" function
        and prints the result according to hard-codded string.
    """
    string = "This is an example of how split works"
    print(my_split(string, " "))
    print(my_split(string, "s"))
    print(my_split(string, "x"))
    print(my_split(string, "y"))


main()
