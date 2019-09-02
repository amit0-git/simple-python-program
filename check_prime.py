#Author:Amit Verma
def prime(n):
	list1=[]
	prime=False
	for i in range(1,n+1):
		if n%i==0:
			list1.append(i)
	if len(list1)==2:
		prime=True
	
	return prime
print('Program to check prime number.')
num=int(input('Enter number:'))
print(prime(num))

	