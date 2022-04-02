import random
r = random.randint(1,100)
while True:
	num = input('please input number:')
	num = int(num)
	if num == r :
		print('You got it!')
		break
	elif num > r :
		print('larger than answer')
	elif num < r :
		print('smaller than answer')
