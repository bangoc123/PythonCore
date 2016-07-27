class Animal:
	def sounding(self):
		pass

class Tiger(Animal):
	def __init__(self):
		self.sound = "Grrr"
	def sounding(self):
		return self.sound

class Elephant(Animal):
	def __init__(self):
		self.sound = "bbbpppphhhhfff"
	def sounding(self):
		return self.sound

class Cat(Animal):
	def __init__(self):
		self.sound = "Meow"
	def sounding(self):
		return self.sound

class Rabbit(Animal):
	def __init__(self):
		self.sound = "Purring"
	def sounding(self):
		return self.sound

class Dog(Animal):
	def __init__(self):
		self.sound = "Woof"
	def sounding(self):
		return self.sound


smallTiger = Tiger()
smallElephant = Elephant()
smallCat = Cat()
smallRabbit = Rabbit()
smallDog = Dog()

animals = [smallTiger, smallElephant, smallCat, smallRabbit, smallDog]

for animal in animals:
	print(animal.sounding())

