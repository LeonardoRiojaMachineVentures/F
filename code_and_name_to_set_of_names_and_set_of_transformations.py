NAMES = set()
TRANSFORMATIONS = set()
A = "transformations.txt"
B = "code_and_first_name_only.txt"
t = open(A, 'w')
n = open(B, 'w')

class Inside(): pass
class Outside(): pass


def switch(x):
	if isinstance(x,Inside):
		return Outside()
	elif isinstance(x, Outside):
		return Inside()
	else:
		exit("error")



f = open("code_and_name.txt").read()
lines = [i for i in f.split('\n')]
for line in lines:
	line = line.split(':', 1)

	if len(line) != 2:
		continue
	code, whole_name = (line[0], line[1])
	#print(code)
	#print(whole_name)
	state = Outside()
	i = []
	aux = ""
	for c in whole_name:
		if c == '(' or c == ')':
			state = switch(state)
		elif c == ',':
			if isinstance(state, Inside):
				aux += ','
			elif isinstance(state, Outside):
				i.append(aux)
				aux = ""
			else:
				exit("error")
		else:
			aux += c
	i.append(aux)
	print(i)
	i = [f.strip().lower() for f in i]
	name = set((i[0], ))
	print(name)
	transformations = list(set(i[1:]))
	code = int(code.strip())
	print(code, name, transformations)
	TRANSFORMATIONS = TRANSFORMATIONS.union(transformations)
	NAMES = NAMES.union(name)
	

TRANSFORMATIONS = list(TRANSFORMATIONS)
NAMES = list(NAMES)
#print(TRANSFORMATIONS)
#print(NAMES)

for i in TRANSFORMATIONS:
	t.write(i + '\n')
for i in NAMES:
	n.write(i + '\n')

t.close()
n.close()

import shutil
shutil.copy2(A, "transformation_to_edit.txt")
shutil.copy2(B, "code_and_first_name_to_edit.txt")

	