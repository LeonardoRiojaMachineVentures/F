def bmi(w, h):
	return w/h**2
def bmi2(w, h):
	return 1.3*w/h**(2.5)
def range_f(min, max, step):
	ans = []
	while min <= max:
		ans.append(round(min, 1))
		min += step
	return ans

def cross(a, b):
	assert(type(a) == list)
	assert(type(b) == list)
	ans = [(0.0, 0.0)]*len(a)*len(b)
	print(len(a))
	print(len(b))
	for (index_1, x) in enumerate(a):
		for (index_2, y) in enumerate(b):
			ans[index_1*len(b) + index_2] = (x, y)
	return ans

def every_ten(x):
	ans = []
	count = 0
	for i in s:
		if count == 10:
			ans.append(i)
			count = 0
		count += 1
	return ans
if __name__ == "__main__":
	w = list(range_f(50, 70, 0.3))
	#print(w)
	h = list(range(160, 180, 1))
	s = cross(w, h)
	del w
	del h
	for i in s:
		w, h = i
		print((w, h), bmi(w, h), bmi2(w, h))




