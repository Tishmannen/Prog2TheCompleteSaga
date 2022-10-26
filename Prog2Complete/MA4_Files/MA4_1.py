import math
import random
import matplotlib.pyplot as plt
import operator
import functools
from time import perf_counter
import concurrent.futures as future

########### MA4 1.1

def rand_circle(n):
    val = {
        'inval_x': [],
        'inval_y': [],
        'outval_x': [],
        'outval_y': []
    }
    for i in range(n):
        val_1 = random.uniform(-1,1)
        val_2 = random.uniform(-1,1)
        if val_1**2+val_2**2 <= 1:
            val['inval_x'].append(val_1)
            val['inval_y'].append(val_2)
        else:
            val['outval_x'].append(val_1)
            val['outval_y'].append(val_2)
    pi_approx = 4*len(val['inval_x'])/n
    print('pi approx: ' + str(pi_approx))
    print('pi = ' + str(math.pi))
    plt.axis('equal')
    plt.plot(val['inval_x'],val['inval_y'],'r.',val['outval_x'],val['outval_y'],'b.')
    plt.title('n = ' + str(n) + ', pi approximation = ' + str(pi_approx))
    my_file = 'MA4_1_1_n=' + str(n) + '.png'
    my_directory = 'MA4_files'
    plt.savefig(my_directory + '/' + my_file)

n = [1000,10000,100000]
for i in n:
    rand_circle(i)



########### MA4 1.2

def vol_dsphere(n,d):
    func = lambda us: functools.reduce(operator.add, [random.uniform(-1,1)**2 for _ in us])
    val = [func([None]*d) for _ in range(n) if func([None]*d) <= 1]
    return 2**d*len(val)/n #idk where 2**d is from

def t_vol_dsphere(d):
    r = 1
    return math.pi**(d/2)*r**d/(math.gamma(d/2+1))

for n,d in [(100000,2),(100000, 11)]:
    val = vol_dsphere(n,d)
    t_val = t_vol_dsphere(d)
    print('Approx d sphere: ' + str(val) + ', real val d sphere: ' + str(t_val))


########### MA4 1.3

if __name__ == "__main__":
    t_n_start = perf_counter()
    n_result = vol_dsphere(10000000,11)
    t_n_stop = perf_counter()

    t_p_start = perf_counter()
    with future.ProcessPoolExecutor(10) as ex:
        n = [1000000]*10
        d = [11]*10
        p_result = ex.map(vol_dsphere,n,d)
    t_p_stop = perf_counter()

    print('Time normal: ' + str(t_n_stop-t_n_start) + ', time pararell: ' + str(t_p_stop-t_p_start))

#Time normal: 169.32295240007807, time pararell: 79.65323489997536