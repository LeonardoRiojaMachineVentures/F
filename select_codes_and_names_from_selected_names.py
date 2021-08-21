f = open("code_and_name.txt").read()


NAMES = open("more_restricted_list_foods.txt").read()

NAMES = [i.strip().lower() for i in NAMES.split('\n')]
NAMES = [i for i in NAMES if i != ""]
print(set(list(NAMES)))

class Inside(): pass
class Outside(): pass

R = open("choices.txt", "w")

def switch(x):
	if isinstance(x,Inside):
		return Outside()
	elif isinstance(x, Outside):
		return Inside()
	else:
		exit("error")



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
	name = i[0]
	print(name)
	transformations = list(set(i[1:]))
	code = int(code.strip())
	print(code, name, transformations)
	name = name.lower()
	if name in NAMES:
		R.write(str(code) + " : " + name + str(transformations) + "\n")

R.close()
