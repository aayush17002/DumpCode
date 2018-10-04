"""Aayush Gupta 
2017002
5/10/2017"""

import unittest
from fin import lis
from fin import Dijkstra
from fin import bfs 

# TEST cases should cover the different boundary cases.

class testpoint(unittest.TestCase):
	def test_Dijkstra(self):
		w=[[[1,5],[2,3]],[[3,3]],[[1,2],[3,5],[4,6]],[],[[3,1]]]
		self.assertEqual(Dijkstra(w,0),[0,5,3,8,9])
		self.assertEqual(Dijkstra(w,1),['inf', 0, 'inf', 3, 'inf'])
		self.assertEqual(Dijkstra(w,2),['inf', 2, 0, 5, 6])
		self.assertEqual(Dijkstra(w,3),['inf', 'inf', 'inf', 0, 'inf'])
		self.assertEqual(Dijkstra(w,4),['inf', 'inf', 'inf', 1, 0])

	def test_bfs(self):
		w=[[[1,5],[2,3]],[[3,3]],[[1,2],[3,5],[4,6]],[],[[3,1]]]
		self.assertEqual(bfs(w,0),([0, 2, 1, 3, 4], [0, 3, 5, 8, 9]))
		self.assertEqual(bfs(w,1),([1, 3], [0, 3]))
		self.assertEqual(bfs(w,2),([2, 1, 3, 4], [0, 2, 5, 6]))
		self.assertEqual(bfs(w,3),([3], [0]))
		self.assertEqual(bfs(w,4),([4, 3], [0, 1]))

	def test_unit_weight(self):
		w=[[[1,1],[2,1]],[[3,1]],[[1,1],[3,1],[4,1]],[],[[3,1]]]
		self.assertEqual(Dijkstra(w,0),[0, 1, 1, 2, 2])
		self.assertEqual(Dijkstra(w,1),['inf', 0, 'inf', 1, 'inf'])
		self.assertEqual(Dijkstra(w,2),['inf', 1, 0, 1, 1])
		self.assertEqual(Dijkstra(w,3),['inf', 'inf', 'inf', 0, 'inf'])
		self.assertEqual(Dijkstra(w,4),['inf', 'inf', 'inf', 1, 0])
		self.assertEqual(bfs(w,0),([0,1,2, 3, 4], [0, 1, 1, 2, 2]))
		self.assertEqual(bfs(w,1),([1, 3], [0, 1]))
		self.assertEqual(bfs(w,2),([2, 1, 3, 4], [0, 1, 1, 1]))
		self.assertEqual(bfs(w,3),([3], [0]))
		self.assertEqual(bfs(w,4),([4, 3], [0, 1]))

	# you can not tell what the user will input so we can't possibly chech that.
	def test_lis(self):
		w=[[[1,5],[2,3]],[[3,3]],[[1,2],[3,5],[4,6]],[],[[3,1]]]
		self.assertEqual(lis(5),w)




if __name__=='__main__':
	unittest.main()