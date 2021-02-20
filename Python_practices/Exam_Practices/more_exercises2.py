# exercises from "problems before exam" from braude collage

def sort_small_to_big(letters_list):
    """ With space complexity of O(n)"""
    original_len = len(letters_list)
    for i in range(len(letters_list)):
        if "a" <= letters_list[i] <= "z":
            letters_list.append(letters_list[i])

    for i in range(len(letters_list)):
        if "A" <= letters_list[i] <= "Z":
            letters_list.append(letters_list[i])
    return letters_list[original_len:]


def sort_small_to_big_2(lst):
    """ With space complexity of O(1)"""
    start = 0
    end = len(lst) - 1
    while start < end:
        if 'a' <= lst[start] <= 'z':
            start += 1
        if 'A' <= lst[end] <= 'Z':
            end -= 1
        if 'A' <= lst[start] <= 'Z' and 'a' <= lst[end] <= 'z':
            lst[start], lst[end] = lst[end], lst[start]
            start += 1
            end -= 1
        if 'A' <= lst[start] <= 'Z' and 'A' <= lst[end] <= 'Z':
            end -= 1
    return lst


def reverse_string(s1):
    i, j = 0, len(s1) - 1
    s2 = s3 = ''
    while i <= j:
        s2 += s1[j]
        if i < j:
            s3 = s1[i] + s3
        i += 1
        j -= 1
    return s2 + s3


def number_of_followers(sorted_list):
    counter = 1
    for i in range(len(sorted_list) - 1):
        if sorted_list[i] + 1 == sorted_list[i + 1]:
            continue
        else:
            counter += 1
    return counter


def range_matrix(sorted_list):
    arr2D = [[], []]
    arr2D[0].append(sorted_list[0])
    for i in range(len(sorted_list)):
        if number_of_followers(sorted_list[i:i + 2]) == 1:
            continue
        arr2D[1].append(sorted_list[i])
        if i > 0:
            arr2D[0].append(sorted_list[i + 1])
    arr2D[1].append(sorted_list[-1])

    for i in range(len(arr2D)):
        for j in range(len(arr2D[i])):
            print(arr2D[i][j], end=" ")
        print()


def biggest_seq(int_list):
    if len(int_list) == 1:
        return 1
    tmp_max = 1
    counter = 1
    for i in range(len(int_list) - 1):
        if int_list[i] < int_list[i + 1]:
            counter += 1
        else:
            if counter > tmp_max:
                tmp_max = counter
                counter = 1
    if counter > tmp_max:
        tmp_max = counter
    return tmp_max


def get_perimeter_min(matrix, row_num):
    mini = matrix[row_num][row_num]
    if row_num == 0:
        mini = min(min(matrix[0], matrix[-1]))
    for i in range(row_num, len(matrix) - row_num):
        if i == row_num or i == len(matrix) - row_num - 1:
            for j in range(len(matrix[i])):
                if row_num <= j <= len(matrix) - row_num - 1:
                    mini = min(mini, matrix[i][j])

    for i in range(row_num + 1, len(matrix) - row_num - 1):
        mini = min(mini, matrix[i][row_num], matrix[i][-1 - row_num])
    return mini


def get_perimeter_max(matrix, row_num):
    maxi = max(max(matrix[row_num], matrix[-1 - row_num]))
    for i in range(row_num + 1, len(matrix) - row_num - 1):
        maxi = max(maxi, matrix[i][row_num], matrix[i][-1 - row_num])
    return maxi


def is_pyramid_matrix(matrix):
    for i in range((len(matrix) // 2) - 1):
        if get_perimeter_max(matrix, i) < get_perimeter_min(matrix, i + 1):
            continue
        return False
    if len(matrix) % 2 != 0:
        if matrix[(len(matrix) - 1) // 2][(len(matrix) - 1) // 2] < \
                get_perimeter_max(matrix, (len(matrix) // 2) - 1):
            return False
    return True


def get_perimeter_list(matrix, row_num):
    perim_list = []
    if row_num == 0:
        perim_list.extend(matrix[0])
        perim_list.extend(matrix[-1])
    perim_list.extend(matrix[row_num][row_num:-row_num])
    perim_list.extend(matrix[-1-row_num][row_num:-row_num])
    for i in range(row_num + 1, len(matrix) - row_num - 1):
        perim_list.append(matrix[i][row_num])
        perim_list.append(matrix[i][-1-row_num])
    return perim_list


def is_pyramid_matrix_2(matrix):
    """ Space complexity of O(n) """
    comp_matrix = []
    for i in range(len(matrix) // 2):
        comp_matrix.append(get_perimeter_list(matrix, i))

    for k in range(len(comp_matrix) - 1):
        if max(comp_matrix[k]) < min(comp_matrix[k + 1]):
            continue
        return False
    if len(matrix) % 2 != 0:
        if matrix[(len(matrix) - 1) // 2][(len(matrix) - 1) // 2] < max(comp_matrix[-1]):
            return False
    return True


def main():
    # print(sort_small_to_big(['K', 'f', 'H', 'T', 'm']))  # = ['f', 'm', 'K', 'H', 'T']
    print(sort_small_to_big_2(['K', 'f', 'H', 'T', 'm']))  # = ['f', 'm', 'K', 'H', 'T']
    # print(reverse_string("FOREVER"))  # = REVEROF
    # print(number_of_followers([-10, -9, 3, 7, 8, 9]))
    # print(number_of_followers([-10, -9, 3]))
    # range_matrix([-10, -9, 3, 7, 8, 9])
    print(biggest_seq([1, 2, 3, 2, 3, 4, 5]))
    # print(is_pyramid_matrix([[7, 8, 4, -1], [1, 13, 22, 0], [5, 20, 19, 9], [-2, 0, 6, 6]]))
    print(is_pyramid_matrix([[7, 8, 9, 4, -1],
                             [1, 13, 17, 22, 0],
                             [7, 19, 25, 16, 12],
                             [5, 20, 21, 19, 9],
                             [-2, 0, 8, 6, 6]]))

    print(is_pyramid_matrix([[1, 2, 3, 4],
                             [1, 2, 3, 4],
                             [1, 2, 3, 4],
                             [1, 2, 3, 4]]))  # = False
    print(is_pyramid_matrix([[1, 2, 3, 4, 5, 6],
                             [1, 12, 12, 12, 12, 7],
                             [1, 14, 20, 16, 12, 8],
                             [1, 15, 16, 20, 12, 9],
                             [1, 12, 12, 12, 12, 10],
                             [1, 11, 11, 11, 11, 11]]))

    return


main()
