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

class Word(): pass
class Skip(): pass
def split_by_any(line, s):
	assert(type(line) == str)
	assert(type(s) == set)
	ans = []
	aux = ""
	state = Word()
	for c in line:
		if c in s:
			if isinstance(state, Word):
				state = Skip()
				ans.append(aux)
				aux = ""
			#elif state == Skip():
		else:
			if isinstance(state, Word):
				aux += c
			else:
				state = Word()
				aux += c
	ans.append(aux)
	return ans

def exclude_repetition(l):
	assert(l.__class__ == list)
	last = None
	ans = []
	for i in l:
		if last != i[0]:
			ans.append(i)
			last = i[0]
	return ans
def read_to_list(file):
	f = open(file).read().split('\n')
	f = [k.strip().lower() for k in f]
	f = [i for i in f if i != ""]
	return f
	
if __name__ == "__main__":
	headers, content = parse_csv("central/Ingredient Nutrient Values-Table 1.csv", set([',']), set(['"']), (Header(), 4))
	#print(content)
	ans = []
	for ingredient in content:
		code = int(ingredient[0])
		name = ingredient[1].lower()
		ans.append( (code, split_by_any (name, set ( [",", " "] ) ) ) )
	
	ans = exclude_repetition(ans)
	print(ans)
	foods = read_to_list("search_list.txt")
	foods = set(foods)
	possible = []
	#print(ans)
	d = {}
	for f in foods:
		d[f] = []
	for ingredient in ans:
		code, names = ingredient
		count = 0
		for name in names:
			if name in foods:
				UP = name.upper()
				print(UP)
				before =  " ".join(names[:count])
				after = " ".join(names[count + 1:])
				#possible.append([code, before, UP, after])
				d[name].append((code, before, UP, after))
				continue
			count += 1
	print(d)
	f = open("more_complete_list_of_codes", 'w')
	for k in d:
		print(k, file = f)
		for j in d[k]:
			print(j, file = f)
	
