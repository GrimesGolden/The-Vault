# Challenge 1

class Shape():
	"""
	Models a shape.
	Includes method to print statement about size.
	"""
	shape_list = []
	def __init__(self, w, l):
		self.width = w
		self.len = l
		self.shape_list.append((self.width, self.len))

	def print_size(self):
		print("""{} by {}
			  """.format(self.width,
			  	         self.len))

	def what_am_i(self):
		print("I am a shape")

class Square(Shape):
	"""
	Represents a square, child of Shape.
	"""

	def __repr__(self):
		return "{} by {} by {} by {}".format(self.width,self.width, self.len, self.len)

	def calculate_perimeter(self):
		calc = self.width * 2 + self.len * 2
		print("The perimeter of the square is: " + str(calc))

	def print_size(self):
		print("""I am a square, sized: {} by {}
			  """.format(self.width,
			  	         self.len))

	def change_size(self, width, length):
		self.width += width
		self.len += length
		print(self.width, self.len)




class Rectangle(Shape):
	def calculate_perimeter(self):
		calc = self.width * 2 + self.len * 2
		print("The perimeter of the rectangle is: " + str(calc))

class Rider():
	def __init__(self, name):
		self.name = name

class Horse():
	def __init__(self, name, species, rider):
		self.name = name
		self.species = species
		self.rider = rider

	def info(self):
		print("""
			  This horse is called {} 
			  It's species is {}
			  It's rider is {}
			  """.format(self.name, self.species, self.rider.name)
			  )

class Hexagon():
	sides = []
	def __init__(self, w, l):
		self.width = w
		self.length = l
		self.sides.append((self.width, self.length))


john = Rider("Johnny Chainwax")
fred = Horse("fred", "arabian", john)
fred.info()

class Hexagon():
	sides = []
	def __init__(self, w, l):
		self.width = w
		self.length = l
		self.sides.append((self.width, self.length))

def compare(obj1, obj2):
	return obj1 is obj2

h1 = Hexagon(20, 20)
h2 = Hexagon(10, 10)
h3 = Hexagon(200, 100)

square = Square(20, 25)
rectangle = Rectangle(20, 25)
square.calculate_perimeter()
rectangle.calculate_perimeter()
square.what_am_i()

print(Hexagon.sides)
print(Shape.shape_list)
print(square)

print(compare(h1, h2))

