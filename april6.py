# def odd_even(number):
# 	end = number % 10
# 	if number == 0:
# 		return True
# 	elif end % 2 == 0:
# 		return False
# 	elif number != 0:
# 		return odd_even(number//10)

# print(odd_even(11))

# c = []
# def numbers(n):
# 	if n == 0:
# 		return " ".join(reversed(c))
# 	else:
# 		c.append(str(n))
# 		return numbers(n-1)
# print(number(5))

# a = 7
# b = 5
# res = (a*a-b*b)/(a-b)
# print(res)             # import num2words

# c = {"a":"1","b":"2","c":"2"}
# u = {}
# for key,value in c.items():
# 	if value not in u:
# 		u[value] = key
# 	else:
# 		u[value] = list(u[value])
# 		u[value].append(key)
# print(u)

# class MyClass:
# 	x = 5
# p1 = MyClass()
# print(p1.x)

class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def result(self):
		return self.name + self.age

p1 = Person('John','36')
print(p1.name)
print(p1.age)
print(p1.result())

































