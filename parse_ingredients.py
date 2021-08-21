


from enum import Enum
class State(Enum):
	ID = 1
	NAME = 2
class Counts(Enum):
	YES = 1
	NO = 2
	def flip(self):
		if self == Counts.YES:
			self = Counts.NO
		else:
			self = Counts.YES
	

def generic_function(x):
	last = None
	name_length = 0
	#3 digit code
	assert(type(x) == str)
	for b in bytes(x, 'utf-8'):
		pass
				
		

g = open("to_build_code_to_nutrient.txt").read()
lines = g.split('\n')
CODE_TO_NUTRIENT = {}
for l in lines:
	
	x = []
	s = ""
	c = Counts.YES
	print(l)
	print(bytes(l, 'utf-8'))
	for b in bytes(l, 'utf-8'):
		#print(b)
		if b == ord(','):
			print("found ,")
			if c == Counts.YES: 
				x.append(s)
				s = ""
			elif c == Counts.NO:
				s += chr(b)
		elif b == ord('"'):
			if c == Counts.NO:
				
		else:
			s += chr(b)
	print(x)
		
print(CODE_TO_NUTRIENT)

def parse_csv_with_double_quotes(filename):
	f = open(filename).read()
	q = Quotes.CLOSED
	ans = []
	class Quotes(Enum):
		OPEN = 1
		CLOSED = 2
	line = []
	s = []
	for c in bytes(f, 'utf-8'):
		if q == Quotes.CLOSED:		
			if c == ord(','):
				
			elif c == ord('"'):
			else:
				s.append(c)
		elif q == Quotes.OPEN:
			if c == ord(','):
			elif c == ord('"'):
			else:
				
		else:
			exit("unreachable")
		

#f = open("Ingredient Nutrient Values-Table 1.csv").read()
#generic_function(f)

