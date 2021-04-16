# numbers = ['Miyagi', 'and', 'Andy']
# numbers_1 = ['Miyagi', 'and', 'Andy']
# res = numbers_1 is  numbers
# res_1 = numbers == numbers_1
# print(res)
# print(res_1)
# fruits = ['banana', 'apple', 'cherry']
# fruits[1] = 'kiwi'
# print(fruits)

# fruits.append('orange')
# print(fruits)

# fruits.insert(1, 'orange')   #avelcnuma nshac indexic heto
# print(fruits)

# fruits.remove('apple')    # jnjuma
# print(fruits)

# total = 0

# happy = [1,25,10,12,55,11,98,74,58,62]
# for i in happy:
# 	total += i
# print(total)

# # numbers_1 = ['Miyagi', 'and', 'Andy']
# # numbers_1.pop()    #verjiny jnjuma u pahuma ira mej
# # print(numbers_1)

# numbers_1 = ['Miyagi', 'and', 'Andy']
# del numbers_1[1]   # jnjuma 
# print(numbers_1)
# happy.extend(numbers_1) # kpcnuma irar
# print(numbers_1)


# happy.reverse()  # tequma 
# print(happy)

# my_list =  [98,25,10,12,55,11,44,74,58,62]
# # print(max(my_list))
# # print(min(my_list))
# # print(sum(my_list))


# first = my_list[0]
# for i in my_list:
# 	if i > first:  # maximumi ashxatelu dzevy
# 		first = i
# print(first)


# boys = ['Albert', 'Abo', 'Abul']
# girls = ['Mash', 'Qiso', 'Katya']
# res = []
# for i,j in zip(boys,girls):
# 	c = i + ' , ' + j
# 	res.append(c)
# print(' '.join(res))

# c = 0
# for i in range(1, len(boys) + 3,2):
# 	boys.insert(i,girls[c])
# 	c += 1
# print(boys)
numbers =  [98,25,10,12,55,11,44,74,58,62]
first = numbers[0] - numbers[1]

for i in range(1, len(numbers) - 1):   # koxi tver hanumnery
	c = numbers[i] - numbers[i + 1]
	if c > first:
		first = c
print(first)







