# names = ['Razmik', 'Albert', 'Mery', 'Sargis', 'Arsho']
# c = []
# for i in names:
# 	c.append(len(i))
# max_l = max(c)

# for i in names:
# 	if len(i) == max_l:
# 		print(i)


# a = ['Razmik',True, 8, (12, 24, 'aaa'), 8.5, ['Razo']]
# print(a)
# a = 0
# my_list = ['hp', 'asus', 'dell', 'mac', 'lenovo']
# x = input('What pc you want? ').lower()
# if x in my_list:
# 	print('Yes', a += 1)

# chars = ('i', '@', '#', '$', '%', '&', '*')


# while True:
# 	password = input('Your Password:  ')
# 	if len(password) < 8:
# 		print('Your password lenght is less than 8')
# 		continue
# 	sinvol = 0
# 	tiv = 0 
# 	for i in password:
# 		if i in chars:
# 			sinvol += 1
# 		elif i.isdigit():
# 			tiv += 1
# 	if sinvol < 2:
# 		print('Qich sinvol')
# 		continue
# 	if tiv < 2:
# 		print('Qich tiv?')
# 		continue

# 	if password[0].isalpha() and password[0].islower():
# 		print('Araji tary piti misht mecatar ylni')

# 	print('Strong Password')
# 	break	



# link = input('Link: ')
# count = 0
# for i in link:
# 	count += 1
# 	if i == '=':
# 		break
# print(link[count:])

# x = input('Bar: ')
# if x == x[::-1]:
# 	print('Right:')
# else:
# 	print('False:')
#  x = [ ]
# tiv = ['Hello', 'my', 'my', 'name', 'name', 'is', 'Razo']
# for i in tiv:
# 	if i not in x:
# 		if i not in x:
# 			x.append(i)
# x = []
# tiv = input('Numbers:  ')
# for i in tiv:
# 	if int(i) % 2 == 0:
# 		x.append(i)
# print(x)

# x = []
tiv = input('Numbers:  ').split()
for i in tiv:
	if i % 2 != 0:
		tiv.remove(i)
print(tiv)
































