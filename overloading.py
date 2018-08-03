import sys

class Point:
	"""docstring for ClassName"""
	def __init__(self, a = 0, b = 0):
		self.a = a
		self.b = b

	def __str__(self):
		return "({0},{1})".format(self.a, self.b)

	def __add__(self, other):
		x = self.a + other.a
		y = self.b + other.b
		return Point(x,y)
	def itr(self):
		my_list = [4,5,2,6]
		my_itr = iter(my_list)
		while True:
			try:
				print(next(my_itr))
			except StopIteration: 
				print('EoD of Itr')
				break
				

# Step One 
p1 = Point(1,2)
p2 = Point(3,4)
p3 = p1+ p2
#Traceback (most recent call last):
#   File "overloading.py", line 13, in <module>
#     p3 = p1+ p2
# TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
p1.itr();
# print(p3)

