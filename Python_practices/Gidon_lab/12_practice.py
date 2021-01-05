# 1-
def is_row_equal(matrix, row_num):
    """ Function is_row_equal gets a matrix and number
        and returns if the sum of all number in that row
        is equal to the received num.
    """
    sum_of_row = 0
    # running number of cols of that row
    # [number of elements in list].
    for i in range(len(matrix[row_num])):
        sum_of_row += matrix[row_num][i]

    return sum_of_row == row_num

def is_diagonal_positive(matrix):
    """ Function is_diagonal_positive gets a matrix
        and returns if all nuumbers in the diagonal are positive.
    """
    # running len(rows) times.
    for i in range(len(matrix)):
        # checking the possibility that it's not a square matrix.
        if len(matrix[i]) < i + 1:
            return True
        if matrix[i][i] < 0:
            return False
    return True

def print_matrix(matrix):
    """ Function print_matrix get a matrix
        and prints it with space of 4 to the left between elements.
    """
    # run on rows
    for i in range(len(matrix)):
    # runs on col of each row
        for j in range(len(matrix[0])):
            print("%4d" % matrix[i][j], end=" ")
        print()

def is_mat_ok(matrix):
    """ Function is_mat_ok gets a matrix
        and retruns if the matrix is ok by calling
        "is_row_equal" and "is_diagonal_positive" functions.
    """
    # running on each row of matrix.
    for i in range(1, len(matrix)):
        if not is_row_equal(matrix, i):
            return False

    return is_diagonal_positive(matrix)

def main():
    """ Function main has hard-coded matrices and prints them
        and print if the matrices are ok(according to requirements).
    """
    matrix_a = [[31, -15, 0, -12, -4],
                [1, 1, -3, 2, 0],
                [12, -2, 4, -23, 11],
                [5, 0, 3, 2, -7],
                [1, 1, 0, 1, 1]]
    matrix_b = [[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 0],
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 0],
                [1, 2, 3, 4, 5]]
    print_matrix(matrix_a)
    print("Matrix A is", "ok" if is_mat_ok(matrix_a) else "not ok")
    print()

    print_matrix(matrix_b)
    print("Matrix B is", "ok" if is_mat_ok(matrix_b) else "not ok")

main()


# 2-
def get_matrix_from_user(dim):
    """ Function get_matrix_from_user gets a dimension of a matrix
        and return a user inputted matrix.
    """
    matrix = []
    row_list = []
    print("Enter the entries rowwise:")
    # running "dim" times, for rows.
    for i in range(dim):
        # running "dim" times, for cols.
        for j in range(dim):
            row_list.append(int(input()))
        # after getting all element of a row, appending it to the matrix.
        matrix.append(row_list)
        row_list = []

    return matrix


def print_matrix(matrix):
    """ Function print_matrix get a matrix
        and prints it with space of 4 to the left between elements.
    """
    # run on rows
    for i in range(len(matrix)):
        # runs on col of each row
        for j in range(len(matrix[0])):
            print("%4d" % matrix[i][j], end=" ")
        print()


def is_mat_perfect(matrix, dim):
    """ Function is_mat_perfect gets a matrix and the dimension of it
        and returns whether the matrix is perfect or not.
    """
    # two list of counter for row, and col.
    row_counter_list = [0] * dim
    col_counter_list = [0] * dim
    # running on rows.
    for i in range(dim):
        # running on cols.
        for j in range(dim):
            # checking if element is in bounds.
            if (0 < matrix[i][j] <= dim) and (0 < matrix[j][i] <= dim):
                # incrementing the right slot that represents the number,
                # counter_list[0] represents number of 1's
                row_counter_list[matrix[i][j] - 1] += 1
                col_counter_list[matrix[j][i] - 1] += 1
            # if not in bounds.
            else:
                return False

        # checking if the row/cols have more than one representative of a digit.
        if max(row_counter_list) > 1 or max(col_counter_list) > 1:
            return False
        row_counter_list = [0] * dim
        col_counter_list = [0] * dim

    return True


def main():
    """ Function main gets a dimension and matrix from user
        and prints if the matrix is perfect or not(according to requirements).
    """
    # an endlees loop until dimension is 0.
    while True:
        dimension = int(input("Enter the matrix dimension: "))
        if dimension == 0:
            print("Finish")
            break
        matrix = get_matrix_from_user(dimension)
        print_matrix(matrix)
        print("The Matrix is", "perfect" if is_mat_perfect(matrix, dimension) \
              else "not perfect")


main()

# practice
def recursive_max_value(lst):
    if len(lst) == 1:
        return lst[0]
    max_value = recursive_max_value(lst[1:])
    return lst[0] if lst[0] > max_value else max_value


list_a = [100, 50, 40, 35, 10, -5]
print(recursive_max_value(list_a))
