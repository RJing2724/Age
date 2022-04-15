# Age

driving_Question = input('Are you old enough to drive?')

if driving_Question != 'yes' and 'no':
	print('Please enter yes or no.')
	raise SystemExit #执行退出程序

age = input('Please entre your age.')

age = int(age)

if driving_Question == 'yes': # if 可以套 if 
	if age >= 16:
		print('You passed.')
	else:
		print('You lied.') 

elif driving_Question == 'no':
	if age >= 18:
		print('You are old enough to take driving test.')
	else:
		print('You should wait till you are old enought to take driving test.')
else:
	print('Please enter yes or no.')