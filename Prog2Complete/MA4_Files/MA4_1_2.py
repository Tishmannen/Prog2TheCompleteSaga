import operator
import random
import functools
import math

def vol_dsphere(n,d):
    func = lambda us: functools.reduce(operator.add, [random.uniform(-1,1)**2 for _ in us])
    val = [func([None]*d) for _ in range(n) if func([None]*d) <= 1]
    return 2**d*len(val)/n

def t_vol_dsphere(d):
    r = 1
    return math.pi**(d/2)*r**d/(math.gamma(d/2+1))

for n,d in [(100000,2),(100000, 11)]:
    val = vol_dsphere(n,d)
    t_val = t_vol_dsphere(d)
    print('Approx: ' + str(val) + ', real val: ' + str(t_val))

#Approx: 3.15376, real val: 3.141592653589793
#Approx: 1.92512, real val: 1.8841038793898994