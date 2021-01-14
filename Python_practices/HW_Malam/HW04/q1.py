def get_max_size_of_row(matrix):
    """ Function get_max_size_of_row gets a matrix and
        and returns the size of the longest row in the matrix.
    """
    max_len_of_row = len(matrix[0])
    for row in matrix:
        if len(row) > max_len_of_row:
            max_len_of_row = len(row)
    return max_len_of_row


def warp_perimeter_of_matrix(matrix, wrapper):
    """ Function warp_perimeter_of_matrix get an matrix and a wrapper
        and return a square wrapped-matrix with that wrapper.
    """
    max_size_of_row = get_max_size_of_row(matrix)
    # creating a new matrix and the first row that contains the wrapper.
    # "max_size_of_row + 2" because first and last col will also contain the wrapper.
    wrapped_matrix = [[wrapper] * (max_size_of_row + 2)]
    for i in range(len(matrix)):
        # adding new row that has the wrapper in the beginning.
        wrapped_matrix.append([wrapper])
        for element in matrix[i]:
            # adding each element in "matrix" to the "wrapped_matrix".
            # i + 1 because the first row in the wrapped_matrix is list of wrappers.
            wrapped_matrix[i + 1].append(element)
        # adding the wrapper in the end of the row,
        # in case of non square matrix we fill the empty space in wrappers
        # in order to get an square matrix.
        for j in range(max_size_of_row - len(matrix[i]) + 1):
            wrapped_matrix[i + 1].append(wrapper)

    # adds the last row of the matrix that contains a list of wrappers.
    wrapped_matrix.append([wrapper] * (max_size_of_row + 2))
    return wrapped_matrix


def remove_non_real_neigh(list_of_neigh, wrapper):
    """ Function remove_non_real_neigh gets a list and a wrapper,
        and returns a list that doesn't contain the wrapper.
    """
    filtered_list = []
    for element in list_of_neigh:
        if element != wrapper:
            filtered_list.append(element)
    return filtered_list


def get_neighbors(matrix, row, col):
    """ Function get_neighbors gets an matrix and row,col number and
        and return a list of neighbors
    """
    # declaring a square_list that contains all the square of neighbors around the
    # matrix[row][col] element(without the element itself).
    square_list = [matrix[row - 1][col - 1],
                   matrix[row - 1][col],
                   matrix[row - 1][col + 1],
                   matrix[row][col - 1],
                   matrix[row][col + 1],
                   matrix[row + 1][col - 1],
                   matrix[row + 1][col],
                   matrix[row + 1][col + 1]]
    return square_list


def get_str_list_with_round_brackets(list):
    """ Function get_str_list_with_round_brackets gets a list and
        returns a string of the list with round brackets
    """
    string = "("
    for element in list:
        string += str(element) + ", "
    # string[:-2] for cutting off the last ", " of last element.
    return string[:-2] + ")"


def check_mat(matr):
    """ Function check_mat gets an matrix, and print the
        elements that are bigger than there neighbors, and returns there amount
    """
    # declare an string that will be warped around the matrix to ease the checking
    # process of neighbors.
    wrapper_of_mat = ""
    wrapped_matr = warp_perimeter_of_matrix(matr, wrapper_of_mat)
    # counts number of element that are bigger.
    counter = 0

    # runs on rows(without first and last row that holds the wrapper).
    for i in range(1, len(wrapped_matr) - 1):
        # runs on col(without first and last col that holds the wrapper).
        for j in range(1, len(wrapped_matr[i]) - 1):
            # checking in case it's not a square matrix
            if wrapped_matr[i][j] == wrapper_of_mat:
                continue
            list_of_neigh = get_neighbors(wrapped_matr, i, j)
            list_of_real_neigh = remove_non_real_neigh(list_of_neigh, wrapper_of_mat)
            # checking if the element is bigger than neighbors.
            if wrapped_matr[i][j] > max(list_of_real_neigh):
                counter += 1
                print("%d. matr[%d][%d]=%d > %s" % (
                    counter,
                    i - 1,
                    j - 1,
                    wrapped_matr[i][j],
                    get_str_list_with_round_brackets(list_of_real_neigh)))
    print()
    return counter


def main():
    """ Function main has an hard-codded matrix,
        and prints numbers of element that are bigger than there neighbors.
    """
    mat = [[2, 3, 4, 5, 6],
           [6, 5, 7, 4, 3],
           [3, 4, 9, 8, 2],
           [5, 4, 8, 7, 6],
           [1, 2, 9, 5, 9]]
    print("count =", check_mat(mat))


main()
