w = 64

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
	
	return((sd, average, N))
	
	
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

_, r = normal_distribution(average = 71.9, sd = 10.61, negative_sigma = 2.0, positive_sigma = 1.5, step = 0.04, N = 200)
_, s = normal_distribution(average = 71.9, sd = 10.61, negative_sigma = 5.0, positive_sigma = 5.0, step = 0.04, N = 200)
sd, average, total = stats(r)
print(sd, average, total)
print(w/(2*sd))


sd, average, total = stats(s)
print(sd, average, total)
