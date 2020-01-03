def squared(x):
	"""
	Returns x ** 2
	:param x: int
	"""
	return x ** 2

def printer(y):
	"""
	Prints y
	:param y: str
	"""
	print(y)

def third(x, y, z, i=2, u=3):
	'''
	Takes 3 required parameters and two optional.

	'''
	return x + y + z + i + u

def divider(x):
	"""
	Divides x by 2
	:param x: int
	"""
	return x / 2

def times_4(x):
	"""
	Multiplies x by 4
	:param x: int
	"""
	return x * 4

y = divider(4)
print(times_4(y))

def converter(x):
	"""
	Converts passed in str to float
	:param x: str.
	:return: string converted to float.
	"""
	try:
		return float(x)
	except ValueError:
		print("Could not convert string into float")

c = converter("55.0")
print(c)