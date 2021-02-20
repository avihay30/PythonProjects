# example exam from braude college(a.k.a "לקט בחינות משנים קודמות.docx" file)

def right_circle_shift(integers_list):
    for i in range(len(integers_list) - 1):
        integers_list[i], integers_list[-1] = integers_list[-1], integers_list[i]
    return integers_list


def in_all_rows(mat):
    numbers_range = 10
    ct_mat = []
    for i in range(numbers_range):
        ct_mat.append([0] * len(mat))

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            ct_mat[mat[i][j]][i] += 1

    list_of_repeated = []
    for i in range(len(ct_mat)):
        if 0 not in ct_mat[i]:
            list_of_repeated.append(i)

    if len(list_of_repeated) == 0:
        print("No common elements.")
    else:
        print("Common element(s):", end=" ")
        for element in list_of_repeated:
            print(element, end=" ")


def foo(lst):
    lst1 = lst
    lst1 = lst1 + [6]
    lst1[0] = 20
    length = len(lst)
    lst2 = lst + [lst[length - 1 - i] + 2 for i in range(length)]
    print("lst2=", lst2)
    sum1 = sum(lst2[-1::-2])
    sum2 = sum(lst2[::2])
    return sum1, sum2


def find_elem(mat, num):
    N = len(mat)
    M = len(mat[0])
    if N == 0:
        return -1
    low, high = 0, N * M - 1
    while low <= high:
        mid = (low + high) // 2
        Xindex = mid // M
        Yindex = mid % M
        if mat[Xindex][Yindex] == num:
            return Xindex, Yindex
        if mat[Xindex][Yindex] > num:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def natural_power(a, b):
    if b == 1:
        return a
    temp = natural_power(a, b // 2)
    temp *= temp
    if b % 2 == 1:
        temp *= a
    return temp


def main():
    print(right_circle_shift([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    # =
    # [[10, 20, 5, 15],
    # [20, 10, 15, 5],
    # [1,  2,  3,  44],
    # [5,  6,  7,  32]]
    print(natural_power(2, 6))
    in_all_rows([[7, 1, 3, 0, 4, 6],
                 [2, 5, 0, 6, 6, 1],
                 [6, 1, 7, 2, 4, 0],
                 [1, 1, 7, 6, 8, 9],
                 [5, 5, 6, 1, 5, 3],
                 [4, 1, 4, 3, 6, 0],
                 [4, 6, 1, 7, 4, 3]])  # = Common element(s): 1 6

    print()
    print(find_elem(
        [[1, 5, 9, 11],
         [14, 20, 21, 26],
         [30, 34, 43, 50]], 11
    ))

    lst1 = [1, 2, 3, 4, 5, 6]
    sum1, sum2 = foo(lst1)
    print("lst1=", lst1)
    print("Odd" if sum1 > sum2 else "Even")


main()


def array_mult(A, B):
    C = [[]]
    sum = 0
    if len(A[0]) == len(B):
        for i in range(len(A)):
            for k in range(len(B[0])):
                for j in range(len(A[i])):
                    sum += A[i][j] * B[j][k]
                C[i].append(sum)
                sum = 0
            if i < len(A) -1:
                C.append([])
        return C


M1 = [[1, 2, 3], [-2, 3, 7]]
M2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
M3 = [[1], [0], [-1]]

print(array_mult(M1, M3))