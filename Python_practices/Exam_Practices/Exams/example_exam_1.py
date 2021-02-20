# example exam from braude college(integers_list.k.integers_list "בחינה לדוגמה.doc" file)

def guest_country(n):
    ct_list = [0] * 10
    for i in range(n):
        ct_list[int(input())] += 1

    for i in range(len(ct_list)):
        if ct_list[i] > 0:
            print("%3d %3d" % (i, ct_list[i]))


def guest_country_2(n):
    ct_list = [0] * 10
    for i in range(n):
        ct_list[int(input())] += 1
    copy_of_list = []
    for counter in ct_list:
        copy_of_list.append(counter)
    ct_list.sort()
    for counter in ct_list:
        if counter > 0:
            index = copy_of_list.index(counter)
            copy_of_list[index] = 0
            print("%3d %3d" % (index, counter))


def count_sequences(string):
    counter = 1
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            counter += 1
    return counter


def long_colored(string):
    counter = 0
    index_of_longest = 0
    maximum_seq = 0
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            counter += 1
        else:
            if maximum_seq < counter:
                maximum_seq = counter
                index_of_longest = i - maximum_seq
            counter = 0
    if maximum_seq < counter:
        maximum_seq = counter
        index_of_longest = len(string) - 1 - maximum_seq
    return index_of_longest


def print_mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            print("%4d" % mat[i][j], end="")
        print()


def magic_rows(mat):
    max_row_sum = 0
    for row in mat:
        max_row_sum = max(sum(row), max_row_sum)

    for i in range(len(mat)):
        mat[i][-1] += max_row_sum - sum(mat[i])

    print_mat(mat)
    return mat


def main():
    # guest_country(14)
    # guest_country_2(14)
    print(count_sequences("rrbbbyrr"))  # = 4
    print(long_colored("rrrbbbbyrrrrrrr"))  # = 8
    print(magic_rows([[10, 20, 5, 15],
                      [20, 10, 15, 5],
                      [1, 2, 3, 4],
                      [5, 6, 7, 8]]))
    return


main()
