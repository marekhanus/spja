from enum import Enum


class CellState(Enum):
    """
    Represents the state of a cell in the game.
    """
    Empty = 0
    Cross = 1
    Circle = 2


class Game(object):
    def __init__(self, dimension):
        self.dimension = dimension
        self.active_player = 0  # starting player is Player 0 with Cross

        """
        TODO: create a representation of the game board (grid with dimension * dimension cells).
        Initially all the cells should be empty.
        """

    def get_cell_state(self, row, column):
        """
        Return the CellState of the cell located at row `row` and column `col`.
        """
        pass

    def move(self, row, column):
        """
        Perform a move for the current active player at (row, column).
        Return a tuple (valid_move, winner).

        If the (row, column) is outside of the game board or its cell is not empty, valid_move should be False and
        the game state shouldn't change. Else valid_move should be True and you should switch the active player.

        If the move resulted in the win of the current player, winner should be the value of the current player (0/1).
        If a win didn't happen, winner should be None.

        Example:
            game.move(-1, -1) # (False, None)
            game.move(1, 1)   # (True, None)
            game.move(1, 1)   # (False, None)
            ...
            # the next move causes player 1 to win
            game.move(2, 3)   # (True, 1)
        """
        pass
