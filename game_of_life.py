import random
from itertools import product

class Universe:
    def __init__(self, n, board):
        self.n = n
        if board:
            self.board = board
        else:
            self.board = self._init_board()
            
    def _init_board(self):
        return [[random.randint(0, 1) for _  in range(self.n)] for _  in range(self.n)]
    
    def _count_neighbours(self, row: int, col: int) -> int:
        return sum(self.board[(row + i)%self.n][(col + j)%self.n] for i, j in list(product([0, -1, 1], [0, -1, 1]))[1:])
    
    def next_position(self, row, col):
        position = row*self.n+col+1
        return position//self.n, position%self.n
                
    def evolve(self):
        next_generation, row, col = [[0]*self.n for _  in range(self.n)], 0, 0
        while (row, col ) != (self.n-1, self.n-1):
            neighbours = self._count_neighbours(row, col)
            next_generation[row][col] = int((self.board[row][col] and neighbours == 2) or neighbours == 3)
            row, col = self.next_position(row, col)
        self.board = next_generation
    
    def next_coords(self, i, j):
        if i is None:
            yield 0, 0
        position = i*self.n+j+1
        yield position//self.n, position%self.n
        

'''
def main():
    new_game = Universe(5)
    for _ in range(5):
        new_game.evolve()
        print(new_game.board)

if __name__ == "__main__":
    main()
'''
import unittest

class Testing(unittest.TestCase):
    def test1(self):
        board1 = [[0]*5, [0]*5, [0, 1, 1, 1, 0], [0]*5, [0]*5]
        result1 = [[0]*5, [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0]*5]
        game1 = Universe(len(board1), board1)
        game1.evolve()
        self.assertEqual(game1.board, result1)
        game1.evolve()
        self.assertEquals(game1.board, board1)