while True:
	num1 = int(input('\n\nEnter first number: '))
	num2 = int(input('Enter second number: '))
	oper = input('Enter operation: ')

	if oper == '+':
		ans = num1 + num2
		print('Your answer = ', ans)
	elif oper == '-':
		if num1 > num2:
			ans = num1 - num2
		else: 
			ans = num2 - num1
		print('Your answer = ', ans)
	elif oper == '*':
		ans = num1 * num2
		ans = num2 * num1
		print('Your answer = ', ans)
	elif oper == '/':
		if num1 > num2:
			ans = num1 / num2
		else:
			ans = num2 / num1
		print('Your answer = ', ans)
	else:
		print('Error!!!')

	if oper == '0':
		break