from abc import ABC, abstractmethod

class Animal(ABC):
	@abstractmethod
	def move(self):
		pass

class Human(Animal):
	def move(self):
		print("I can walk and run")

class Snake(Animal):
	def move(Self):
		print("I can crawl")

h1 = Human()
h1.move()

s1 = Snake()
s1.move()

print(isinstance(s1, Snake))
print(issubclass(Snake, Human))