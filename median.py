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
	for (value, multiplicity) in x:
		k += multiplicity
		print(k)
		if k >= N/2:
			median = value
			break
	
	return((sd, average, N, median))
	
if __name__ == "__main__":
	x = [(2.2, 10), (2.3, 10), (2.4, 10), (2.5, 1), (2.6, 10), (2.7, 6)]
	print(x)
	print(stats(x))
