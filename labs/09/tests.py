from game import Game, CellState

ValidMove = (True, None)
InvalidMove = (False, None)


def test_invalid_moves():
    game = Game(3)

    assert game.move(-1, -1) == InvalidMove
    game.move(0, 0)
    assert game.move(0, 0) == InvalidMove

    for col in range(3):
        for row in range(3):
            cell = game.get_cell_state(col, row)
            if row == 0 and col == 0:
                assert cell is CellState.Cross
            else:
                assert cell is CellState.Empty


def test_player_swap():
    game = Game(3)

    assert game.move(0, 0) == ValidMove
    assert game.get_cell_state(0, 0) is CellState.Cross

    assert game.move(0, 1) == ValidMove
    assert game.get_cell_state(0, 1) is CellState.Circle

    assert game.move(0, 2) == ValidMove
    assert game.get_cell_state(0, 2) is CellState.Cross


def test_player_win_horizontal():
    game = Game(6)
    moves_cross = [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4)
    ]
    moves_circle = [
        (1, 0),
        (2, 0),
        (2, 1),
        (2, 2)
    ]

    assert play_game(game, [moves_cross, moves_circle]) == (9, 0)


def test_player_win_vertical():
    game = Game(6)
    moves_cross = [
        (0, 5),
        (1, 5),
        (2, 5),
        (3, 5),
        (4, 5)
    ]
    moves_circle = [
        (1, 0),
        (2, 0),
        (2, 1),
        (2, 2)
    ]

    assert play_game(game, [moves_cross, moves_circle]) == (9, 0)


def test_player_win_diagonal_right():
    game = Game(10)
    moves_cross = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4)
    ]
    moves_circle = [
        (1, 0),
        (2, 0),
        (2, 1),
        (3, 0)
    ]

    assert play_game(game, [moves_cross, moves_circle]) == (9, 0)


def test_player_win_diagonal_left():
    game = Game(10)
    moves_cross = [
        (0, 9),
        (1, 8),
        (2, 7),
        (3, 6),
        (4, 5)
    ]
    moves_circle = [
        (1, 0),
        (2, 0),
        (2, 1),
        (2, 2)
    ]

    assert play_game(game, [moves_cross, moves_circle]) == (9, 0)


def test_player_win_more_than_five():
    game = Game(10)
    moves_cross = [
        (1, 0),
        (2, 0),
        (2, 1),
        (2, 2),
        (3, 0),
        (3, 1)
    ]
    moves_circle = [
        (0, 0),
        (0, 1),
        (0, 3),
        (0, 4),
        (0, 5),
        (0, 2)
    ]

    assert play_game(game, [moves_cross, moves_circle]) == (12, 1)


def play_game(game, moves):
    turn = 0

    while True:
        index = turn % 2

        if not moves[index]:
            # the game took too long
            assert False

        move = moves[index][0]
        moves[index].pop(0)

        valid, winner = game.move(*move)
        assert valid

        turn += 1
        if winner is not None:
            return (turn, winner)

        # game is cycled
        if turn > 1000:
            assert False
