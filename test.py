# def factorial(n):
# 	if n == 0:
# 		raise ValueError ('bacasakan chpetqa lini')		
		
# 	elif n == 0:
# 		return 1
# 	else:
# 		count = 1 
# 		for i in range(2, n+1):
# 			count *= i
# 		return count

# def print(text,end='\n')
# 	return f"{text} {end}"

# def gcd(x,y):
# 	while x != y:
# 		if x > y:
# 			x -= y # amenamec yndhanur bajanarary
# 		else:
# 			y -= x
# 	return x
def fibon():
	nterms = int(input('Number:  '))
	n1 ,n2 = 0, 1
	count = 0

	if nterms <= 0:
		print('Only positive numbers')
	elif nterms == 1:
		print('Fibonachi up to ', nterms, ":")
		print(n1)
	else:
		print('Fibonachi sequence:')
		while count < nterms:
			print(n1)
			nth = n1 + n2
			n1 = n2
			n2 = nth
			count += 1
