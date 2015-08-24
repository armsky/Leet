"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cell
s are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. 
Only the filled cells need to be validated.
"""

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        #turn board into a 2D list
        new_board = []
        for oneRow in board:
            oneRowList = list(oneRow)
            new_board.append(oneRowList)

        #validate each row
        for row in new_board:
            temp = []
            for char in row:
                if char != '.':
                    if char not in temp:
                        temp.append(char)
                    else:
                        return False

        #validate each column
        for col in range(9):
            temp = []
            for row in range(9):
                if new_board[row][col] != '.':
                    if new_board[row][col] not in temp:
                        temp.append(new_board[row][col])
                    else:
                        return False

        #calidate each sub-box
        for i in [0,3,6]:
            for j in [0,3,6]:
                temp = []
                for row in range(3):
                    for col in range(3):
                        print row+i, col+j
                        if  new_board[row+i][col+j] != '.':
                            if new_board[row+i][col+j] not in temp:
                                temp.append(new_board[row+i][col+j])
                            else:
                                return False
                print temp
                print "+++++++++++++++"
        return True

board = ["....5..1.",".4.3.....",".....3..1",
        "8......2.","..2.7....",".15......",
        ".....2...",".2.9.....","..4......"]
solution = Solution()
print solution.isValidSudoku(board)

