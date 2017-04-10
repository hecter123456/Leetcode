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
        preboard = set()
        for line in board:
            for idx,slot in enumerate(line):
                if(slot == 'X'):
                    if(idx not in preboard):
                        if(idx-1 not in preboard):
                            battleship+=1
                        preboard.add(idx)
                else:
                    if(idx in preboard):
                        preboard.remove(idx)
        return battleship;

if __name__ == '__main__':
    unittest.main()
