import math

class Circle:
	radius = 1
	def __init__(self, newRadius):
		self.radius = newRadius
	def getArea(self):
		return self.radius * self.radius * math.pi
	def getPerimeter(self):
		return 2*radius*math.pi
