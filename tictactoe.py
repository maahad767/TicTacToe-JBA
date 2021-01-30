def main():
    # get user input
    game_played = "_________"
    game_matrix = [
        [cell for cell in game_played[:3]],
        [cell for cell in game_played[3:6]],
        [cell for cell in game_played[6:]],
        ]
    print_game(game_matrix)
    player = 'X'
    while not is_finished(game_matrix):
        user_move(game_matrix, player)
        print_game(game_matrix)
        status = game_status(game_matrix, player)
        if status is not None:
            print(status)
            break
        player = alter_player(player)


def alter_player(player):
    if player == 'X':
        return 'O'
    return 'X'


def print_game(game):
    print("---------")
    for row in game:
        print("| " + " ".join(row) + " |")
    print("---------")


def is_row_winner(game, player):
    wins = True
    for row in game:
        for cell in row:
            if cell != player:
                wins = False
                break
        if wins:
            return True
        else:
            wins = True
    return False


def is_col_winner(game, player):
    wins = True
    for row in range(len(game)):
        for col in range(len(game)):
            if game[col][row] != player:
                wins = False
                break
        if wins:
            return True
        else:
            wins = True

    return False


def is_diagonal_winner(game, player):
    if player == game[0][0] == game[1][1] == game[2][2]:
        return True
    if player == game[0][2] == game[1][1] == game[2][0]:
        return True
    return False


def is_winner(game, player):
    return is_row_winner(game, player) or is_col_winner(game, player) or is_diagonal_winner(game, player)


def is_finished(game):
    for row in game:
        for col in row:
            if col == '_':
                return False
    return True


def is_impossible(game):
    count_x, count_y = 0, 0

    for row in game:
        for col in row:
            if col == 'X':
                count_x += 1
            elif col == 'O':
                count_y += 1
    return abs(count_x - count_y) > 1


def game_status(game, player):
    if is_winner(game, player):
        return f'{player} wins'
    elif is_finished(game):
        return 'Draw'


def take_coordinates():
    coordinates = input('Enter the coordinates:').split()
    try:
        x, y = int(coordinates[0]), int(coordinates[1])
    except ValueError:
        print('You should enter numbers!')
        return take_coordinates()

    while not (1 <= x <= 3 and 1 <= y <= 3):
        print('Coordinates should be from 1 to 3!')
        coordinates = input('Enter the coordinates:').split()
        try:
            x, y = int(coordinates[0]), int(coordinates[1])
        except ValueError:
            print('You should enter numbers!')
            return take_coordinates()

    return x - 1, y - 1


def user_move(game, player):
    x, y = take_coordinates()
    while game[x][y] != '_':
        print('This cell is occupied! Choose another one!')
        x, y = take_coordinates()
    game[x][y] = player


if __name__ == '__main__':
    main()
