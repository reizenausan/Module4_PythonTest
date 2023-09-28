import math
import unittest

def test_sqrt():
	num = 25 
	assert math.sqrt(num) == 5

def test_square():
	num = 7
	assert 7*7 == 49

def check(test_sqrt, test_square):
	return check

class checkFunction(unittest.TestCase):

	def test(self):
		self.assertTrue(check(test_square, test_sqrt))

if __name__=='__main__':
	unittest.main()