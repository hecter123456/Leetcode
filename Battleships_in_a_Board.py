import unittest

class unitest(unittest.TestCase):
    def testRow(self):
        board = ["XXX"]
        self.assertEqual(Solution.countBattleships(self,board),1);
    def testColumu(self):
        board = ["X","X","X"]
        self.assertEqual(Solution.countBattleships(self,board),1);

class Solution():
    def countBattleships(self,board):
        battleship = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                    battleship+=1
        return battleship

if __name__ == '__main__':
    unittest.main()
