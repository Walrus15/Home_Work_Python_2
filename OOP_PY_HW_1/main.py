from exception import EmailAlreadyExistsException
from recruiter_developer_h import Developer
from recruiter_developer_h import Recruiter
from emploee_h import Employee



	#mark = rdh.Developer('Mark', 500)
	#chel = rdh.Developer('Chel', 300)

	#mark.tech_stack = ['Gimn','Car','Uil','Pikadu']
	#chel.tech_stack = ['Dinner','Simon','Uil']

	#


def main():
    mark = Employee('Man', 24, 'gdfjgdsf')
    chel = Employee('Himmm', 23, 'gmail')
    Employee('Dimsf', 25, 'lolman')

    giorg = Developer('Giorgi', 200, 'C++ Python SQL')

    giorg.printDev()

    print(mark <= chel)


if __name__ == '__main__':
    try:
        main()
    except EmailAlreadyExistsException as ex:
        pass
