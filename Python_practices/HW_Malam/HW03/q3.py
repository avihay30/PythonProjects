def strCompress(string):
    """ Function strCompress gets a string and returns its compressed form.
    """
    compressed_str = ""
    # declaring a counter the will holds the number of
    # appearances of the char.
    counter = 0
    for i in range(len(string) - 1):
        counter += 1
        # checking if the current char isn't equal the next one.
        if string[i] != string[i+1]:
            # concatenating the char and "counter" and adding it
            # to "compressed_str"
            compressed_str += string[i] + str(counter)
            # resetting counter
            counter = 0
    # adding the last char to the "compressed_str".
    compressed_str += string[-1] + str(counter + 1)
    return compressed_str


def strRestored(string):
    """ Function strRestored gets a compressed string
        and returns the restored form of the string.
    """
    restored_str = ""
    multiplier = ""
    index = 0
    # running loop len(string) times.
    while index < len(string):
        if string[index].isalpha():
            # declaring "alpha" that holds the char.
            alpha = string[index]
            # running loop until the string[i] is letter.
            for i in range(index + 1, len(string)):
                if string[i].isalpha():
                    # changing index to skip the unwonted
                    # iterations in the while loop.
                    index = i - 1
                    break
                multiplier += string[i]
            # adding the restored char to the "restored_str"
            # by multiplying in counter.
            restored_str += alpha * int(multiplier)
            multiplier = ""
        index += 1
    return restored_str


def main():
    """ Function main gets an input from the user of
        section chain and compressed string and prints the
        returned value from the right function.
    """
    section_chain = input("Enter a section chain to compress: ")
    print("The compressed string is:", strCompress(section_chain))
    compressed_string = input("Enter a compressed string: ")
    print("The restored string is:", strRestored(compressed_string))


main()
