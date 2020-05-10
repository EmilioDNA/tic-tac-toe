# write your code here


def verify_horizontal_lines(board_input, side):
    for i in range(0, len(board_input), 3):
        if board_input[i:i+3].count(side) == 3:
            return True
    return False


def verify_more_sides(board_input):
    if board_input.count('X') - board_input.count('O') >= 2 or board_input.count('O') - board_input.count('X') >= 2:
        return False
    return True


def verify_diagonals(board_input, side):
    left_top_to_right_bottom = board_input[0] + board_input[4] + board_input[8]
    right_top_to_left_bottom = board_input[2] + board_input[4] + board_input[6]
    if left_top_to_right_bottom.count(side) == 3 or right_top_to_left_bottom.count(side) == 3:
        return True
    return False


def verify_vertical_lines(board_input, side):
    left = board_input[0] + board_input[3] + board_input[6]
    middle = board_input[1] + board_input[4] + board_input[7]
    right = board_input[2] + board_input[5] + board_input[8]
    if left.count(side) == 3 or middle.count(side) == 3 or right.count(side) == 3:
        return True
    return False


def verify_game_not_finished(board_input, side):
    if board_input.count(side) < 3:
        return True
    return False
    print(board_input.count('X'))
    print(board_input.count('O'))
    print(board_input.count(' '))


def switch_columns(board_input):
    column_1 = []
    column_2 = []
    column_3 = []
    for i in range(0, len(board_input), 3):
        column_1.append(board_input[i])
        column_2.append(board_input[i + 1])
        column_3.append(board_input[i + 2])
    return [column_1, column_2, column_3]


def extend_rows(board_input):
    complete_row = []
    for row_ in board_input:
        complete_row.extend(row_)
    return complete_row


def convert_matrix_to_string(matrix):
    new_str = ''
    for row_ in matrix:
        new_str += ''.join(row_)
    return new_str


def print_board(list_board):
    print("---------")
    for row in list_board:
        print(f"| {row[0]} {row[1]} {row[2]} |")
    print("---------")


def format_coordinates(x, y):
    new_coordinates = [x - 1, -y]
    return new_coordinates


def eval_coordinates_cycle(move):
    pass_ = True
    while pass_:
        print('Enter the coordinates: ')
        coordinates_str = input().split(' ')
        try:
            coordinates = [int(coordinate) for coordinate in coordinates_str]
        except ValueError:
            print('You should enter numbers!')
            continue
        if coordinates[0] >= 4 or coordinates[1] >= 4:
            print('Coordinates should be from 1 to 3!')
            continue
        new_coord = format_coordinates(coordinates[0], coordinates[1])
        if math_rows[new_coord[0]][new_coord[1]] != ' ':
            print('This cell is occupied! Choose another one!')
            continue
        else:
            math_rows[new_coord[0]][new_coord[1]] = move
        pass_ = False


def eval_game_status(list_board):
    game_status = True
    if verify_more_sides(list_board) != True or (verify_vertical_lines(list_board, 'X') and verify_vertical_lines(list_board, 'O')):
        print("Impossible")
    else:
        if verify_horizontal_lines(list_board, 'X') or verify_diagonals(list_board, 'X') or verify_vertical_lines(list_board, 'X'):
            print('X wins')
            game_status = False
        elif verify_vertical_lines(list_board, 'O') or verify_diagonals(list_board, 'O') or verify_vertical_lines(list_board, 'O'):
            print('O wins')
            game_status = False
        elif list_board.count(' ') == 0:
            print('Draw')
            game_status = False
        else:
            print('Game not finished')
    return game_status

# write your code here
board = '         '
visual_rows = []
for i in range(0, len(board), 3):
    row = []
    row.extend(board[i:i+3])
    visual_rows.append(row)

print_board(visual_rows)

math_rows = switch_columns(convert_matrix_to_string(visual_rows))

current_move = 'X'
next_move = 'O'
while eval_game_status(extend_rows(math_rows)):
    eval_coordinates_cycle(current_move)
    final_board_list = switch_columns(convert_matrix_to_string(math_rows))
    final_board = convert_matrix_to_string(final_board_list)
    final_visual_rows = []
    for i in range(0, len(final_board), 3):
        row = []
        row.extend(final_board[i:i + 3])
        final_visual_rows.append(row)

    print_board(final_visual_rows)
    current_move, next_move = next_move, current_move














