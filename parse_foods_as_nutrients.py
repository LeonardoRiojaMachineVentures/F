f = open("central/Ingredient Nutrient Values-Table 1.csv").read()
class Inside(): pass
class Outside(): pass


code_to_food_name = open("code_to_food_name.txt", 'a')
possible_foods = open("to_choose_from.txt", 'w')


def switch(x):
	if isinstance(x,Inside):
		return Outside()
	elif isinstance(x, Outside):
		return Inside()
	else:
		exit("error")

last_code = None

ALL_POSSIBLE_NAME_KEYWORDS = set()

possible_name_keywords = open("possible_name_keywords.txt", 'w')

#NOT_KEYWORDS = set({"canned", "frozen", "cooked", "boiled", "drained"})

NOT_KEYWORDS = open("disallow_name_keywords.txt").read()
NOT_KEYWORDS = set([i for i in NOT_KEYWORDS.split('\n')])
print(NOT_KEYWORDS)


for line in f.split('\n')[4:]:
	state = Outside()
	i = []
	aux = ""
	for c in line:
		
		if c == '"':
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
	assert(len(i) == 9)
	i = [f.strip() for f in i]
	food_code = int(i[0])
	name = i[1].lower()
	nutrient_code = i[2]
	nutrient_name = i[3]
	nutrient_value = i[4]
	keywords = set([i.strip() for i in name.split(',')])
	ALL_POSSIBLE_NAME_KEYWORDS = ALL_POSSIBLE_NAME_KEYWORDS.union(keywords)
	a = keywords.intersection(NOT_KEYWORDS)
	if food_code != last_code:
		code_to_food_name.write(str(food_code) + " : " + str(name) + '\n')
		last_code = food_code
		if a == set():
			possible_foods.write(str(food_code) + " : " + str(name) + '\n')
	#print(i)

for k in ALL_POSSIBLE_NAME_KEYWORDS:
	possible_name_keywords.write(str(k).strip())
	possible_name_keywords.write('\n')
	