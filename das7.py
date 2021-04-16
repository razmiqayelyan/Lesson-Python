# word = 'pythono'
# c = {}
# for i in word:
# 	c[i] = word.count(i)
# print(c)

# set1 = {12, 12, 23, '11', 'Hello'}
# print(set1)                                   
# for i in set1:         # i-i mej menak mi hat 12 ktpi
# 	print(i)

# set1.remove(12) # jnjuma bayc ete chka erora tali
# set1.discard(1) # jnjuma ete chka eror chi tali

# set1 = {12, 12, 23, '11', 'Hello'}
# set2 = {12, 12, 23, '50', 'Hello'}
# set3 = set1.union(set2)  # miasnuma irar
# print(set3)

# x = input('Pakagcer:  ')

# count = 0 
# for i in x:
# 	if i == ')':
# 		count -= 1
# 	elif i == '(':
# 		count += 1
# 	if count == -1:
# 		print('error')
# 		break
# if count > 0:
# 	print('error')
# elif count == 0:
# 	print('Good')

# x = 12 
# y = 15 
# for i in range((12 * 15)+ 1):
# 	if i % 12 == 0 and i % 15 == 0 and i < 180:
# 		print(i)
# x = int(input())
# y = int(input()) 
# if x > y:
# 	start = x
# else:
# 	start = y
# count = 2
# while True:
# 	res = start * count
# 	if res % x == 0 and res % y == 0:
# 		print('good', res)
# 		break
# 	else:
# 		count += 1


# x = int(input())
# y = int(input()) 
# if x > y:
# 	start = x
# 	result = x
# else:            # aveli karj verevinic
# 	start = y
# 	result = y
# count = 2
# while True:
# 	start += result
# 	if res % x == 0 and res % y == 0:
# 		print('good', start)
# 		break
	

# set1 = {12,23,'11','hello'}
# set2 = {14,3,'141','world'}  # ete ka talisa false ete nuyn banic chka talisa True
# print(set1.isdisjoint(set2))

# x = input('Name: ')
# set1 = {12,23,'11','hello'}
# if x in set1:
# 	print('ka setum')
# else:
# 	print('chka')
# set1 = {12,23,'11','hello'}
# set2 = {59,48,'11','hello'}
# for i in set1:
# 	if i in set2:
# 		print(i)
z = []
x = ['Ani', 'Aram']
y = ['Ani', 'Arsen']
for a,b in zip(x,y):
	if a != b:
		z.append(a)
		z.append(b)
print(z)


































