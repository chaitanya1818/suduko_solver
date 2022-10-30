board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve_board(bo):
    find_empty_pos = find_empty_square(bo)
    if not find_empty_pos:
        return True
    else:
        row, col = find_empty_pos

    for i in range(1, 10):
        if check_valid_position(bo, i, (row, col)):
            bo[row][col] = i

            if solve_board(bo):
                return True

            bo[row][col] = 0
    return False


def check_valid_position(bo, num, pos):
    # check the row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # check the column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check the box
    box_X = pos[0] // 3
    box_Y = pos[1] // 3

    for i in range(box_X * 3, box_X * 3 + 3):
        for j in range(box_Y * 3, box_Y * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_suduko_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" |  ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty_square(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j
    return None


print_suduko_board(board)
solve_board(board)
print("-----------------------------------")
print_suduko_board(board)
