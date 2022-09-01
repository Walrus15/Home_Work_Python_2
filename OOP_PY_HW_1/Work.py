class Employee:
	
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary

	def printWorker(self):
		print(self.name + ' ' + str(self.salary))
		
	def work(self):
		return print('I come to the office.')

	def salaryTop(self):
		lis = []
		for i in self:
			if self.salary > salary:
				lis = self.name, self.salary 
			else: lis = name, salary
		return lis

	def chek_salary(self, days):
		return self.salary * days


class Recruiter(Employee):
	def __init__(self, name, salary):
		super().__init__(name, salary)

	def work(self):
		return print(self.__class__.__name__,':',self.name,', I come to the office and start to hiring.')

class Developer(Employee):
	def __init__(self, name, salary):
		super().__init__(name, salary)
		self.tech_stack = []

	def work(self):
		return print(self.__class__.__name__,':',self.name,', I come to the office and start to coding.')

	def numberOfTechnologies(self, tech_stack, name):
		if len(self.tech_stack) > len(tech_stack):
			print('У ' + self.name + ' більше технологій ніж у ' + name)
		else: print('У ' + name + ' більше технологій ніж у ' + self.name)

	#def newWorker(self, other):



if __name__ == '__main__':
	
	mark = Developer('Mark', 500)
	chel = Developer('Chel', 300)

	mark.tech_stack = ['Gimn','Car','Uil','Pikadu']
	chel.tech_stack = ['Dinner','Simon','Uil']





