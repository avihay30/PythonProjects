# 1-
def filter_non_letters(string):
    """ Function filter_non_letters gets a string
        and returns a string with only letters.
    """
    letters_string = ""
    for char in string:
        if char.isalpha():
            letters_string += char

    return letters_string


def largest_letter(string_of_letters):
    """ Function largest_letter gets a string
        and returns the maximum letter of that string.
    """
    return max(string_of_letters)


def smallest_letter(string_of_letters):
    """ Function smallest_letter gets a string
        and returns the minimum letter of that string.
    """
    return min(string_of_letters)


def main():
    # getting an input of a string from the user.
    sentence = input("Enter your sentence: ")
    # declaring a variable that contains the inputted
    # string with only letters.
    letters = filter_non_letters(sentence)
    # changing the letters to lower-case
    letters = letters.lower()
    # checking if the inputted string doesn't contain letters at all.
    if letters == "":
        print("Please enter a sentence with letters next time.")
        # stopping the function.
        return
    # printing the largest and smallest letters in the inputted string.
    print("Largest and smallest alphabet are: %s %s" %
          (largest_letter(letters), smallest_letter(letters)))


# running main function.
main()


# 2-
def remove_duplicates_chars(string):
    """ Function remove_duplicates_chars gets a string
        and returns the string without any double chars.
    """
    # declaring an empty string the will contain a
    # string without double chars.
    new_string = ""
    # running in a loop len(string) - 1 times.
    for i in range(len(string) - 1):
        # checking if the there is duplicate char
        if string[i] == string[i + 1]:
            # skip the iteration.
            continue
        # if not duplicate char, adds the char to "new_string".
        new_string += string[i]
    # adding the last letter to "new_string".
    new_string += string[-1]

    return new_string


def main():
    # getting an input of a string from the user.
    sentence = input("Enter a string, please: ")
    # printing the new string without duplicates.
    print("After removing all duplicates:", remove_duplicates_chars(sentence))


# running main function.
main()


# 3-
def print_letters_separately(string):
    """ Function print_letters_separately gets a string
        and prints the letters in separate lines.
    """
    # declaring an empty string the will contain a
    # string with \n between letters.
    new_string = ""
    # running in a loop len(string) times.
    for i in range(len(string)):
        # checking if the char(string[i]) doesn't contain a space or tab.
        if string[i] == " " or string[i] == "\t":
            # checking if the "new_string" not ends with "\n",
            # and new_string is empty(in case we have space in the beginning).
            if not new_string.endswith("\n") and new_string != "":
                # adds "\n" in the end of the "new_string",
                # that represent the place of a space between letters,
                # will print empty line in each char if we print "new_string".
                new_string += "\n"
        else:
            # if there is not space, and we are between letters.
            # adds the char(string[i]) to "new_string".
            new_string += string[i]
    # print the "new_string" with \n between letters.
    print(new_string)


def main():
    # running an endless loop.
    while True:
        # getting an input of a string from the user.
        sentence = input("Enter a string, please: ")
        # checking if the inputted string is empty.
        if sentence == "":
            print("Finish")
            # stopping the while.
            break
        # calling "print_letters_separately" with the inputted string.
        print_letters_separately(sentence)


# running main function.
main()


# training No.9
# def my_title(s1):
#     title = ""
#     for i in range(len(s1) - 1):
#         if s1[i] != " ":
#             if s1[i+1] == " ":
#                 if s1[i] >= "a" and s1[i] <= "z":
#                     title += chr(ord(s1[i]) - 32)
#                 else:
#                     title += s1[i]
#             else:
#                 if s1[i] <= "Z" and s1[i] >= "A":
#                     title += chr(ord(s1[i]) + 32)
#                 else:
#                     title += s1[i]
#         else:
#             title += " "
#     return title

# def palindrome(s1):
#     re_half_s1 = s1[::-1][len(s1) // 2:]
#     half_s1 = s1[len(s1) // 2:]
#     return re_half_s1 == half_s1
