w = 64
w_ave = 71.9
w_sd = 10.61
cv = w_sd/w_ave
print(cv)
print(1.2)
coefficient1 = w/(w_ave + 2*w_sd)
print(coefficient1)
coefficient2 = w_ave/(w_ave + 2*w_sd)
print(coefficient2)

