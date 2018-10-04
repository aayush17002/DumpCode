#Made by :- Aayush Gupta 2017002
import unittest
from a4 import RREFMatrix
from a4 import MatrixRank
from a4 import swapRows
from a4 import Row_Transformation

# TEST cases should cover the different boundary cases.

class testpoint(unittest.TestCase):

	def test_swapRows(self):

		matrix1=[[1,2,3],[4,5,6],[7,8,9]]
		swapRows(matrix1,1,2)
		self.assertEqual(matrix1,[[1,2,3],[7,8,9],[4,5,6]])

		matrix2=[[10,20,10,11],[0,40,20,12],[0,50,0,13],[0,20,10,11]]
		swapRows(matrix2,1,2)
		self.assertEqual(matrix2,[[10,20,10,11],[0,50,0,13],[0,40,20,12],[0,20,10,11]])

		matrix3=[[10,20,10],[20,40,20],[30,50,0],[0,20,10]]
		swapRows(matrix3,3,2)
		self.assertEqual(matrix3,[[10,20,10],[20,40,20],[0,20,10],[30,50,0]])

		matrix4=[[1,0,0],[2,1,0],[3,2,1],[4,3,2],[5,4,3]]
		swapRows(matrix4,4,2)
		self.assertEqual(matrix4,[[1,0,0],[2,1,0],[5,4,3],[4,3,2],[3,2,1]])

		matrix5=[[0,2,4,6,8,10,12,14,16],[1,3,5,7,9,11,13,15,17],[0,1,2,3,4,5,6,7,8],[99,98,97,96,95,94,93,92,91],[11,22,33,44,55,66,77,88,99]]
		swapRows(matrix5,3,2)
		self.assertEqual(matrix5,[[0,2,4,6,8,10,12,14,16],[1,3,5,7,9,11,13,15,17],[99,98,97,96,95,94,93,92,91],[0,1,2,3,4,5,6,7,8],[11,22,33,44,55,66,77,88,99]])


	def test_Row_Transformation(self):

		matrix1=[[1,2,3],[4,5,6],[7,8,9]]
		Row_Transformation(matrix1,2,1,2)
		self.assertEqual(matrix1,[[1,2,3],[4,5,6],[-1,-2,-3]])

		matrix2=[[10,20,10,11],[0,40,20,12],[0,50,0,13],[0,20,10,11]]
		Row_Transformation(matrix2,2,1,2)
		self.assertEqual(matrix2,[[10,20,10,11],[0,40,20,12],[0,-30,-40,-11],[0,20,10,11]])

		matrix3=[[10,20,10],[20,40,20],[30,50,0],[0,20,10]]
		Row_Transformation(matrix3,2,1,2)
		self.assertEqual(matrix3,[[10,20,10],[20,40,20],[-10,-30,-40],[0,20,10]])

		matrix4=[[1,0,0],[2,1,0],[3,2,1],[4,3,2],[5,4,3]]
		Row_Transformation(matrix4,5,1,2)
		self.assertEqual(matrix4,[[1,0,0],[2,1,0],[-7,-3,1],[4,3,2],[5,4,3]])

		matrix5=[[0,2,4,6,8,10,12,14,16],[1,3,5,7,9,11,13,15,17],[0,1,2,3,4,5,6,7,8],[99,98,97,96,95,94,93,92,91],[11,22,33,44,55,66,77,88,99]]
		Row_Transformation(matrix5,3,0,2)
		self.assertEqual(matrix5,[[0,2,4,6,8,10,12,14,16],[1,3,5,7,9,11,13,15,17],[0,-5,-10,-15,-20,-25,-30,-35,-40],[99,98,97,96,95,94,93,92,91],[11,22,33,44,55,66,77,88,99]])

	
	def test_MatrixRank(self):
		
		matrix1=[[1,2,3],[4,5,6],[7,8,9]]
		RREFMatrix(matrix1)
		self.assertEqual(MatrixRank(matrix1),2)
		
		matrix2=[[10,20,10,11],[0,40,20,12],[0,50,0,13],[0,20,10,11]]
		RREFMatrix(matrix2)
		self.assertEqual(MatrixRank(matrix2),4)
		
		matrix3=[[10,20,10],[20,40,20],[30,50,0],[0,20,10]]
		RREFMatrix(matrix3)
		self.assertEqual(MatrixRank(matrix3),3)
		
		matrix4=[[2,0,0],[4,1,0],[9,2,0],[2,4,5]]
		RREFMatrix(matrix4)
		self.assertEqual(MatrixRank(matrix4),3)
		
		matrix5=[[3,2,1],[2,0,5]]
		RREFMatrix(matrix5)
		self.assertEqual(MatrixRank(matrix5),2)
		
		matrix6=[[9,4,6],[5,0,2],[0,9,0]]
		RREFMatrix(matrix6)
		self.assertEqual(MatrixRank(matrix6),3)
		
		matrix7=[[0,1,2,4],[5,0,4,9],[0,0,0,6]]
		RREFMatrix(matrix7)
		self.assertEqual(MatrixRank(matrix7),3)

		matrix8=[[1,0,0],[2,1,0],[3,2,1],[4,3,2],[5,4,3]]
		RREFMatrix(matrix8)
		self.assertEqual(MatrixRank(matrix8),3)

		matrix9=[[0,2,4,6,8,10,12,14,16],[1,3,5,7,9,11,13,15,17],[0,1,2,3,4,5,6,7,8],[99,98,97,96,95,94,93,92,91],[11,22,33,44,55,66,77,88,99]]
		RREFMatrix(matrix9)
		self.assertEqual(MatrixRank(matrix9),2)
		

if __name__=='__main__':
	unittest.main()
