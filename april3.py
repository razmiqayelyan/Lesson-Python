a = 12
b = 14
print((abs(a + b)+ abs(a-b))/ 2)

import threading
import time

def gender(file_name, start, end):
	with open(file_name) as f:
		for line in f.readlines()[start:end]:
			info = line[:-1].split(',')
			if info[3] == 'male':
				with  open('males.txt', 'a') as malef:
					malef.write(line)
			elif info[3] == 'female':
				with open('females.txt', 'a') as femalef:
					femalef.write(line)
			time.sleep(0.1)
file_name = 'users.txt'
start_time = time.time()
# gender(file_name)
t1 = threading.Thread(target=gender,args=('users.txt',1,33))
t2 = threading.Thread(target=gender,args=('users.txt',34,66))
t3 = threading.Thread(target=gender,args=('users.txt',67,100))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print('Time:',time.time() - start_time)
# print(time.time() - start_time)

def tiv(start, end):
		for i in range(start, end):
			if i % 2 == 0:
				with open('zuyg.txt', 'a') as zuyg:
					zuyg.write(str(i) + '\n')
			else:
				with open('kent.txt', 'a') as kent:
					kent.write(str(i) + '\n')

start_time = time.time()
t1 = threading.Thread(target=tiv,args=(1,25000))
t2 = threading.Thread(target=tiv,args=(25001,50000))
t1.start()
t2.start()
t1.join()
t2.join()

tiv(1, 50000)
print('Time:',time.time() - start_time)
















































