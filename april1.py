# x = [1,2,3,4,5]
# while True:
# 	try:
# 		x = iter(x)
# 		print(next(x))
# 	except:
# 		break
# import os
# import time
# while True:
# 	localtime = time.localtime()
# 	result = time.strftime("%I:%M:%S %p", localtime)
# 	print('\n\n\n\n\n\n\n\n',result)      #budelnik sarqel tuny
# 	time.sleep(1)
# 	os.system('cls')

# c = 0 
# while True:
# 	print('\n\n\n\n\n\n\n\n',c)
# 	c += 1
# 	time.sleep(1)
# 	os.system('cls')
# def renj(start,stop,step):
# 	c = []
# 	for i in range(start,stop,step):
# 		c.append(i)
# 	return c


# x = int(input('From: '))
# y = int(input('to: '))
# u = int(input('stop: '))

# print(renj(x,y,u))

# x = [3,7,12,5,20,0]
# u = []
# for i in range(len(x) - 1):
# 	z = x[i] * x[i + 1]
# 	u.append(z)
# print(u)
# def res(sentence, my_list):
# 	sentence = list(sentence)
# 	count = 0
# 	for i in range(len(sentence)):
# 		if sentence[i] == '_':
# 			sentence[i] = my_list[count]
# 			count += 1
# 	return "".join(sentence)
# sentence = '_, we have a _.'
# my_list = ['Ashot', 'problem']
# print(res(sentence,my_list))   

res = [len(i) for i in c]
print(min(res) + max(res))

c = [21, -9, -22, 2116, -71, 33]
z = -8
if z in c:
	print(c.index(z))
else:
	res = []
	for i in c:
		x = abs(z - i)
		res.append(x)
	print(res)
	print(res.index(min(res)))