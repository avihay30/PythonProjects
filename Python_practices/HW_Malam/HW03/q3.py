def strCompress(string):
    compressed_str = ""
    counter = 0
    for i in range(len(string) - 1):
        counter += 1
        if string[i] != string[i+1]:
            compressed_str += string[i] + str(counter)
            counter = 0
    compressed_str += string[-1] + str(counter + 1)
    return compressed_str


def strRestored(string):
    restored_str = ""
    multiplier = ""
    index = 0
    while index < len(string):
        if string[index].isalpha():
            alpha = string[index]
            for j in range(index + 1, len(string)):
                if string[j].isalpha():
                    index = j - 1
                    break
                multiplier += string[j]
            restored_str += alpha * int(multiplier)
            multiplier = ""
        index += 1
    return restored_str


def main():
    section_chain = input("Enter a section chain to compress: ")
    print("The compressed string is:", strCompress(section_chain))
    compressed_string = input("Enter a compressed string: ")
    print("The restored string is:", strRestored(compressed_string))


main()
