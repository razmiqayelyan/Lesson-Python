# import os 

# # path = f'{os.getcwd()}/Razos'
# # os.mkdir(path) # stexcuma et papkum file Razos anunov
# f = open('armenia.txt','x') #stexcuma taza file u ete ka talisa error
# f = open('armenia.txt','a') #stexcuma taza file u ete ka karas mejy ban avelasnes
# f.write('Something') #stexcuma u mejy gruma Something.inch kar mnuma chi jnjum
# f = open('armenia.txt','w') #stexcuma taza file u ete mejy inchvor ban ka jnjuma
# f.write('Something') #stexcuma u mejy gruma Something.inch kar jnjuma
# f = open('armenia.txt','r') #uxaki bacuma isk ete chka erora tali
# f.read() # ashxatuma menak 'r' i vaxt
# f.close() # anpayman file y baceluc heto petq e pakel

# os.remove('armenia.txt') # jnjuma

# with open('armenia.text', 'w') as f: #bacum enq filey,'w'a nshanakuma sax jnjuma
# 									 #u havasarcnum f-in   
# 	f.write('Avelacnel mi ban')

# try:
# 	with open('RazmikMikayelyan.txt') as fil:
# 		print('my password is',fil.road())
# except FileNotFoundError:
# 	password = input('your password:  ')
# 	with open('RazmikMikayelyan.txt', 'w') as fil: #stexcuma u avelcnuma inputy
# 		fil.write(password)
# finally:
# 	print('Thanks')

# with open('Year.txt') as fil:
# 	for i in fil.read():
# 		if i.isdigit():
# 			print(i)

# with open('Year.txt') as fil:
# 	c = fil.read().split(' ') # amenaerkar bary
# 	# print(max(c, key=len)) # tarberak mek
# 	x = ''
# 	for i in c:
# 			if len(i) > len(x): # tarberak 2
# 				x = i
# 	print(x)

# with open('Year.txt') as fil:
# 	c = fil.read().split(' ')
# 	z = []
# 	for i in c:
# 		if i not in z:
# 			z.append(i)
# 			print(i, c.count(i))
path = f'{os.getcwd()}/web_images'
try:
	os.mkdir(path)

except OSError:
	print("Creation of the directory %s failed" % path)
else:
	print('Successfully created the directory %s' % path)