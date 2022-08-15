game = [[1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]]


def game_board(input_Game, value=0, g_row=0, g_column=0, just_Display=False):
    try:
        print("   0, 1, 2")
        if not just_Display:
            input_Game[g_row][g_column] = value
        for row, col in enumerate(input_Game):
            print(row, col)
        return input_Game
    except IndexError as e:
        print("Error: Make sure to enter row/column between 0, 1 or 2 ?", e)
    except Exception as e:
        print("Unexpected error occur-ed", e)

def win(current_Game):
    win_h(current_Game)
    win_v(current_Game)
    win_h0(current_Game)
    win_h1(current_Game)

def win_h(current_Game):
    for row in current_Game:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("Player", row[0], "Won!!, with Horizontal lines (-)")


def win_v(current_Game):
    for col in range(0, len(current_Game)):
        check = []
        for row in current_Game:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print("Player", row[0], "Won!!, with Vertical(|)")

def win_h0(current_game):
    diags = []
    row_ = list(range(len(current_game)))
    col_ = list(range(len(current_game)))

    for row, col in zip(row_, col_):
        diags.append(current_game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
       print("Player", diags[0], "Won!!, with Diagonal(\\)")


def win_h1(current_game):
    diags = []
    row_ = list(range(len(current_game)))
    col_ = list(reversed(range(len(current_game))))

    for row, col in zip(row_, col_):
        diags.append(current_game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print("Player", diags[0], "Won!!, with Diagonal(/)")


#game = game_board(game, 1, 2, 0, False)


win(game)
