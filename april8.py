import string 

letters = string.ascii_letters
print(letters)

lower = string.ascii_lowercase
print(lower)

upper = string.ascii_uppercase
print(upper)

number = string.digits
print(number)

chars = string.punctuation
print(chars)

a = 'ani'
b = 'jon'

b = f'{b}  {a.replace("n","m")}'
print(a)
print(b)

class calculator:
	""" Calculator """
	def number(self):
		while True:
			try:
				number = int(input('Number:'))
				return number
			except:
				print('Only numbers')

	def choice(self):
		c = "+","-","/","*"
		while True:
			ch = input('+ - / *')
			if ch in c:
				return ch
			else:
				print('only', c)


	def result(self):
		x = self.number()
		ch = self.choice()
		y = self.number()

		if ch == "+":
			return x + y

res = calculator()
print(res.result())
class Armenia:
	def country(self):
		print('Yerevan')
class Usa:
	def country(self):
		print('Glendale')

def country():
	return 'Good'

print(country())

A = Armenia()
U = Usa()
A.country()
U.country()


class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname

	def result(self):
		print(self.firstname, self.lastname)

class Student(Person):
	def __init__(self, fname, lname, raiting):
		super().__init__(fname, lname)
		self.raiting = raiting
	def welcome(self):
		print(self.raiting)

x = Student("Razo", "Mikayelyan", 5)
x.result()
x.welcome()




































