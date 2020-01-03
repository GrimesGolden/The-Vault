class AlwaysPositive:
	def __init__(self, number):
		self.n = number

	def __add__(self, other):
		return abs(self.n + other.n)

class TestClass:
	def __init__(self, number):
		self.n = number

	def __repr__(self):
		return "Object of TestClass"


x = AlwaysPositive(-20)
y = AlwaysPositive(10)
z = TestClass(30)
i = TestClass(45)

print(x + y)
print(y.n)
print(x.n)
print(-20 + 10)
print(TestClass)