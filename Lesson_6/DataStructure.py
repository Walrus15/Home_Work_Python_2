def MoreGroups(j,p,fr,fu):
	g1 = j & p
	g2 = fr & fu
	return g1 | g2

def NotFrontEnd(j,p,fr,fu):
	g1 = j - fr
	g2 = p - fr
	g3 = fu - fr
	return g1 | g2 | g3

java = {"Tolik Kucha" , "Liza Juba" , "Tolik Simp" , "Jon Viner" , "Mark Huker"}

python = {"Tolik Kucha" , "Fina Heel" , "Jon Viner" , "Mark Huker"}

frontEnd = {"Klich Finder" , "Kupa Among" , "Oper Man" , "Liza Him" , "Mark Huker"}

fullStack = {"Kupa Among" , "Mark Huker" , "Kim Tuplik" , "Sara Von"}



print('In two or more groups: ',MoreGroups(java,python,frontEnd,fullStack))
print('Do not learn on the frontend: ',NotFrontEnd(java,python,frontEnd,fullStack))
print('Learn Python or Java: ',)  #Не понял вопроса. Нужно вывести что-то одно или то и то?