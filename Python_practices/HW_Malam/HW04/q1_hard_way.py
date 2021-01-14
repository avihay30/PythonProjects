def check_square(matrix, r, c):
    square_list = [matrix[r - 1][c - 1],
                   matrix[r - 1][c],
                   matrix[r - 1][c + 1],
                   matrix[r][c - 1],
                   matrix[r][c + 1],
                   matrix[r + 1][c - 1],
                   matrix[r + 1][c],
                   matrix[r + 1][c + 1]]
    return square_list if matrix[r][c] > max(square_list) else False


def create_edge_neighbors(matrix):
    edge_mat = [[matrix[0][1], matrix[1][0], matrix[1][1]],
                [matrix[0][-2], matrix[1][-2], matrix[1][-1]],
                [matrix[-2][0], matrix[-2][1], matrix[-1][1]],
                [matrix[-2][-2], matrix[-2][-1], matrix[-1][-2]]]
    return edge_mat


def get_edge_number(i, j):
    # upper left edge
    edge_number = 0
    if i == j:
        # lower right edge
        if not i == 0:
            edge_number = 3
    else:
        # upper right edge
        if i == 0:
            edge_number = 1
        # lower left edge
        else:
            edge_number = 2
    return edge_number


def check_middles_frame(mat, i, j):
    if i == 0 or i == len(mat) - 1:
        if i == 0:
            delta = 1
        else:
            delta = -1
        list_neigh = [mat[i][j - 1],
                      mat[i][j + 1],
                      mat[i + delta][j - 1],
                      mat[i + delta][j],
                      mat[i + delta][j + 1]]
    # cols
    else:
        if j == 0:
            delta = 1
        else:
            delta = -1
        list_neigh = [mat[i - 1][j],
                      mat[i + 1][j],
                      mat[i - 1][j + delta],
                      mat[i][j + delta],
                      mat[i + 1][j + delta]]
    return list_neigh


def check_mat(matr):
    counter = 0
    edge_matrix = create_edge_neighbors(matr)
    # iterate on rows
    for i in range(len(matr)):
        # iterate on cols
        for j in range(len(matr[i])):
            # if not first/last row.
            # if not first/last col.
            if (0 < i < len(matr) - 1) and (0 < j < len(matr[i]) - 1):
                checked_list = check_square(matr, i, j)
                if checked_list:
                    counter += 1
                    print("%d. wrapped_matr[%d][%d]=%d > %s" % (counter, i, j, matr[i][j], checked_list))
            # if on edges(checks for diagonal, anti-diagonal).
            elif i == j or (len(matr[i]) - i - 1 == j):
                edge_neig = edge_matrix[get_edge_number(i, j)]
                is_point_big = matr[i][j] > max(edge_neig)
                if is_point_big:
                    counter += 1
                    print("%d. wrapped_matr[%d][%d]=%d > %s" % (counter, i, j, matr[i][j], edge_neig))
            # on middle frame
            else:
                frame_nigh = check_middles_frame(matr, i, j)
                is_big = matr[i][j] > max(frame_nigh)
                if is_big:
                    counter += 1
                    print("%d. wrapped_matr[%d][%d]=%d > %s" % (counter, i, j, matr[i][j], frame_nigh))
    return counter


def main():
    mat = [[2, 3, 4, 5, 6],
           [6, 5, 7, 4, 3],
           [3, 4, 9, 8, 2],
           [5, 4, 8, 7, 6],
           [1, 2, 9, 5, 9]]
    print("count =", check_mat(mat))


main()
