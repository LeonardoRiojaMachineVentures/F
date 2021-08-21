f = open("choices.txt").read()
lines = [i.strip() for i in f.split('\n')]
lines = [i for i in lines if i != ""]

TRANSFORMATIONS = set()

AVOID = open("avoid_transformations.txt").read()
AVOID = [i.strip() for i in AVOID.split('\n')]
AVOID = [i for i in AVOID if i != ""]

AVOID = set(list(AVOID))
print(AVOID)

wants = open("wants.txt", 'w')
thrown = open("thrown.txt", 'w')




for line in lines:
	line = line.split(':', 1)
	assert(len(line) == 2)
	code = int(line[0])
	rest = str(line[1])
	#print(code, rest)
	#print(code.__class__, rest.__class__)
	rest = rest.split('[', 1)
	name = rest[0]
	rest = str(rest[1])[:-1]
	#print(code, name, rest)
	transformations = rest.split(',')
	transformations = [i.strip() for i in transformations]
	#for f in transformations:
		#print(type(f))
	#	print(f[1:-1])
	transformations = [f[1:-1] for f in transformations]
	#print(code, name, transformations)
	transformations = set(list(transformations))
	TRANSFORMATIONS = TRANSFORMATIONS.union(transformations)
	if set() == transformations.intersection(AVOID):
		print(code, name, transformations)
		wants.write(str(code) + " : " + name + " # " + " ".join(list(transformations))+ '\n')
	else:
		thrown.write(str(code) + " : " + name + "#" + " ".join(list(transformations)) + '\n')
#print(TRANSFORMATIONS)
R = open("select_set_of_transformations.txt", 'w')
for i in TRANSFORMATIONS:
	R.write(i + "\n")
R.close()

import shutil
shutil.copy2("select_set_of_transformations.txt", "select_set_of_transformations_to_edit.txt")


wants.close()
thrown.close()