class Dog:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def __str__(self):
		return f"{self.name} is {self.age} years old"

c = Dog('Razo',19)
print(c)


my_list = [10,-1,12,8,-1,3,-1,-1,2]
res = sorted([ i for i in my_list if i != -1])
c = 0
z = []
for i in range(len(my_list)):
	if my_list[i] == -1:
		z.insert(i,-1)
	else:
		z.insert(i,res[c])
		c += 1 
print(z)



























