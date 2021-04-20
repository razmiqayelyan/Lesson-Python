# import time 

# def time_test(func):

# 	def times():
# 		start = time.time()
# 		func()
# 		print(time.time() - start)
# 	return times

# @time_test
# def even():
# 	print('even')
# 	c = []
# 	for i in range(1000000):
# 		if i % 2 == 0:
# 			c.append(i)
# print(even.__name__)
