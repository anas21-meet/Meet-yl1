class Animal():
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		print('Yummy!! ' + self.name + ' is eating ' + food)
	def description(self):
		print(self.name + ' is ' + str(self.age) +' years old and loves the color '+self.favorite_color)
	def make_sound(self):
		x=1
		for y in range(x):
			print(self.sound)
animal= Animal('meow ','cat ',4,' Blue')
animal.eat('cat food')
animal.description()
animal.make_sound()
class Person():
	def __init__(self,name,age,city,gender):
		self.name=name
		self.age=age
		self.city=city
		self.gender=gender
	def eatbreakfast(self,breakfast):
		print(self.name+' is eating '+breakfast)
person= Person('mike ','26','Jerusalem','Male')
person.eatbreakfast('eggs')

class Bird(object):
	def __init__(self,name,color,speed):
		self.name=name
		self.color=color
		self.speed=speed
	def getspeed(self):
		return self.speed
	def race(self):
		if self.speed>bird1.speed:
			print(self.name+'has won a race against '+self.name)
		elif self.speed<bird1.speed:
			print(self.name+"has won a race against "+self.name)

	def sing(self,sound):
		self.sound=sound
		print(self.sound)
			
bird1=Bird('sherlock','Blue',8)
print(bird1)
bird1.race()
bird1.sing('LALALALALALALALALALALALA')








