# first = int(input('Number: ' ))
# second = int(input('Number:  '))
# if first >= second:
# 	start = first 
# else:
# 	start = second
# for i in range(start,first * second + 1):
# 	if i % first == 0 and i % second == 0:
# 		print(i) 
# 		break                                   # zamenapoqr bajaqnarary

# if first >= second:
# 	start = first
# else:
# 	start = second
# while True:
# 	if start % first == 0 and start % second == 0:
# 		print(start)
# 		break
# 	start += 1
# even = 0 
# odd = 0
# for i in range(1, 104):
# 	if i % 2 == 0:                   #kent zuyg 
# 		even += 1
# 	else:
# 		odd += 1
# print(even, odd) 

# x , y = 0 , 1
# while x < 40:
# 	print(x)
# 	x,y = y, x + y             # fibonachi i dzevov enq hashvum

# tiv = 0
# tar = 0
# text = 'python 3.9'
# for i in text:
# 	if i.isalpha():
# 		tar += 1                # texti mej tary u bareri qanaky
# 	if i.isdigit():
# 		tiv += 1
# print(tiv, tar)          




# count = 0 
# number = 73421

# for i in str(number):   # hertov tvery irara gumarum
# 	count += int(i)
# 	print(count)

# count = 1 
# X = int(input('Number:  '))
# for i in range(1, X+1):
# 	count *= i               # faktorialy
# print(count)

# import time 
# start = time.time()


# x = int(input('Number:  '))

# for i in range(2, x):
# 	if x % i == 0:
# 		print('No')
# 		break
# else:
# 	print('Yes,Parza')

import math
import time 
x = int(input('Number:  '))
start = time.time()




for i in range(2, math.ceil(x**0.5)):
	if x % i == 0:
		print('No')
		break
else:
	print('Yes,Parza')

end = time.time()
print(end - start)


	 




















































