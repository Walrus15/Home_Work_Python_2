import emploee_h as eh

class Recruiter(eh.Employee):
	def __init__(self, name, salary):
		super().__init__(name, salary)

	def work(self):
		return print(self.__class__.__name__,':',self.name,', I come to the office and start to hiring.')

class Developer(eh.Employee):
	def __init__(self, name, salary, tech_stack):
		super().__init__(name, salary, tech_stack)
		self.tech_stack = tech_stack

	def printDev(self):
		print(self.name + ' | ' + str(self.salary) + ' | ' + self.tech_stack)

	def work(self):
		return print(self.__class__.__name__,':',self.name,', I come to the office and start to coding.')

	def numberOfTechnologies(self, tech_stack, name):
		if len(self.tech_stack) > len(tech_stack):
			print('У ' + self.name + ' більше технологій ніж у ' + name)
		else: print('У ' + name + ' більше технологій ніж у ' + self.name)