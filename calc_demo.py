class calci:
	def add(self, num1, num2):
		return num1 + num2

	def sub(self, num1, num2):
		return num1 - num2

	def divide(self, num1, num2):
		if num2 == 0:
			raise ValueError("num2 is Zero")
		return num1 / num2
# c = calci()
# print(c.add(10,7))
# print(c.sub(19,8))






