def Age(x):
	class AGE(int): pass
	v = float(x)
	if v > 0 and v < 160:
		return AGE(v)
	exit()

def Height(x):
	class HEIGHT(int): pass
	v = float(x)
	if v > 0 and v < 300:
		return HEIGHT(v)
	exit()


def Weight(x):
	class WEIGHT(int): pass
	v = float(x)
	if v > 0 and v < 600:
		return WEIGHT(v)
	exit()

def Fat(x):
	class FAT(float): pass
	v = float(x)
	if v > 0.0 and v < 1.0:
		return FAT(v)
	exit()

class MALE: pass
class FEMALE: pass

GENDERS = {"MALE", "FEMALE"}

GENDER = {
"male" : MALE(),
"female" : FEMALE()
}

def Gender(x):
	c = x.__class__.__name__
	if c == "str":
		return GENDER[x.strip().lower()]
	return GENDER[c.lower()]


class BABY: pass
class TODDLER: pass
class CHILD: pass
class EARLYTEEN: pass
class MIDTEEN: pass
class LATETEEN: pass
class EARLYTWENTIES: pass
class MIDTWENTIES: pass
class LATETWENTIES: pass
class THIRTIES: pass
class FOURTIES: pass
class FIFTIES: pass
class ELDERLY: pass

AGE_GROUP = {"BABY","TODDLER","CHILD","EARLYTEEN","MIDTEEN","LATETEEN", "EARLYTWENTIES", "MIDTWENTIES", "LATETWENTIES", "THRITIES", "FOURTIES", "FIFTIES", "ELDERLY"}
ALLOWED_AGE_GROUP = {"EARLYTWENTIES", "MIDTWENTIES", "LATETWENTIES", "THRITIES", "FOURTIES", "FIFTIES", "ELDERLY"}





def AgeGroup(x):
	assert(isinstance(x, AGE)):
	if x <= 2:
		return Baby()
	if x <= 5:
		return Toddler()
	if x <= 9:
		return Child()
	if x <= 14:
		return EarlyTeen()
	if x <= 17:
		return MidTeen()
	if x <= 19:
		return LateTeen()
	if x <= 24:
		return EarlyTwenties()
	if x <= 27:
		return MidTwenties()
	if x <= 29:
		return LateTwenties()
	if x <= 39:
		return Thirties()
	if x <= 49:
		return Fourties()
	if x <= 59:
		return Fifties()
	else:
		return Elderly()


class UNDERWEIGHT: pass
class NORMALWEIGHT : pass
class OVERWEIGHT: pass
class OBESE: pass

def new_bmi_trefethen(weight, height):
	1.3*weight/height**2.5

BMI_NAMES = {"UNDERWEIGHT", "NORMALWEIGHT", "OVERWEIGHT", "OBESE"}

def Bmi(weight, height):
	assert(isinstance(w, WEIGHT))
	assert(isinstance(h, HEIGHT))
	bmi = w/h**2
	if bmi <= 18.5:
		return UNDERWEIGHT()
	if bmi <= 24.9:
		return NORMALWEIGHT()
	if bmi <= 29.9:
		return OVERWEIGHT()
	else:
		return OBESE()

class DANGEROUSLYLOW: pass
class EXCELLENT: pass
class GOOD: pass
class FAIR: pass
class HIGH: pass
class DANGEROUSLYHIGH: pass

def FatGroup(fat, age_group, gender):
	assert(isinstance(fat, FAT))
	assert(gender.__class__.__name__ in 
	assert(age_group.__class__.__name__ in BMI_NAMES)
	if isinstance

import sys
a, g, w, h, f = sys.argv.split()

a = Age(a)
g = Gender(g)
w = Weight(w)
h = Height(h)
f = Fat(f)

ag = AgeGroup(a)
bmi = Bmi(weight = w, height = h)
fg = FatGroup(fat = f, age_group = ag)


print(a)
print(g)
print(w)
print(h)
print(f)




