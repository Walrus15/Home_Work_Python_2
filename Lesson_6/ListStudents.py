listStudens = {'Tolik': [8,9,10,4,6,7],
				'Dima': [3,6,1,8,5,8,12,12],
				'Sasha':[5,7,4,9,10,4,3],
				'Masha':[12,8,1,8,9,10,9]}
print('\nList students: ')
for key in listStudens.keys():
	n = sum(listStudens[key]) / len(listStudens[key])
	print(key, listStudens[key],' average mark |',n,'|')

print('\nSuccessful student: ',max(listStudens, key = listStudens.get),'\nLaging student: ',min(listStudens, key = listStudens.get))	
	