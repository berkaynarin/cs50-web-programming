class Dog:
	def __init__(self, dogType, dogColor):
		self.type = dogType
		self.color = dogColor

cakir = Dog("Golden", "Orange")

print(f"Cakır is a type of {cakir.type} dog and it's color is {cakir.color}")