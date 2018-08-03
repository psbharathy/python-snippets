import sys

# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass

class StringError(Error):
	"""Raised when the input value is String"""
	pass

class DivideByZeroError(Error):
	"""Raised when the input value is 0 zero"""
	pass

# This is Try catch Class
class tryCatch:
	"""This is Try catch Class"""
	def __init__(self, randomList):
		"""Constructor"""
		self.rdL = randomList
		self._count = 4

	
	def reciporcal(self):
		"""This is reciporcal method"""
		print('Reciporcal Array', self.rdL)
		for entry in self.rdL:
			try:
				print('Entry is ', entry)
				if(isinstance(entry, str)):
					raise StringError
				elif(entry == 0):
					raise DivideByZeroError
				else:
					r = 1/int(entry)
					print("The reciporcal of", entry, "is ", round(r, 2))
					print()
			except StringError:
				print("This value is String, try again!")
				print()
			except DivideByZeroError:
				print("This value is Zero, try again!")
				print()

	def setCount(self, count):
		"sets private value of this class"
		self._count = count

	def printCount(self):
		'Print the _count value'
		print("Total Count is {}", self._count)
		
# Trigger class

tc = tryCatch(['a', 0, 3, 6, 10, 12])
tc.__count =5;
tc.printCount()

tc.__count =25;
tc.printCount()

tc.setCount(50);
tc.printCount()

print(tc.__doc__)
print(tc.reciporcal.__doc__)
# print(tc.printCount.__doc__)

tc.reciporcal()