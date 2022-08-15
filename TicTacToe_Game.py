import itertools


def game_board(input_Game, value=0, g_row=0, g_column=0, just_Display=False):
    try:
        if input_Game[g_row][g_column] != 0:
            print("Pos is already occupied! Choose another")
            return input_Game, False
        print("   0, 1, 2")
        if not just_Display:
            input_Game[g_row][g_column] = value
        for row, col in enumerate(input_Game):
            print(row, col)
        return input_Game, True
    except IndexError as e:
        print("Error: Make sure to enter row/column between 0, 1 or 2 ?", e)
        return input_Game, False
    except Exception as e:
        print("Unexpected error occur-ed", e)
        return input_Game, False


def win(current_Game):
    if win_h(current_Game):
        return True
    elif win_v(current_Game):
        return True
    elif win_h0(current_Game):
        return True
    elif win_h1(current_Game):
        return True
    else:
        return False


def win_h(current_Game):
    for row in current_Game:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("Player", row[0], "Won!!, with Horizontal lines (-)")
            return True
        else:
            return False


def win_v(current_Game):
    for col in range(0, len(current_Game)):
        check = []
        for row in current_Game:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print("Player", row[0], "Won!!, with Vertical(|)")
            return True
        else:
            return False


def win_h0(current_game):
    diags = []
    row_ = list(range(len(current_game)))
    col_ = list(range(len(current_game)))

    for row, col in zip(row_, col_):
        diags.append(current_game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print("Player", diags[0], "Won!!, with Diagonal(\\)")
        return True
    else:
        return False


def win_h1(current_game):
    diags = []
    row_ = list(range(len(current_game)))
    col_ = list(reversed(range(len(current_game))))

    for row, col in zip(row_, col_):
        diags.append(current_game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print("Player", diags[0], "Won!!, with Diagonal(/)")
        return True
    else:
        return False


play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won = False
    game, _ = game_board(game, 0, 0, just_Display=True)
    player_choice = itertools.cycle([1, 2])

    while not game_won:
        current_player = next(player_choice)
        print("Current player is: ", current_player)
        played = False

        while not played:
            row_Choice = int(input("Enter desired row to play from (0, 1, 2): "))
            column_Choice = int(input("Enter desired column to play from (0, 1, 2): "))
            game, played = game_board(game, current_player, row_Choice, column_Choice, just_Display=False)

            if win(game):
                game_won = True
                again = input("The game is Over, would you like to replay? (y/n) ")
                if again.lower() == 'y':
                    print("Restarting fresh game")
                    Play = True
                elif again.lower() == 'n':
                    print("Good bye!!!")
                    play = False
                else:
                    print("Not a Valid answer! Bye")
                    play = False


