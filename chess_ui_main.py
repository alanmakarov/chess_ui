import tkinter as tk
from gameBoard import I_GameBoard, MocGameBoard

class ChessBoard:
    def __init__(self) -> None:
        pass
    def draw_board(self):
        pass
    def on_square_click(self, event):
        pass
    def on_button_click(self):
        self._gameBoard.newGame()
        self.draw_board()
        self.status_label.config(text="")

    def run(self):
        self.root.mainloop()


chess = ChessBoard()
chess.run()