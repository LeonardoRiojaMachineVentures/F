from sympy import *
alpha = 0.15
t = Symbol('t')
starting_weight = 64
ending_weight = 80
starting_weight *= 1000
ending_weight *= 1000
c = ending_weight - starting_weight
print("as long as the change is not drastic, assume the relation is linear")
w = starting_weight + c*t/(365*24)
print(w.subs(t, 0))
print(w.subs(t, 365*24))

w_prime = diff(w, t)
i = alpha*w_prime + 8*w/240000
print(i)
I = integrate(i, t)
print(I)
x = Symbol('x')
day = I.subs(t, 24*x + 24) - I.subs(t, 24*x)
print(day)
first_day = I.subs(t, 24) - I.subs(t, 0)
last_day = I.subs(t, 365*24) - I.subs(t, 364*24)
print(first_day)
print(last_day)
print(day.subs(x, 0))
print(day.subs(x, 30))
print(day.subs(x, 60))
print(day.subs(x, 120))
print(day.subs(x, 300))
print(day.subs(x, 365))