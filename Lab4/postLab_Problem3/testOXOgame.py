import cmd, oxo_ui, oxo_logic
import unittest

class testOXO(unittest.TestCase):
    def test_newGame(self):
        gameTest = oxo_logic.newGame()
        self.assertEqual(gameTest, list(" " * 9))
    
    def test_printing(self):
        gameTest = ['X',' ','O','O',' ','X','O','X',' ']
        displayTest = '''
            1 | 2 | 3      {} | {} | {}
           ----------     -----------
            4 | 5 | 6      {} | {} | {}
            ---------     -----------
            7 | 8 | 9      {} | {} | {}
            '''
        expectedPrint = '''
            1 | 2 | 3      X |   | O
           ----------     -----------
            4 | 5 | 6      O |   | X
            ---------     -----------
            7 | 8 | 9      O | X |  
            '''
        self.assertEqual(displayTest.format(*gameTest), expectedPrint)

    def test_winLoseCon(self):
        wins = ((0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6))

        for a,b,c in wins:
            gameTest = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            gameTest[a] = 'X'
            gameTest[b] = 'X'
            gameTest[c] = 'X'
            self.assertTrue(oxo_logic._isWinningMove(gameTest))
            gameTest[a] = 'O'
            gameTest[b] = 'O'
            gameTest[c] = 'O'
            self.assertTrue(oxo_logic._isWinningMove(gameTest))
        
    def test_drawCondition(self):
        '''Since User Always Goes First, User Always does the last move
        Computer therefore will check if there is anything left'''
        gameTest = ['X','O','O','O','X','X','O','X','O']
        self.assertEqual(oxo_logic.computerMove(gameTest),'D')

    def test_moveGen(self):
        gameTest1 = ['X','O','O','O','X','X',' ','X','O']
        gameTest2 = ['X','O','O','O','X','X','O','X','O']
        self.assertEqual(oxo_logic._generateMove(gameTest1),6)
        self.assertEqual(oxo_logic._generateMove(gameTest2),-1)

if __name__ == '__main__':
    unittest.main()