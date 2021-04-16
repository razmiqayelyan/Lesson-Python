
while True:
	try:
		number = int(input('Number:  '))
		break
	except ValueError:
		print('only number')
try:
	my_list = [1,2,23,4,True,'Ani']
except IndexError:
	print('chunenq')
try:
	print('Hello')
except:
	print('Something went wrong')
else:
	print('Nothing went wrong')
try:
	print(x)
except:
	print('Something went wrong')
finally:
	print('The "try except" is finished ')
try:
	name = input('Your name? ')
	print(name)
except KeyboardInterrupt:
	print('\n Bye') 
while True:
	try:
		x = int(input('Number:  '))
		break
	except ValueError:
		print('Only numbers')
x = int(input('Age:  '))
try: 
	if x < 1:
		raise Exception
except Exception:
	print('>')

x = 'hello'
if isinstance(x, str):
	raise TypeError('Only integers are allowed')
try:
	print('a' + 8)
except TypeError:
	print('chi lini')
try:
	x = {'a': 1,'b':2}
	print(x['l'])
except KeyError:
	print('wrong')
try:
	import maths
except ModuleNotFoundError:
	print('Chka tenc modul')
def calculator():
	while True:
		try:
			x = int(input('First number:  '))
			y = int(input('Second number:  '))
		except ValueError:
			print('only numbers')
		z = input('\n*\n+\n-\n/ \n' )
		if z == '*':
			print(x * y)
			break
		if z == '+':
			print(x + y)
			break
		if z == '-':
			print(x - y)
			break
		if z == '/':
			print(x / y)
			break
calculator()

def number():
	while True:
		
		try:
			x = float(input('Input number: '))
			return x
		except ValueError:
			print('only numbers')

def choice():
	ch = ('+','-','/','*')
	while True:
		try:
			c = input('+-/*')
			if c not in ch:
				raise Exception
		except Exception:
			print('only', ch)
		else:
			return c

def result():
	x = number()
	c = choice()
	y = number()
	if c == '+':
		res = x + y
		return f'{x} + {y} = {res}'
	elif c == '-':
		res = x - y
		return f'{x} - {y} = {res}'
	elif c == '*':
		res = x * y
		return f'{x} * {y} = {res}'
	elif c == '/':
		while True:
			try:
				res = x / y 
				return f'{x} / {y} = {res}'
			except ZeroDivisionError:
				print('not Division 0')
				y = number()
print(result())

	


	











