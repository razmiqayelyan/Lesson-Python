# class Tari:
# 	def __init__(self,year):
# 		self.y = year

# 	def dar(self):
# 		if self.y % 100 == 0:
# 			return self.y // 100
# 		else:
# 			return (self.y // 100) + 1

# x = Tari(2001)
# print(x.dar())

# class Palidrom:
# 	def __init__(self, word):
# 		self.w = word

# 	def polid(self):
# 		if self.w == self.w[::-1]:
# 			return True
# 		else:
# 			return False

# x = Palidrom('Razo')
# print(x.polid())

# class Biggest:
# 	def __init__(self, l):
# 		self.l = l

# 	def big(self):
# 		z = 0
# 		for i in range(0,len(self.l), 2):
# 			res =  self.l[i] * self.l[i+1]
# 			if res > z:
# 				z = res
# 		return z

# c = [3,6,-2,-5,7,3]
# x = Biggest(c)
# print(x.big())
# c = [3,6,-2,-5,7,3]
# print(max([c[i] * c[i+1] for i in range(len(c) - 1)]))

# class Long:
# 	def __init__(self, l):
# 		self.l = l
# 	def longest(self):
# 		z = []
# 		u = ''
# 		for i in self.l:
# 			if len(i) > len(u):
# 				u = i
# 		z.append(u)
# 		self.l.remove(u)
# 		for i in self.l:
# 			if len(i) == len(u):
# 				z.append(i)
# 		return z

# a = ['aba', 'aa', 'ad', 'vcd', 'aba']
# x = Long(a)
# print(x.longest())


# inputList = ['aba', 'aa', 'ad', 'vcd', 'aba']
# c = [i for i in inputList if len(i) == max([len(i) for i in inputList])]
# print(c)

# class Loto:
# 	def __init__(self, lucky):
# 		self.lucky = lucky

# 	def win(self):
# 		for i in range(0,len(self.lucky),2):
# 			z = []
# 			res =  int(self.lucky[i]) + int(self.lucky[i + 1])
# 			z.append(res)
# 			if res not in z:
# 				return False
# 		return True

# a = Loto('1230')
# print(a.win())

loto = input('loto: ')
res = [int(i) for i in loto]
mid = int(len(res) / 2)
c = sum(res[:mid]) == sum(res[mid:])
prin(c)




























