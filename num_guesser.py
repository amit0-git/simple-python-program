import random

ch=5
print("""
	|------------------------------|
    	 Choose number between 10-20        
	|------------------------------|
""")
print()
num=random.randint(10,20)
while ch>=0:
	try:
		guess=int(input('Guess No. '))
	except Exception as a:
		print('Provide a integer number!')
		continue
	if num==guess:
		print(':-)')
		print('You found it!')
		break
	else:
		if guess >num:
			print(f'No. is lesser than {guess}')
		else:
			print(f'No. is greater than {guess}')
	ch-=1
else:
	print(':-(')
	print(f'Answer was {num}')
