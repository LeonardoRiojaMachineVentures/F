def range_float(min, max, step):
	N = int((max - min)//step + 1)
	assert(N > 0)
	return([min + step*i for i in range(N + 1)])

def normal_distribution(average, sd, sigmas, step, multiplier):
	import math
	assert(type(sigmas) == int)
	assert(sigmas >= 0)
	assert(type(average) == float)
	assert(type(step) == float)
	assert(type(sd) == float)
	assert(sd >= 0.0)
	aux = range_float(average - sd*sigmas, average + sd*sigmas, step) 
	ans = [0.0]*len(aux)
	for i in range(len(ans)):
		ans[i] = math.exp(-(aux[i] - average)**2/(2*sd**2))
	assert(type(multiplier) == int)
	assert(multiplier > 0)
	
	ans = [int(i*multiplier) for i in ans]
	return(sum(ans), zip(aux, ans))
		
total1, weights = normal_distribution(average = float(80), sd = float(10), sigmas = 2, step = 0.06, multiplier = 30)
#total2, alphas = normal_distribution(average = float(55), sd = float(8), sigmas = 2, step = 0.03, multiplier = 10)

for w in weights:
	print(w)
print(total1)


amounts = range_float(339, 380, 0.1)

	
'''
import itertools

amounts = [(0.0, 0)]*total1*total2
for (index, element) in enumerate(itertools.product(weights, alphas)):
	sa = element[0][0]*element[1][0]
	multiplicity = element[0][1]*element[1][1]
	amounts[index] = (sa, multiplicity)

#print(amounts)

print(total1)
print(total2)

'''