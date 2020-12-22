# 1-
def hidden_str(s1, s2):
    """ Function hidden_str gets two strings,
        and returns if s2 is hidden in s1.
    """
    if len(s2) > len(s1):
        return False
    index_of_s2 = 0
    for i in range(len(s1)):
        # checking if s1[i] is equal to the first char in "s2"
        # (from left to right).
        if s1[i] == s2[index_of_s2]:
            index_of_s2 += 1
            # running in loop to check every char in s2
            # is exists in s1.
            for j in range(i+1, len(s1)):
                if s1[j] == s2[index_of_s2]:
                    # checking is all chars in s2 are checked.
                    if index_of_s2 == len(s2) - 1:
                        return True
                    index_of_s2 += 1
        # checking if s1[i] is equal to the last char in "s2"
        # (reversed order).
        elif s1[i] == s2[-1]:
            # setting the index to the next char from right.
            index_of_s2 = -2
            # running in loop to check every char in s2
            # is exists in s1(in reversed order).
            for j in range(i+1, len(s1)):
                if s1[j] == s2[index_of_s2]:
                    # checking is all chars in s2 are checked.
                    if index_of_s2 == -len(s2):
                        return True
                    index_of_s2 -= 1

    return False


def main():
    string = "Computer Science"
    list_of_hidden = ["optic", "nirto", "option"]
    for element in list_of_hidden:
        if hidden_str(string, element):
            print(element, "is hidden in", string)
        else:
            print(element, "is not hidden in", string)


main()


# 2-
def my_replace(s1, sub):
    """ Function my_replace gets a string and sub string,
        and returns a new string with upper-case in every appearance
        of the sub in the main string.
    """
    if len(sub) > len(s1):
        return s1
    list_of_indexes = []
    index_of_s1 = 0
    # # running in a loop of the indexes of the s1.
    while index_of_s1 < len(s1):
        # checking if both chars in s1 and sub are equal.
        # and if there is left to check in s1 for subs.
        if s1[index_of_s1] == sub[0] and len(s1) - index_of_s1 >= len(sub):
            if len(sub) == 1:
                list_of_indexes.append(index_of_s1)
                index_of_s1 += 1
                continue
            # checking if the whole sub is exists in s1.
            for j in range(len(sub)):
                if s1[index_of_s1 + j] == sub[j]:
                    if j == len(sub) - 1:
                        list_of_indexes.append(index_of_s1)
                        index_of_s1 += 1
                        break
                # if only part of sub is exists.
                else:
                    index_of_s1 += 1
                    break
        else:
            index_of_s1 += 1

    index = 0
    index_s1 = 0
    replaced_string = ""
    distance_between_subs = len(sub)
    while index_s1 < len(s1) and len(replaced_string) < len(s1):
        if index < len(list_of_indexes) - 1:
            # distance_between_subs for checking the case of sub in sub.
            distance_between_subs = list_of_indexes[index + 1] - list_of_indexes[index]
        if list_of_indexes and index_s1 == list_of_indexes[index]:
            # if there is sub in sub (e.g: ababa, aba -> ABABA)
            if distance_between_subs < len(sub):
                replaced_string += sub.upper() + sub.upper()[1:]
                index_s1 += len(sub) * 2 - 2
            # handling one sub.
            else:
                replaced_string += sub.upper()
                index_s1 += len(sub)
                if index < len(list_of_indexes) - 1:
                    index += 1
        # not a sub letter
        else:
            replaced_string += s1[index_s1]
            index_s1 += 1

    return replaced_string


def main():
    while True:
        text = input("Enter text: ")
        sub_string = input("Enter substring: ")
        # checking if to stop the unless loop
        if sub_string == "" or text == "":
            print("Finish")
            break
        replaced_text = my_replace(text, sub_string)
        print(replaced_text)


main()
