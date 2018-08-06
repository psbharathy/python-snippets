# Propery

class Celsius:
	minimum_temp = -273
	def __init__(self, temperature):
	    self.temperature = temperature

	def to_fahrenheit(self):
		return (self.temperature * 1.8) + 32

	def get_temperature(self):
		print('Getting Value')
		return self._temperature

	def set_temperature(self, value):
		if value < self.minimum_temp :
			raise ValueError('Temperature below ', self.minimum_temp , 'is not possible')
		print('Setting Value')
		self._temperature = value;

	temperature = property(get_temperature,set_temperature)
c = Celsius(float(input('Enter the temperature: ')))

print(c.temperature)
# print(c.to_fahrenheit())