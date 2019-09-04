#Author:Amit Verma

def sqr(n):
	psqr =False 
	if n>0:
		if (int(n**0.5)**2)==n:
			psqr=True
	return psqr

	
def even(n):
	if n%2==0:
		return 'Even'
	else:
		return 'Odd'
		
def prime(n):
	list1=[]
	x=None
	prime=False
	for i in range(1,n+1):
		if n%i==0:
			list1.append(i)
	if len(list1)==2:
		prime=True
	
	x=[prime,list1]
	return x
	
	
print('Program to check properties of a number.')
num=int(input('Enter positive number:'))
y=prime(num)
print()
print('Prime:',y[0])
print('Factors:',y[1])
print(even(num))
print('Perfect Square:',sqr(num))



	