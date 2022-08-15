game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

print("   0, 1, 2")


def game_board(value, g_row, g_column):
    game[g_row][g_column] = value
    for row, col in enumerate(game):
        print(row, col)


game_board(1, 0, 0)
