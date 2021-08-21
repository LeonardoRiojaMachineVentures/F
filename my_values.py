import sys


from enum import Enum
class Gender(Enum):
	MALE = 1
	FEMALE = 2
	def __init__(x):
	    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    print switcher.get(argument, "Invalid month")
		match type(x):
			case Gender: return x
			case str: match x:
				case "male": return Gender.MALE
				case "female" : return Gender.FEMALE
				case _: exit("error")
			case _: exit("error")
		
def check(x, min, max, d):
	x = float(x)
	assert(min < x and x < max)
	return(round(x, d))

def bmi(w, h):
	return(w/h**2)

class BMIGroup(Enum):
	UNDERWEIGHT = 1
	NORMAL = 2
	OVERWEIGHT = 3
	OBESE = 4
	def __init__(x):
		if type(x) == BMIGroup:
			return(x)
		assert(type(x) == float)
		if x < 18.5:
			return BMIGroup.UNDERWEIGHT
		elif x < 24.9:
			return BMIGroup.NORMAL
		elif x < 29.9:
			return BMIGroup.OVERWEIGHT
		else:
			return BMIGroup.OBESE

class FatGroup(Enum):
	ESSENTIAL_FAT = 1
	ATHLETES = 2
	FITNESS = 3
	ACCEPTABLE = 4
	OBESITY = 5
	def classify(x, g):
		assert(type(x) == float)
		assert(0.0 < x and x < 1.0)
		
		if x <= 5.0:
			return FatGroup.ESSENTIAL
		elif x <= 13.0:
			return FatGroup.ATHLETES
		elif x <= 17.0:
			return FatGroup.FITNESS
		elif x <= 24.0:
			return FatGroup.ACCEPTABLE
		else:
			return FatGroup.OBESITY


Essential fat	10-13%
Athletes	14-20%
Fitness	21-24%
Acceptable	25-31%
Obesity	>32%

def parse_values(values):
	age, gender, height, weight, fat_group = values.split()

	age = Age(age)
	
	gender = Gender(gender)

	height = Height(height)
	
	weight = Weight(weight)

	fat_group = FatGroup(fat_group, gender, height, weight, age)
	
	
if __name__ == "__main__":
	parse_values(sys.argv[1:])
	#21 male 1.78 64 0.15

#you are -0.7445805843543832 away.
#0.9545  lies inside [ 50.68000000000001 93.12 ]
#healthy people in [ 51.74100000000001 88.876 ]
#healthy people us in [ 51.76500000000001 88.9 ]
#8.668724405136333 71.37882738339886 973232 71.546 486246
#0.7200440673337511
#6.314917008939404 80.49008197061426 530190 81.77000000000001 265055
#0.6779672937547617
#{'calcium': 720044, 'chromium': 25, 'copper': 648, 'fluoride': 0, 'iodine': 108, 'iron': 5760, 'magnesium': 288017, 'manganese': 1656, 'molybdenum': 32, 'phosphorus': 504030, 'selenium': 39, 'zinc': 7920, 'potassium': 2448149, 'sodium': 1080066, 'chloride': 1656101, 'vitamin a': 648, 'vitamin c': 64803, 'vitamin d': 0, 'vitamin E': 10800, 'vitamin K': 86, 'thiamin': 864, 'riboflavin': 936, 'niacin': 11520, 'vitamin b6': 936, 'folate': 288, 'vitamin b12': 1, 'pantothenic acid': 3600, 'biotin': 21, 'choline': 396024}
#{'calcium': 677967, 'chromium': 23, 'copper': 610, 'fluoride': 0, 'iodine': 101, 'iron': 5423, 'magnesium': 271186, 'manganese': 1559, 'molybdenum': 30, 'phosphorus': 474577, 'selenium': 37, 'zinc': 7457, 'potassium': 2305088, 'sodium': 1016950, 'chloride': 1559324, 'vitamin a': 610, 'vitamin c': 61017, 'vitamin d': 0, 'vitamin E': 10169, 'vitamin K': 81, 'thiamin': 813, 'riboflavin': 881, 'niacin': 10847, 'vitamin b6': 881, 'folate': 271, 'vitamin b12': 1, 'pantothenic acid': 3389, 'biotin': 20, 'choline': 372882}

from enum import Enum
class Unit(Enum):
	UG = 1
	MG = 2
	G = 3
	def mul(self):
		if self == Unit.UG:
			return(1)
		elif self == Unit.MG:
			return(1_000)
		elif self == Unit.G:
			return(1_000_000)
		else:
			exit("should not happen")
def convert_to_ug(x):
	assert(type(x) == dict)
	for i in x:
		value, unit = x.get(i)[0], x.get(i)[1]
		x[i] = value*unit.mul()
	return(x)


def bmi(w, h):
	return(w/h**2)



#_______________


_, r = normal_distribution(average = 71.9, sd = 10.61, negative_sigma = 1.9, positive_sigma = 1.6, step = 0.01, N = 400)
#_, s = normal_distribution(average = 71.9, sd = 10.61, negative_sigma = 2.0, positive_sigma = 2.0, step = 0.1, N = 4)

sd, average, total, median, k = stats(r)
print(sd, average, total, median, k)


coefficient = w/(median + 2*sd)
print(coefficient)


_, r_us = normal_distribution(average = 88.9, sd = 10.61, negative_sigma = 3.5, positive_sigma = 0.0, step = 0.01, N = 400)

sd, average, total, median, k = stats(r_us)
print(sd, average, total, median, k)


coefficient_us = w/(median + 2*sd)
print(coefficient_us)


#__________


print(bmi(47, 1.60))
print(bmi(65, 1.78))

for_me = {
"vitamin A" : (521.91, Unit.UG),
"vitamin B1" : (0.75, Unit.MG),
"vitamin B2" : (0.83, Unit.MG),
"niacin" : (9.28, Unit.MG),
"vitamin B6" : (1.05, Unit.MG),
"folate DFE" : (247.84, Unit.MG),
"cobalamin" : (1.5, Unit.UG),
"vitamin C" : (115.98, Unit.MG),
"vitamin D" : (0, Unit.MG),
"alpha-tocopherol" : (9.01, Unit.MG),
"calcium" : (826.15, Unit.MG),
"copper" : (525.73, Unit.UG),
"iodine" : (86.98, Unit.MG),
"iron" : (6.38, Unit.MG),
"magnesium" : (262.87, Unit.MG),
"molybdenum" : (26.1, Unit.UG),
"phosphorus" : (792.35, Unit.MG),
"selenium" : (33.8, Unit.UG),
"zinc" : (7.06, Unit.MG)
}

c = convert_to_ug(for_me)
print(c)