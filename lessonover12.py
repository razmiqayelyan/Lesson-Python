import random
ch = random.choice('pu')
point = 0
if ch = 'u':
	user = 4 - point % 4
	print('Pc-', point, '+', user, "=", point + user)
	point += user
	if point >= 21:
		print('\n\t Win user:')
		break
while True:

	while True:
		user = input('1-3:  ')
		end = 4
		if point > 18:
			end = 22 - point
		if user.isdigit():
			user = int(user)
			if 0 < user < end:

				print('User-', point, '+', user, '=',point + user)
				point += user
				break
			else:
				print('please inputq betwen 1-', end -1)
		else:
			print('please input only number')
	if point >= 21:
		print('\n\t Win PC')
		break
	# if ch == 'u':

	# 	user = 4 - point % 4
	# 	print('Pc-', point, '+', user, "=", point + user)
	# 	point += user
	# 	if point >= 21:
	# 		print('\n\t Win user:')
	# 		break
	

	if ch == 'p'
	
		pc = 4 - point % 4
		print('Pc-', point, '+', pc, "=", point + pc)
		point += pc
		if point >= 21:
			print('\n\t Win user:')
			break
