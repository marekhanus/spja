import sys

from PySide2.QtCore import Signal
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import QApplication, QVBoxLayout, QWidget

from game import Game, CellState

"""
5 points

Implement the Tic-tac-toe game (Piškvorky) for two players.
1) Implement the game logic inside the Game class in game.py.
2) Render a game board with a grid where the players will click and play the game.
3) After a click to a cell, check if its empty and render the Czech flag (if the active player has the cross mark)
or the Japan flag (if the active player has the circle mark).
Do not use bitmap images for the flags, draw them using QPainter.

After a move, check if the current active player has won. If so (5 or more of his mark in a row/column/diagonal),
print it and exit the game. If not, switch the current active player.
The first player should be Player 0 with the cross mark.
4) Add a label that will show the current active player.
5) Add a "Reset game" button that will reset the game state to the beginning (erase all moves and set active player
to Player 0).

Hint:
Check the TODOs in the code.
Documentation: https://srinikom.github.io/pyside-docs/PySide/QtGui/index.html
Google keywords: python qt5

After the game state changes, you should redraw the UI widgets (active player label and game board).
Use the method repaint() on the game board and setText() on the label to change its text.

1 point (bonus)
Implement some form of AI to play against you.
It can be done with simple pattern matching and prioritized rules (if I have 3 in a row, add fourth etc.).
"""


class GameBoard(QWidget):
    # signal that should be emitted after a player clicks on a cell
    # self.slotClicked.emit(x, y)
    slotClicked = Signal(int, int)

    def __init__(self, width, dimension, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set dimension to (width, width)
        self.setFixedSize(width, width)

        """
        `dimension` - how many cells should be in a row (total number of cells will be dimension * dimension)
        `width` - actual width of the game board

        Therefore each cell should take `width / dimension` pixels.
        """

    def paintEvent(self, *args, **kwargs):
        """
        This method is called automatically when the widget should be drawn.
        It should draw the whole UI for this widget, the previous draw state is discarded.
        """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        """
        TODO: paint the game board state here with `painter`.
        Use the painter method to actually draw the board, do not represent the cells with separate widgets
        (e.g. buttons).
        """

    def mousePressEvent(self, event):
        """
        This method is called automatically after the user clicks on this widget.
        """
        mouse_x = event.x()
        mouse_y = event.y()

        """
        TODO: calculate the cell position from the mouse (x, y) coordinates.
        Check if the click is valid (inside bounds and on an empty cell) and if it is valid, emit the slotClicked
        signal.
        """


class TicTacToe(QWidget):
    def __init__(self, dimension, width, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Piškvorky")

        """
        TODO: create an instance of the Game.
        """

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        """
        TODO: create a label with the active player, reset game button and instance of the game board
        and add them to the layout.
        Pass their events (clicked event on the button and slotClicked event on the game board) to the game instance.
        """


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # create a game with 10x10 Tic-tac-toe grid that has width and height 600px
    tictactoe = TicTacToe(10, 600)
    tictactoe.show()
    sys.exit(app.exec_())
