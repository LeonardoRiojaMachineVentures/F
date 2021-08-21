class Inside(): pass
class Outside(): pass


class Header(): pass
class NoHeader(): pass

def check(x):
	a = x[0]
	b = x[1]
	#print(a)
	#print(b)
	assert(type(b) == int)
	assert(b >= 0)
	if isinstance(a, Header):
		if b == 0:
			exit("error 4")
		else:
			return(a, b)
	elif isinstance(a, NoHeader):
		if b == 0:
			return (a, b)
		else:
			exit("error 2")
	else:
		exit("error 3")
def switch(s):
	if isinstance(s, Outside):
		return Inside()
	elif isinstance(s, Inside):
		return Outside()

def all_chars(x):
	for i in x:
		assert(type(i) == str)
		assert(len(i) == 1)


def all_printable(x):
	for i in x:
		assert(i.isprintable())
		
def parse_csv(x, separators, escape_chars, header_num):
	print(header_num)
	assert(type(separators) == set)
	assert(type(escape_chars) == set)
	all_chars(separators)
	all_chars(escape_chars)
	assert(separators.intersection(escape_chars) == set())
	assert(not ('\n' in separators))
	assert(not ('\n' in escape_chars))
	all_printable(separators)
	all_printable(escape_chars)
	check(header_num)
	header_num = header_num[1]

	x = open(x).read()
	lines = [l for l in x.split('\n') if l.strip() != ""]
	if header_num == 0:
		headers = []
	else:
		headers = lines[:header_num]
	content = lines[header_num:]
	del lines
	#print(headers)
	#print(content)
	
	headers = [separate(line, separators, escape_chars) for line in headers]
	content = [separate(line, separators, escape_chars) for line in content]
	#for token in content:
	#	assert(len(token) == len(headers))
	
	return (headers, content)

def separate(line, separators, escape_chars):
	state = Outside()
	tokens = []
	aux = ""
	for c in line:
		if c in escape_chars:
			state = switch(state)
		elif c in separators:
			if isinstance(state, Inside):
				aux += c
			elif isinstance(state, Outside):
				tokens.append(aux)
				aux = ""
			else:
				exit("error")
		else:
			aux += c
	tokens.append(aux)
	return tokens

def reduce_repeated(x):
	assert(type(x) == list)
	last = None
	answer = []
	for i in x:
		code = i[0]
		names = i[1]
		
		if code != last:
			answer.append((code, names))
			last = code
	return answer	

def from_some_weird_tuple_thing_to_csv(data, filename):
	f = open(filename, 'w')
	print("code, ingredient_group, real_product", file = f)
	for d in data:
		print(d[0] + "," + d[1] + "," + d[2], file = f)
	f.close()

if __name__ == "__main__":
	headers, content = parse_csv("central/Ingredient Nutrient Values-Table 1.csv", set([',']), set(['"']), (Header(), 4))
	#print(content)
	ans = []
	for ingredient in content:
		code = ingredient[0].strip().lower()
		name = ingredient[1].strip().lower()
		names = [n.strip() for n in name.split(',')]
		ans.append((code, names))
	#print(ans)
	del ingredient
	del content
	del names
	del name
	del code
	ans = reduce_repeated(ans)
	#print(ans)
	
	f = open("combined_searches_reduced.txt").read()
	ingredients = [line for line in f.split('\n') if line.strip() != ""]
	ingredients = [line.strip().lower() for line in ingredients]
	ingredients = set(ingredients)
	final = []
	for ingredient in ingredients:
		for code, keys in ans:
			if ingredient in set(keys):
				final.append((code, ingredient, "%".join(keys)))
				
	print(final)
	from_some_weird_tuple_thing_to_csv(final, "the_final_list_to_choose_from.csv")
		
