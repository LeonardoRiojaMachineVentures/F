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


if __name__ == "__main__":
	headers, content = parse_csv("list_for_h.txt", set([',']), set(['"', '[', ']']), (NoHeader(), 0))
	#print(headers)
	#print(content)
	#for h in headers:
	#print(h)
	all_searches = set()
	for c in content:
		print(c)
		assert(len(c) == 3)
		name = c[0].strip()
		price = c[1].strip()
		searches = c[2].strip()
		searches = [i.strip().lower() for i in searches.split(',')]
		print((name, price, set(searches)))
		all_searches = all_searches.union(set(searches))
	print(all_searches)
	out = open("his_searches.txt", 'w')
	for s in all_searches:
		print(s , file = out)
	out.close()

