
import recruiter_developer_h as rdh


if __name__ == '__main__':
	
	mark = rdh.Developer('Mark', 500)
	chel = rdh.Developer('Chel', 300)

	mark.tech_stack = ['Gimn','Car','Uil','Pikadu']
	chel.tech_stack = ['Dinner','Simon','Uil']

	print(mark >= chel)





