'''Python program to print English alphabets'''

def A():
	for row in range(6):
		for col in range(11):
			if (row+col==5) or (col-row==5) or (row==3 and row+col in[7,9]):
				print('*',end='')
				
			else:
				print(end=' ')
		print()
#########################
def M():
	for row in range(6):
		for col in range(11):
			if (col==0) or (col-row==0) or (row+col==10) or (col==10):
				print('*',end='')
			else:
				print(end=' ')
		print()
#########################
def I():
	for row in range(7):
		for col in range(11):
			if  (col==5):
				print('*',end='')
			else:
				print(end=' ')
		print()
#########################		
def T():
	for row in range(6):
		for col in range(11):
			if  (col != 5 and row== 0) or (col==5):
				print('*',end='')
			else:
				print(end=' ')
		print()
#########################		
def V():
	for row in range(6):
		for col in range(11):
			if (row+col==10) or (row-col==0):
				print('*',end='')
			
			else:
				print(end=' ')
		print()
		
#########################
A()
print('\v')
M()
print('\v')
I()
print('\v')
T()