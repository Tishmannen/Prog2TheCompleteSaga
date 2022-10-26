import concurrent.futures as future
import operator
import random
import functools
from time import perf_counter

def vol_dsphere(n,d):
    func = lambda us: functools.reduce(operator.add, [random.uniform(-1,1)**2 for _ in us])
    val = [func([None]*d) for _ in range(n) if func([None]*d) <= 1]
    return 2**d*len(val)/n

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
#Pararell is faster since it runs in pararell over smaller n