# class
class Simple:
	pass

# instantiate
s = Simple()

# class variable
class Service:
	secret = "영구 배꼽 2개"

sv1 = Service() # Don't need 'new' keyword

sv1.secret

# class function
class Calcular:
	def sum(self, a, b):
		result = a+b
		print(result)

c = Calcular()

c.sum(5, 4) # 9
Calcular.sum(c, 5, 4) # 9

# about self
class Person:
	body = 1
	def setname(self, name):
		self.name = name # instance variable

bek9 = Person()
bek9.setname("bek9")

bax4 = Person()
bax4.setname("bax4")

print(bek9.name, bax4.name) # bek9 bax4

# init
class Talker:
	def __init__(self, dialogue):
		self.dialogue = dialogue
	def talk(self):
		print(self.dialogue)

bek9 = Talker("Hello") # will error if no arg
bek9.talk() # Hello

# inheritance
class RepeatTalker(Talker):
	def talk_twice(self):
		print(self.dialogue*2)

bek9 = RepeatTalker("Hi")
bek9.talk() # Hi
bek9.talk_twice() # HiHi

# overloading
class HiphopTalker(Talker):
	def talk(self):
		print(self.dialogue, "Yo")

bek9 = HiphopTalker("Wassup")
bek9.talk() # Wassup Yo

# operation overloading
class ListCalc:
	def __init__(self, list):
		self.list = list
	def __add__(self, other):
		l = list(self.list)
		l.extend(other.list)
		return l
	def __sub__(self, other):
		l = list(self.list)
		for i in other.list:
			try:
				l.remove(i)
			except:
				pass
		return l

l1 = ListCalc([1,2,3])
l2 = ListCalc([2,3,4])
print(l1+l2)
print(l1-l2)