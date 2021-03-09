# import random 

# python_team = ['Mery', 'Albert', 'Arsho', 'Sargis', 'Razmik', 'Arnak']

# random.shuffle(python_team)

# count = 1
# for i,j in zip(python_team[:3],python_team[3:]):
# 	print(count, i,j)
# 	count += 1

# print(len('Ani'))
# print(len(['Ani', 'Aram']))
# print(len({'name':'Ani'}))

# thisdict = {'name':'Aram','year': 1994}
# thisdict['year'] = 2014
# thisdict['age'] = 26
# print(thisdict)                   #{} kam dict('value':'key')

# thisdict = {'name':'Aram','year':1994}
# del thisdict['year']
# print(thisdict)
#person = dict(name='Sargis',year=17, color = 'White', country = 'Vagharshapat')
# for i in person:
	# print(i)  #name,year,color,country
	# print(person[i]) #'Sargis'....

# for i,j in person.items(): #key:value irar het
# 	print(i,j)

# for i in person.values():  #person[i]-i texy
# 	print(i)

# x = person['year']
# x = 2021 - x
# print(x)
# x = 0 
# for i in person:
# 	x += 1 
# print(x)
# x = 0
# person = dict(name='Razmik',name_1='Raz',name_2='Raz',name_3='Razona',name_4='Raznaa')
# for i in person.values():
# 	if i == 'Raz':
# 		x += 1
# print('ka', x ,'hat et baric')
# my_list = ['Ani','Ani','Anna','Ani']
# c = []
# for i in my_list:
# 	if my_list.count(i) > 1:
# 		pass
# 	else:
# 		c.append(i)
# print(c)
# print(y)
# sim = ['!', '@', '#', '$', '&', '*', '^']
# while True:
# 	parol = input('Password:  ')
# 	tiv = 0
# 	simvol = 0
# 	if len(parol) < 8:
# 		print('Paroly petqe parunaki 8 nish')
# 		continue
# 	elif len(parol) > 8:
# 		for i in parol:
# 			if i.isdigit():
# 				tiv += 1
# 			if i in sim:
# 				simvol += 1
# 	if simvol != 2 and tiv != 2:
# 		print('Paroly petq e parunaki 2 simvol ev 2 tiv ')
# 		continue
# 	else:
# 		print('Strong password')
# 		break 

# sim = ['.', '@']

# while True:
# 	simvol = 0
# 	mail = input('Mail:  ')
# 	if len(mail) < 7:
# 		print('Petq e unena minimum 7 simvol')
# 		continue
# 	for i in mail:
# 		if i in sim:
# 			simvol += 1
# 	if simvol != 2:
# 		print('Petq e parunaki @ ev  .')
# 		continue
# 	else:
# 		print('Bomba')
# 		break

# while True:
# 	x = input('Phone number:  ')
# 	for i in x:
# 		if i.isalpha():
# 			print('Petq e parunaki miayn tver')
# 			continue
# 	if len(x) != 9:
# 		print('Petq e baxkacac lini 9 tvic')
# 		continue
# 	if x[0] != '0':
# 		print('Petq e sksi 0ov')
# 		continue
# 	elif x[0] == '0':
# 		print('Good')
# 		break

sim = ['.', '@']
while True:
	simvol = 0
	shnik = ''
	ket = ''
	mail = input('Mail:  ')
	if len(mail) < 7:
		print('Petq e unena minimum 7 simvol')
		continue
	for i in mail:
		if i in sim:
			simvol += 1
	if simvol != 2:
		print('Petq e parunaki @ ev  .')
		continue
	if mail[0] in sim:
		 print('Petq e sksvi tarov kam tvov')
		 continue
	for i in mail:
		if i == '@':
			i = shnik
		if i == '.':
			i = ket
		if mail.index(shnik) < mail.index(ket):
			print('Petq e skzbic lini shniky')

	else:
		print('Bomba')
		break





























