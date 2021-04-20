# first = ['Ani','Jessy','Ben']
# second = [1,2,3]
# u = {}
# for x,y in zip(first,second):
# 	u[y] = x
# print(u)
# with open('razo.txt', 'w') as f:
# 	f.write(str(u))
# x = int(input('First:  '))
# y = int(input('Second: '))
# if x > y:
# 	start = x
# elif x == y:
# 	start = x
# else:
# 	start = y

# for i in range(start, 0, -1):
# 	if x % i == 0 and y % i == 0:
# 		print(i)
# 		break
# import json 

# z = []
# x = int(input('Number:  '))
# for i in range(1, x):
# 	if i % 3 == 0 or i % 5 == 0:
# 		z.append(i)
# print(z)
# print(sum(z))
# with open('razos.json', 'w') as razos:
# 	json.dump(z,razos)

# my_list = ['a','b','a','c','b']
# z = []
# for i in my_list:
# 	if i not in z:
# 		z.append(i)
# print(z)
# with open('fayla.txt', 'r') as fayl:
# 	x =  fayl.read().split()
# 	for i in x:
# 		for z in i:
# 			if i.count(z) > 1:
# 				print(i)
import json
try:
	with open('razos.json', 'r') as file:
		print(json.load(file))
except:
	with open('razos.json', 'w') as file:
		z = {"Miyagi":"It’s time to use my colors, in my head"}

		x = json.dump(z)\

