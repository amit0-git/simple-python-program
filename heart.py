def heart():
	for a in range(6):
		for b in range(7):
			if (a==0 and b%3!=0) or (a==1 and b%3==0) or(a-b==2) or (a+b==8):
				
				print('*',end='')
			else:
				print(end=' ')
		print()
heart()
		