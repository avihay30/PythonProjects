# 1-
def most_common_letter(string):
    """ Function most_common_letter gets a string,
        and returns the most common letter in that string
    """
    # counters_list
    letter_counter = [0] * 26
    for char in string:
        # checking if in range of the lower\upper case letters in ascii.
        if 64 < ord(char) < 91 or 96 < ord(char) < 123:
            # the index of the letter in alphabet order.
            char_index = ord(char.lower()) - 97
            letter_counter[char_index] += 1

    # the index of the most common letter in the counters list.
    max_index = letter_counter.index(max(letter_counter))
    # if no letters exists in "string".
    if letter_counter[max_index] == 0:
        return -1
    # converting to letter.
    most_common_letter = chr(max_index + 97)

    return most_common_letter

def main():
    while True:
        string = input("Enter a string please: ")

        if string == "quit" or string == "Quit":
            print("Thank you for exploring strings and complexity")
            break

        print("mode('%s') returns %s" % (string, most_common_letter(string)))

main()

# 3-
def maxSort(numbers_list):
    """ Function maxSort gets an list of numbers,
        and returns a sorted list, by moving the biggest
        number in every iteration to the end of the list.
    """
    # running from the end to the beginning.
    for i in range(len(numbers_list) - 1, 0, -1):
        maxIndex = i
        for j in range(i):
            if numbers_list[j] > numbers_list[maxIndex]:
                maxIndex = j

        # replacing elements in list by each other,
        # can be done also by doing a,x = x,a but it's less readable.
        tmp_number = numbers_list[i]
        numbers_list[i] = numbers_list[maxIndex]
        numbers_list[maxIndex] = tmp_number
        
    return numbers_list


def main():
    while True:
        list_size = int(
            input("Please enter the number of elements in the list: "))
        if list_size == 0:
            print("Thank you for exploring max sort")
            break
        
        num_list = []
        # inserting the inputted numbers to the "num_list".
        for i in range(list_size):
            num_list.append(int(input()))
    
        print("the list, before sorting:", num_list)
        print("the list, after sorting:", maxSort(num_list))


main()


# # practice
# def is_snake_sorted(l):
#     # i = col
#     for i in range(len(l[0])):
#         if i % 2 == 0:
#             for j in range(len(l) - 1):
#                 if l[j][i] > l[j+1][i]:
#                     return False
#         else:
#             for j in range(len(l) - 1):
#                 if l[j][i] < l[j+1][i]:
#                     return False
#
#     for i in range(len(l) -1):
#         if l[0][i] > l[0][i+1] or l[-1][i] > l[-1][i+1]:
#             return False
#
#     return True

# def intersection(l, x, y):
#     #sum_of_row = sum(l[x])
#     sum_of_row = 0
#     sum_of_col = 0
#     row_sums = []
#     col_sums = []
#     for i in range(len(l)):
#         row_sums.append(sum(l[i]))
#         for j in range(len(l)):
#             sum_of_col += l[i][j]
#
#         col_sums.append(sum_of_col)
#         sum_of_col = 0
#
#     print(row_sums, col_sums)
#     return sum_of_row == sum_of_col
#
# def is_2x2(a, num):
#     # rows
#     for i in range(len(a[0]) - 1):
#         # cols
#         for j in range(len(a) - 1):
#             if (a[i][j] == a[i][j+1] and a[i+1][j] == a[i+1][j+1])\
#             and a[i][j] == num:
#                 return True
#     return False
#
#
# w = [[1,8,9,16,17],[2,7,5,5,18],[3,6,5,5,19],[4,5,12,13,28]]
# print(is_2x2(w, 5))
#
# a=[[0, 7, 9, 2, 3],[1, 4,-1, 3, 0],[2, 2,-3,-1, 5],[0, 0, 2, 0,-3]]
# print(intersection(a, 1, 2))
#
# list_a = [[-1, 8, 9, 16, 17], [2, 7, 10, 15, 18], [3,6,11,14,19], [4,5,12,13,28]]
# print(is_snake_sorted(list_a))
