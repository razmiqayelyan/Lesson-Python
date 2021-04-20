# def my_function():
# 	print('Hello i am a Razo')
# my_function()

# def my_function(fname, lname):
# 	print(fname + " " + lname)

# my_function('Emil', 'Sargsyan')

# def my_function(child2, child1):
# 	print("The youngest child is", child2)
# my_function(child1 = 'Emil', child2 = 'John')

# def myfunction(country = 'Armenia'):
# 	print('I am from', country)

# myfunction('Sweden')
# myfunction('India')
# myfunction()

# def my_function(food):
# 	for x in food:
# 		print(x)
# fruits = ["apple", "banana", "cherry"]
# my_function(fruits)

# def function(number):
# 	start = number[0]
# 	for x in lis:
# 		if x > start:
# 			start = x
# 	print(start)
# numb = [12, 22, 44, 55, 74, 89, 26]

# function(numb) 
# def amd_to_euro(dollar, euro):
# 	res = dollar * 520
# 	re = euro * 87.92
# 	return f'AMD->{res} and RUB->{re}'
# amd_to_euro(1000, 1000)
# def myfunc():
# 	global x
# 	x = 'fantastic'
# myfunc()
# print(f'Python is {x}')

# def test(*args):
# 	print(args)
# test(1,12,124,'Ani','Albert')

# def test(**kwargs):
# 	print(kwargs)

# test(name='Albert', girlfriend='Ani')

# add = lambda x,y: x + y
# print(add(2,5))     # def i texy

def number():
	while True:
		number = input('Number: ')
		if number.isdigit():
			number = int(number)
			return number
		else:
			print('only numbers')

x = number()
y = number()
print(x + y)
		
