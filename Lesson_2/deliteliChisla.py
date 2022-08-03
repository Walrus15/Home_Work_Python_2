num = int(input('Enter number'))

for i in range(1, int(num / 2) + 1):
	if num % i == 0:
		print(i)