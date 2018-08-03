import sys

class Polygon:
	def __init__(self, no_of_sides):
		'Parent Construct'
		self.n = no_of_sides
		self.sides = [0 for i in range(no_of_sides)]

	def inputSides(self):
		self.sides = [float(input('Enter the side # '+ str(i+1) +': ')) for i in range(self.n) ]

	def printArea(self, areaType):
		print(areaType,'area is',self.area)


class Square(Polygon):
	'Sqaure Parent'
	
	def __init__(self):
		Polygon.__init__(self, 1)	

	def findArea(self):
		a = self.sides[0]
		Polygon.area = a * a

class Rectangle(Polygon):
	'Rectangle Parent'
	
	def __init__(self):
		Polygon.__init__(self, 2)	

	def findArea(self):
		w, h = self.sides
		Polygon.area = w * h

class Triangle(Polygon):
	'Triangle Parent'
	
	def __init__(self):
		Polygon.__init__(self, 2)	

	def findArea(self):
		b, h = self.sides
		Polygon.area = (b * h) * 0.5


# Find The Square Area
s = Square()
s.inputSides()
s.findArea()
s.printArea('Square')
print(isinstance(s, Square))
print(isinstance(s, Rectangle))

# Find The Rectangle Area
r = Rectangle();
r.inputSides();
r.findArea();
r.printArea('Rectangle');
print(issubclass(Polygon, Rectangle))

# Find The Rectangle Area
t = Triangle();
t.inputSides();
t.findArea();
t.printArea('Triangle');
print(issubclass(Polygon, Triangle))
