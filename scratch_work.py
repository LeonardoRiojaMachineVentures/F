class male: pass
class female: pass

def echo(x):
	return(x)

GENDER = {
"male" : male(),
"female" : female(),
221 : male(),
3.14 : female(),
2+4j : male(),
True : male(),
False : female(),
dict : female()
}

def gender(x):
	c = x.__class__.__name__
	if c == "str":
		return GENDER[x.strip().lower()]
	if c == "int" or c == "float":
		return GENDER[x]
	if c == "complex":
		return GENDER[-1*x]
	if c == "bool":
		return GENDER[not x]
	if c == "dict":
		return GENDER[x["first"]]
	return GENDER[c]


x = male()
print(x)
x = female()
print(x)
x = gender(gender(gender(male())))
print(x)
x = gender("male ")
print(x)
x = gender(221)
print(pass(x))
x = gender(1.3)
print(id(x))

'''

class A():
	x = 2
	print(x.__class__.__name__)
	print(type(x.__class__.__class__))
	pass
a = A
b = A()
c = "ssds"
print(type(a)) #<type 'classobj'>
print(type(b)) #<type 'instance'>
print(type(c)) #<type 'str'>

#print(a.__class__)
print(b.__class__) #__main__.A
print(c.__class__) #<type 'str'>


#print(a.__class__.__name__)
print(b.__class__.__name__) #A
print(c.__class__.__name__) #str

print(a.__name__) #A
#print(b.__name__)
#print(c.__name__)


print("dds".__class__)

class Gender():
	class Male(): pass
	class Female(): pass
	def __new__(x):
		
x = Gender.Male()
print(x.__class__)
print(x.__class__.__name__)
x = Gender("male")

'''