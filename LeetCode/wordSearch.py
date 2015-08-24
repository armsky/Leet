"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if not word:
            return True
        if not board:
            return False
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.check(board, word, i, j):
                    return True
        return False

    def check(self, board, word, i, j):
        if board[i][j] == word[0]:
            # If iterated all chars in word
            if not word[1:]:
                return True
            # Mark board[i][j] as used
            board[i][j] = " "
            if i > 0 and self.check(board, word[1:], i-1, j):
                return True
            elif i + 1 < len(board) and self.check(board, word[1:], i+1, j):
                return True
            elif j > 0 and self.check(board, word[1:], i, j-1):
                return True
            elif j + 1 < len(board[0]) and self.check(board, word[1:], i, j+1):
                return True
            # change it back
            board[i][j] = word[0]
            return False
        else:
            return False
