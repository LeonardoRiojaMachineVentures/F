d = 10.61
w_ave = 71.9
w = 64
print("you are " + str((w - w_ave)/d) + " sigmas") 
print(0.9545, " lies inside ", w_ave - 2*d, w_ave + 2*d)

def range_float(min, max, step):
	N = int((max - min)//step + 1)
	assert(N > 0)
	return([min + step*i for i in range(N + 1)])

def round_arr(x, d):
	assert(type(d) == int)
	assert(type(x) == list)
	return [round(i, d) for i in x]

def verify(x):
	import math
	assert(type(x) == list)
	N = len(x)
	average = sum(x)/N
	s = 0.0
	for i in x:
		s += (i - average)**2
	sd = math.sqrt(s/N)
	return(average, sd)

def normal(average, sd, sigmas, step, N):
	import math
	#assert(type(sigmas) == int)
	#assert(sigmas >= 0)
	#assert(type(average) == float)
	#assert(type(step) == float)
	#assert(type(sd) == float)
	#assert(sd >= 0.0)
	aux = range_float(average - sd*sigmas, average + sd*sigmas, step) 
	print(aux)
	ans = [0.0]*len(aux)
	for i in range(len(ans)):
		ans[i] = math.exp(-(aux[i] - average)**2/(2*sd**2))
	print(ans)
	assert(type(N) == int)
	assert(N > 0)
	#len(aux) and mul should be in a good ratio
	s = sum(ans)
	print(s)
	ans = [int(i*N) for i in ans]
	print(ans)
	print(len(ans))
	aux = round_arr(aux, 2)
	return(sum(aux), zip(aux, ans))
def normal_distribution(average, sd, sigmas, step, N):
	import math
	#assert(type(sigmas) == int)
	#assert(sigmas >= 0)
	#assert(type(average) == float)
	#assert(type(step) == float)
	#assert(type(sd) == float)
	#assert(sd >= 0.0)
	aux = range_float(average - sd*sigmas, average + sd*sigmas, step) 
	print(aux)
	ans = [0.0]*len(aux)
	for i in range(len(ans)):
		ans[i] = math.exp(-(aux[i] - average)**2/(2*sd**2))
	print(ans)
	assert(type(N) == int)
	assert(N > 0)
	#len(aux) and mul should be in a good ratio
	s = sum(ans)
	print(s)
	ans = [int(i*N) for i in ans]
	print(ans)
	print(len(ans))
	aux = round_arr(aux, 2)
	return(sum(aux), zip(aux, ans))
		

f = open("dri.txt").read()
header = f.split('\n')[0]
content = f.split('\n')[1:]

_, r = normal_distribution(average = 71.9, sd = 10.61, sigmas = 2, step = 0.1, N = 700)
sample = []
for i in r:
	#print([i[0]]*i[1])
	sample += [i[0]]*i[1]


class P:
	def __init__(m, f, sa):
		assert(type(m) == float)
		assert(type(f) == float)
		assert(type(sa) == float)
		assert(m > 0.0)
		assert(f > 0.0)
		assert(sa > 0.0)
		self.m = m
		self.f = f
		self.sa = sa
	def is_enough(self, alpha, beta):
		assert(type(alpha) == float)
		assert(type(beta) == float)
		x = alpha*self.m + beta*self.f
		return(x >= sa)

	def get_averages(x):
		assert(type(x) == list)
		m_sum = 0.0
		f_sum = 0.0
		N = len(x)
		for i in x:
			m_sum += i[0]
			f_sum += i[1]
		return(m_sum/N, f_sum/N)
		
			
	def determine_coefficient(x, alpha, beta)
		assert(type(x) == list)
		below = []
		above = []
		for p in x:
			assert(type(p) == P)
			if p.is_enough(alpha, beta):
				above.append(p)
			else:
				below.append(p)
		b = below.get_averages()
		a = above.get_averages()			



def combine_weights_and_alphas(weights, alphas):
	assert(type(weights) == list)
	assert(type(alphas) == list)
	#import itertools
	assert(len(weights) == len(alphas))
	N = len(weights)
	for i in range(N):
		for j in range(N):
			sa_i = weights[i][0]*alpha[
	#for element in itertools.product(*somelists):
print(sample)
#print(verify(sample))

for line in content:
	nutrient, e, male, female, ul, unit = line.split(',')
	#print(e, male)
	male = float(male)
	if e.strip() == "NE":
		asjusted = male
	else:
		e = float(e)
		print(e)
		print(male)
		adjusted = w*(male - e)/(2*d)
	print(adjusted)