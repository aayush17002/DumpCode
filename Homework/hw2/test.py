import unittest
from hw2 import game1
from hw2 import game2
from hw2 import game3 
from hw2 import validmove 
from hw2 import win 
from hw2 import game
from hw2 import validBoard 
from hw2 import takeNaiveMove
from hw2 import takeStrategicMove

# TEST cases should cover the different boundary cases.

class testpoint(unittest.TestCase):
	def test_game1(self):
		self.assertAlmostEqual(game1(),0.5,delta=0.5)
	def test_game2(self):
		self.assertAlmostEqual(game2(),0.25,delta=0.5)
	def test_game3(self):
		self.assertAlmostEqual(game3(),0.0,delta=0.5)
	def test_validmove(self):
		self.assertFalse(validmove(1))
		self.assertFalse(validmove(2))
		self.assertFalse(validmove(3))
		self.assertFalse(validmove(4))
		self.assertFalse(validmove(5))
		self.assertFalse(validmove(6))
		self.assertFalse(validmove(7))
		self.assertFalse(validmove(8))
	def test_win(self):
		self.assertAlmostEqual(win(),1,delta=1)
	def test_game(self):
		self.assertAlmostEqual(game(1),1,delta=1)
		self.assertAlmostEqual(game(2),1,delta=1)
		self.assertAlmostEqual(game(3),1,delta=1)
	def test_validBoard(self):
		self.assertFalse(validBoard(1))
		self.assertFalse(validBoard(2))
	def test_takeNaiveMove(self):
		self.assertAlmostEqual(takeNaiveMove(1),None)
		self.assertAlmostEqual(takeNaiveMove(2),None)
	def test_takeStrategicMove(self):
		self.assertAlmostEqual(takeStrategicMove(1),None)
		self.assertAlmostEqual(takeStrategicMove(2),None)

if __name__=='__main__':
	unittest.main()