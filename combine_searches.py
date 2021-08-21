a = open("his_searches.txt").read()
a = set(a.split('\n'))
b = open("my_searches.txt").read()
b = set(b.split('\n'))

out = open("combined_searches.txt", 'w')

c = a.union(b)
for i in c:
	print(i, file = out)