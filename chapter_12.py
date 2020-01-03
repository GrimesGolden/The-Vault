from random import randint
from math import pi

class Orange:
	def __init__(self, w, c):
		self.weight = w
		self.color = c
		self.mold = 0
		print("Created!")

	def peel(self):
		print("The orange is peeled!")

	def rot(self, days, temp):
		self.mold = days * temp
		if self.mold > 200:
			print("Shits fucking ROTTEN dude!")
		else:
			print('Hmm still edible')

class Rectangle():
	def __init__(self, w, l):
		self.width = w
		self.len = l

	def area(self):
		return self.width * self.len

	def perimeter(self):
		return (self.width * 2) + (self.len * 2)

	def change_size(self, w, l):
		self.width = w
		self.len = l

class Apple():
	def __init__(self, c, s, t, size):
		self.color = c
		self.species = s
		self.taste = t
		self.size = size

class Circle():
	def __init__(self, r):
		self.radius = r

	def area(self):
		calc = pi * (self.radius ** 2)
		print("The area is: " + str(calc))

class Triangle():
	def __init__(self, base, height):
		self.base = base
		self.height = height

	def area(self):
		calc = (self.base * self.height) / 2
		return calc

class Hexagon():
	def __init__(self, a):
		self.side = a

	def perimeter(self):
		calc = self.side * 6
		return calc

class Shape():
	"""
	Models a shape.
	Includes method to print statement about size.
	"""
	def __init__(self, w, l):
		self.width = w
		self.len = l

	def print_size(self):
		print("""{} by {}
			  """.format(self.width,
			  	         self.len))

class Square(Shape):
	def perimeter(self):
		calc = self.width * 2 + self.len * 2
		print("The perimeter of the square is: " + str(calc))

	def print_size(self):
		print("""I am a square, sized: {} by {}
			  """.format(self.width,
			  	         self.len))

class Dog():
	def __init__(self,
				 name,
				 breed,
				 owner):
		self.name = name
		self.breed = breed
		self.owner = owner

class Person():
	def __init__(self, name):
		self.name = name

jordan = Person("Jordan Tobin")
hamilton = Dog("Hamilton", "Chiworgi", jordan )



grimes_golden = Apple("green", "grimes golden", "sour", "very large")
small_circ = Circle(4)
triangle = Triangle(20, 30)
hexagon = Hexagon(6)
small_circ.area()
print(triangle.area())
print(hexagon.perimeter())
my_shape = Shape(20, 25)
my_shape.print_size()
my_square = Square(20, 25)
my_square.perimeter()
my_square.print_size()
print(hamilton.owner.name)