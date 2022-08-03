f5 = 0
t2 = 0
o1 = 0

mon = int(input('Enter sum: '))

while True:
	if mon // 1000 != 0:
		n = mon // 1000
		print('Number of thousands =' ,n)
		mon %= 1000
		continue
	elif mon // 100!= 0:
		n = mon // 100
		print('Number of hundreds =' ,n)
		mon %= 100
		continue
	elif mon // 10 != 0:
		n = mon // 10
		print('Number of tens =' ,n)
		mon %= 10
		continue
	elif mon // 1 != 0:
		while True:
			if mon - 5 >= 0:
				mon -= 5
				f5 += 1
				continue
			elif mon - 2 >= 0:
				mon -= 2
				t2 += 1
				continue
			elif mon - 1 >= 0:
				mon -= 1
				o1 += 1
				continue
			elif mon == 0:
				if f5 > 0:
					print('Number of fives = ',f5)
				if t2 > 0:
					print('Number of deuces = ',t2)
				if o1 > 0:
					print('Number of units = ',o1)				
				break

		mon %= 1

	elif mon == 0:
		break

