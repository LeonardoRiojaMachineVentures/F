f = open("restricted_foods.csv").read()
f = f.lower()
lines = f.split('\n')
header = lines[0]
content = lines[1:]
del f
del lines
headers = [h.strip() for h in header.split(',')]
#print(headers)
c = []

for line in content:
	aux = [i.strip() for i in line.split(',')]
	assert(len(aux) == 19)
	c.append(aux)



'''
is_fruit 1 empty
too_much_fructose 2 empty
we_sell 3 not_empty
gluten 4 empty
is_molluscs 5 empty
glucose 6 empty
celery_allergy 7 empty
egg allergy 8
fish 9 ignore
mustard 10 empty
tree_nut 11 empty
sesame 12 empty
soybeans 13 empty
sulfure_dioxide 14 empty
sulfites 15 empty
coconut allergy 16 empty
part_of_diet 17 ignore
"" 18 ignore
'''

def all_true(x):
	for i in x:
		if not i:
			return False
	return True
ans = []
for ingredient in c:
	name = ingredient[0]
	booleans = []
	booleans.append(ingredient[1] == "")
	booleans.append(ingredient[2] == "")
	booleans.append(not(ingredient[3] == ""))
	booleans.append(ingredient[4] == "")
	booleans.append(ingredient[5] == "")
	booleans.append(ingredient[6] == "")
	booleans.append(ingredient[7] == "")
	booleans.append(ingredient[8] == "")
	
	#fish = (ingredient[9] == "")
	booleans.append(ingredient[10] == "")
	booleans.append(ingredient[11] == "")
	booleans.append(ingredient[12] == "")
	booleans.append(ingredient[13] == "")
	booleans.append(ingredient[14] == "")
	booleans.append(ingredient[15] == "")
	if all_true(booleans):
		ans.append(name)
ans = set(ans)
print(ans)

f = open("food_list_final_final.txt", 'w')
for i in ans:
	print(i, file = f)