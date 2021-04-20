# def recursion():
# 	print('Hello World')
# 	recursion()
# recursion()

# old_list = [10,75,43,15,25,-4,27]

# def bubble_sort(my_list):
# 	last_item = len(my_list) - 1
# 	for i in range(0, last_item):
# 		for j in range(0, last_item - i):
# 			if my_list[j] > my_list[j + 1]:
# 				my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

# 	return my_list

# print('Old List', old_list)
# new_list = bubble_sort(old_list).copy()
# print('New List:', new_list)

# def linery_search(my_list, n, x):
# 	for i in range(0, n):
# 		if my_list[i] == x:
# 			return i
# 	return -1
# my_list = [2,3,4,10,40,21]
# x = 21
# n = len(my_list)
# result = linery_search(my_list, n, x)
# if result == -1:
# 	print('Element is not present in list')
# else:
# 	print('Element is present at index', result)