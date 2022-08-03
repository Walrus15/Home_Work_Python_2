def fizzBuzz(fizz,buzz,num3):
	m = []
	i = 0
	while i < num3:
		if i % fizz == 0 and i % buzz == 0:
			m.append('FB')
		elif i % buzz  == 0:
			m.append('B')
		elif  i % fizz == 0:
			m.append('F')
		else:
			m.append(str(i))
	return " ".join(m) + "\n"


file = "D:\\Python P\\fizz_buzz.txt"
file2 = "D:\\Python P\\fizz_buzz_two.txt"
f = open(file)
f2 = open(file2,"w")

for s in f:
	f,b,n = map(int, s.split())
	f2.write(fizzBuzz(f,b,n))

f.close()
f2.close()