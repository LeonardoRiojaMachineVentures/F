f = open("list_of_foods.csv").read()
f = [line.strip().lower() for line in f.split('\n')]
f = [i for i in f if i != ""]
f = [line.split(',') for line in f]
g = []
for line in f:
	ans = []
	for thing in line:
		ans.append(thing.strip())
	g.append(ans)
del f

def to_dict(x):
	assert(type(x) == list)
	count = 0
	header_dict = {}
	for t in x:
		header_dict[t] = count
		count += 1
	return header_dict

header = to_dict(g[0])
N = len(g[0])
content = g[1:]
for line in content:
	assert(len(line) == N)

# header["too_much_fructose"] is empty
# header["we_sell"] is sell
# header["gluten"] is empty
# header["is_molluscs"] is empty
# header["glucose"] is empty
# header["celery allergy"] is empty
# header["egg allergy"] is empty
# header["sesame"] is empty
# header["soybeans"] is empty
# header["sulfure dioxide"] is empty
# header["mustard"] is empty
# header["tree_nut"] is empty
# header["coconut_allergy"] is empty
# header["mustard"] is empty


class Empty(): pass
clas NotEmpty(): pass
a = [
(Empty(), "too_much_fructose"),
(NotEmpty(), "we_sell"),
]


#for line in content:
	
for i in header:
	print(i, header[i])


#print(g)
