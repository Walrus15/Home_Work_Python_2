

class Employee:
	
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary

	def __str__(self):
		print(self.name + ' ' + str(self.salary))
		
	def __call__(self):
		return self.salary

	def __lt__(self, other):
		return self() < other()

	def __le__(self, other):
		return self() <= other()

	def __gt__(self, other):
		return self() > other()

	def __ge__(self, other):
		return self() >= other()

	def __eq__(self, other):
		return self() == other()

	def __ne__(self, other):
		return self() != other()

	def work(self):
		return print('I come to the office.')

	def chek_salary(self, days):
		return self.salary * days