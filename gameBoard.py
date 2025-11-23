from abc import ABC, abstractmethod
from typing import Protocol
from Square import Square
from Color import Color

class I_GameBoard(Protocol):
    def getBoard() -> list: ...
    def make_move(start:str,end:str) -> (bool,str): ...
    def getTurn() -> str:...
    def getStatus() -> str:...


class MocGameBoard(ABC, I_GameBoard):
    
    def __init__(self) -> None:
        self.newGame()

    def getBoard(self) -> list:
        return self.board

    def newGame(self):
        self._turn = str(Color.WHITE)
        self.selected = None
        self.board = [
            ['BLACK_Rook', 'BLACK_Knight', 'BLACK_Bishop', 'BLACK_Queen', 
             'BLACK_King', 'BLACK_Bishop', 'BLACK_Knight', 'BLACK_Rook'],
            ['BLACK_Pawn'] * 8,
            [''] * 8,
            [''] * 8,
            [''] * 8,
            [''] * 8,
            ['WHITE_Pawn'] * 8,
            ['WHITE_Rook', 'WHITE_Knight', 'WHITE_Bishop', 'WHITE_Queen',
             'WHITE_King', 'WHITE_Bishop', 'WHITE_Knight', 'WHITE_Rook']
        ]

    def make_move(self,to_square: str) -> (bool, str):
        if self.selected:
            start = self.selected
        else:
            return (False, "Ни чего не выбрано")

        end= Square(to_square)
        self.selected = None

        if start == end :
            return (False,"Нельзя походить на самого себя")

        figure = self.board[start.RowIndex()][start.ColIndex()]
        if figure and figure.split('_')[0] == self._turn :
            if self.board[end.RowIndex()][end.ColIndex()].split('_')[0] == self._turn:
                return (False,"Нельзя сбить свою фигуру")
            else:
                self._turn = str(Color.BLACK) if self._turn == str(Color.WHITE) else str(Color.WHITE)
                self.board[end.RowIndex()][end.ColIndex()] = figure
                self.board[start.RowIndex()][start.ColIndex()] = ''
                return (True,"")


    def getTurn(self) -> str:
        return self._turn

    def getStatus(self) -> str:
        return ""

    def SelectFigure(self, start: str) -> (bool, str):
        square = Square(start)
        figure = self.board[square.RowIndex()][square.ColIndex()]
        if figure and figure.split('_')[0] == self._turn:
            self.selected = square
            return (True,"")
        else:
            return (False,"Нельзя выбрать пустую клетку или чужую фигуру")
    def isSelected(self) -> bool:
        return True if self.selected else False
    def getSelectedIndexes(self) -> (int,int):
        if self.isSelected():
            return (self.selected.RowIndex(), self.selected.ColIndex())