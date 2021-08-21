d = 10.61
w_ave = 71.9
w = 64


print("you are " + str((w - w_ave)/d) + " away.")
print(0.9545, " lies inside [", w_ave - 2*d, w_ave + 2*d, "]")
print("healthy people in [", w_ave - 1.9*d, w_ave + 1.6*d, "]")
print("healthy people us in [", 88.9 - 3.5*d, 88.9, "]")

f = open("dri.txt").read()
header = f.split('\n')[0]
content = f.split('\n')[1:]

def stats(x):
	import math
	assert(type(x) == list)
	t = 0.0
	N = 0
	for (value, multiplicity) in x:
		t += value*multiplicity
		N += multiplicity

	average = t/N
	sd = 0.0
	for (value, multiplicity) in x:
		sd += multiplicity*(average - value)**2
	sd = math.sqrt(sd/N)
	
	median = 0.0
	k = 0
	last_value = 0.0
	for (value, multiplicity) in x:
		k += multiplicity
		if k >= N/2:
			median = (last_value + value)/2
			k -= multiplicity
			break
		last_value = value
	return((sd, average, N, median, k))
	
	
def range_float(min, max, step):
	N = int((max - min)//step + 1)
	assert(N > 0)
	return([min + step*i for i in range(N + 1)])

def normal_distribution(average, sd, negative_sigma, positive_sigma, step, N):
	import math
	assert(type(negative_sigma) == float)
	assert(type(positive_sigma) == float)
	assert(negative_sigma >= 0.0)
	assert(positive_sigma >= 0.0)
	assert(type(average) == float)
	assert(type(step) == float)
	assert(type(sd) == float)
	assert(sd >= 0.0)
	values = range_float(average - sd*negative_sigma, average + sd*positive_sigma, step) 
	ans = [0.0]*len(values)
	for i in range(len(ans)):
		ans[i] = math.exp(-(values[i] - average)**2/(2*sd**2))
	assert(type(N) == int)
	assert(N > 0)
	ans = [int(i*N) for i in ans]
	return(sum(values), list(zip(values, ans)))

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


rda_19_to_30 = {
"calcium" : 1_000_000,
"chromium" : 35,
"copper" : 900,
"fluoride" : 0,
"iodine" : 150,
"iron" : 8_000,
"magnesium" : 400_000,
"manganese" : 2_300,
"molybdenum" : 45,
"phosphorus" : 700_000,
"selenium" : 55,
"zinc" : 11_000,
"potassium" : 3_400_000,
"sodium" : 1_500_000,
"chloride" : 2_300_000,
"vitamin a" : 900,
"vitamin c" : 90_000,
"vitamin d" : 0,
"vitamin E" : 15_000,
"vitamin K" : 120,
"thiamin" : 1_200,
"riboflavin" : 1_300,
"niacin" : 16_000,
"vitamin b6" : 1_300,
"folate" : 400,
"vitamin b12" : 2.4,
"pantothenic acid" : 5_000,
"biotin" : 30,
"choline" : 550_000,
}



adjusted_rda = {}
for i in rda_19_to_30:
	adjusted_rda[i] = int(rda_19_to_30.get(i)*coefficient)
print(adjusted_rda)

adjusted_rda_us = {}
for i in rda_19_to_30:
	adjusted_rda_us[i] = int(rda_19_to_30.get(i)*coefficient_us)
print(adjusted_rda_us)


'''
for line in content:
	line = line.strip()
	if line == "":
		continue
	nutrient, e, male, female, ul, unit = line.split(',')
	male = float(male)
	if e.strip() == "NE":
		adjusted = male
	else:
		e = float(e)
		#print("EAR = ", str(e), ", RDA male (95.45%) = ", str(male))
		adjusted = w*(male - e)/(2*d)
		a2 = w*male/(w_ave + 2*d)
		alpha = max(e/w_ave, male/(w_ave + 2*d))
		#print("alpha = " + str(alpha))
		print(nutrient + " for you = " + str(round(w*alpha, 2)) + unit + ", EAR = " + str(e) + ", RDA male (95.45%) = " + str(male))
	#print(adjusted)
	#print("for weight = " + str(a2))

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
			exit("unreachable")
def convert_to_ug(x):
	assert(type(x) == dict)
	for i in x:
		value, unit = x.get(i)[0], x.get(i)[1]
		x[i] = value*unit.mul()
	return(x)


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

'''