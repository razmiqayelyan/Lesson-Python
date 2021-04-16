# def miles(km):
# 	return km * 0.62
# print(miles(12))

# def seconds(day):
# 	return day * 86400
# print(seconds(2)
# def password(kod):
# 	while True:
# 		count = 0
# 		if len(kod) < 8:
# 			print('Your password is very short')
# 			continue
# 		for i in kod:
# 			if i.isdigit():
# 				count += 1
# 		if count < 2:
# 			print('You can have minimum 2 numbers in password')
# 			continue
# 		if count >= 2:
# 			print('Good password')
# 			break

# password(input(''))
# def fact(factorial):
	
# 	x = 1
# 	if factorial < 0:
# 		print('factorial does not exist for negative numbers')
# 	elif factorial == 0:
# 		print('The factorial of 0 is 1')
# 	else:
# 		for i in range(1, factorial + 1):
# 			x *= i 
# 	return x
# z = int(input('Hello: '))
# print(fact(z))
import random 

d = []
x = ('♣','♦','♥','♠')
y = ('6','7','8','9','10','valet','dama','karol','tuz')
for i in x:
	for z in y:
		res = i + z
		d.append(res)
random.shuffle(d)

user_1 = []
user_2 = []
xoz = []
for i in range(6):
	c = d.pop()
	user_1.append(c)
for i in range(6):
	c = d.pop()
	user_2.append(c)
# print(user_1)
# print(user_2)
# print(d) #kalodic dusa eke pop aracnery

c = d.pop()
xoz.append(c)
# print(xoz)
tal = input('Do you want take this card? y/n ').lower()
if tal == 'y':
	user_1.append(xoz)
	for i in range(2):
		c = d.pop()
		user_1.append(c)
else:
	user_2.append(xoz)
	for i in range(2):
		c = d.pop()
		user_2.append(c)
print(user_1)
print(user_2)


