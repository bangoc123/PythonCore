import random

class Car:
	def __init__(self, name):
		self.name = name
		self.numberOfWheels = 4

	def canMoveOnTheRoad(self):
		print("%s can move on the road by its %s wheels" %(self.name, self.numberOfWheels))

class Canoe:
	def __init__(self, name):
		self.name = name
	def canMoveOnTheRiver(self):
		print("%s can move on the river" %(self.name))		

car1 = Car("Mercedes")
car1.canMoveOnTheRoad()

canoe1 = Canoe("Cano")
canoe1.canMoveOnTheRiver()

class Amphibian(Car, Canoe):
	def __init__(self, fatherName, motherName):
		self.name = "%s - %s"%(fatherName, motherName)
		self.numberOfWheels = 4

amphibian1 = Amphibian("Mercedes","Cano")
amphibian1.canMoveOnTheRoad()
amphibian1.canMoveOnTheRiver()

