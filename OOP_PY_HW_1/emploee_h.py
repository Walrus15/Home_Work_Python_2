from exception import EmailAlreadyExistsException

class Employee:
	
	def __init__(self, name, salary, email):
		self.name = name
		self.salary = salary
		self.email = email
		self.save_email()

	def str(self):
		print(self.name + ' ' + str(self.salary))
		
	def __call__(self):
		return self.salary

	def __lt__(self, other):
		return self.salary < other.salary

	def __le__(self, other):
		return self.salary <= other.salary

	def __gt__(self, other):
		return self.salary > other.salary

	def __ge__(self, other):
		return self.salary >= other.salary

	def __eq__(self, other):
		return self.salary == other.salary

	def __ne__(self, other):
		return self.salary != other.salary

	def work(self):
		return print('I come to the office.')

	def chek_salary(self, days):
		return self.salary * days

	def save_email(self):
		with open('emails.txt', 'a+') as fp:
			fp.write(self.email.lower() + '\n')

	def validate(self):
		with open('emails.txt') as fp:
			if self.email.lower() in fp.read():
				raise EmailAlreadyExistsException('Error!')