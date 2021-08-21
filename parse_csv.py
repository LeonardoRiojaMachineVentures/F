class Inside(): pass
class Outside(): pass

def switch(s):
	if isinstance(s, Outside):
		return Inside()
	elif isinstance(s, Inside):
		return Outside()

def separate(line, separator, escape_char):
	assert(type(separator) == str)
	assert(type(escape_char) == str)	
	assert(separator != escape_char)
	state = Outside()
	tokens = []
	aux = ""
	for c in line:
		if c == escape_char:
			state = switch(state)
		elif c == separator:
			if isinstance(state, Inside):
				aux += c
			elif isinstance(state, Outside):
				tokens.append(aux)
				aux = ""
			else:
				exit("error")
		else:
			aux += c
	return tokens

def parse_csv(x, separator, escape_char):
	assert(type(separator) == str)
	assert(type(escape_char) == str)
	assert(separator == ',' or separator == ' ')
	x = open(x).read()
	lines = [l for l in x.split('\n') if l.strip() != ""]
	header = lines[3]
	content = lines[4:]
	del lines
	
	header = separate(header, separator, escape_char)
	content = [separate(line, separator, escape_char) for line in content]
	for token in content:
		assert(len(token) == len(header))
	return (header, content)

def separate_by_any_of(x, a):
	assert(x.__class__ == str)
	assert(a.__class__ == set)
	for i in a:
		assert(i.__class__ == str)
	tokens = []
	aux = ""
	for c in x:
		if c in a:
			tokens.append(aux)
			aux = ""
		else:
			aux += c
	tokens.append(aux)
	return tokens

def split_by_any_with_index(content, index, a):
	assert(type(content) == list)
	assert(type(index) == int)
	assert(type(a) == set)
	tokens = []
	for line in content:
		assert(type(line) == list)
		tokens.append(separate_by_any_of(line[index], a))
		#print(line[index])
	return tokens

def split_to_array(token, index, a):
	assert(token.__class__ == list)
	assert(index.__class__ == int)
	assert(a.__class__ == set)
	token[index] = separate_by_any_of(token[index], a)
	return token
	
def LevenshteinD(word1, word2):
	assert(m.__class__ == 'str')
	assert(n.__class__ == 'str')
	m = len(word1)
	n = len(word2)
	table = [[0] * (n + 1) for _ in range(m + 1)]
	for i in range(m + 1):
		table[i][0] = i
	for j in range(n + 1):
		table[0][j] = j

	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if word1[i - 1] == word2[j - 1]:
				table[i][j] = table[i - 1][j - 1]
			else:
				table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
	return table[-1][-1]

def exclude_repetition(l):
	assert(l.__class__ == list)
	last = None
	ans = []
	for i in l:
		if last != i[0]:
			ans.append(i)
			last = i[0]
	return ans	

if __name__ == "__main__":
	header, content = parse_csv("central/Ingredient Nutrient Values-Table 1.csv", ',', '"')
	tokens = split_by_any_with_index(content, 1, {','})
	out = open("code_and_ingredients.txt", 'w')
	
	#print(tokens)
	a = []
	for token in tokens:
		b = []
		for t in token:
			b.append(t.strip())
		a.append(b)
	#print(a)
	ingredients = []
	#for ingredient in a:
		#print(ingredient)
		#ingredients.append(ingredient[0])
	#print(ingredients)
	ans = []
	for token in content:
		ans.append((token[0], separate_by_any_of(token[1], {','})[0].lower()))
	#print(ans)
	
	ans = exclude_repetition(ans)
	print(ans)
	print(len(ans))
	del header
	del tokens
	del token
	del b
	del t
	del a
	del ingredients
	del content
	del Inside
	del Outside
	for (code, ingredient) in ans:
		print(str(code) + "$" + str(ingredient), file = out)
	out.close()
	

