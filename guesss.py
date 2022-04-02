
import random
start = int( input('please input the start number:'))
end = int( input('please input the end number:'))
r = random.randint(start, end)
count = 0
while True:
	count = count + 1
	num = input('please input number:')
	num = int(num)
	if num == r :
		print('You got it!')
		break
	elif num > r :
		print('larger than answer')
	elif num < r :
		print('smaller than answer')
	print('the number you guess', count ,'times')
