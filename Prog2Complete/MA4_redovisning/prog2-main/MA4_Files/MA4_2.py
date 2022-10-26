#!/usr/bin/env python3.9

from numba import njit
from time import perf_counter
import matplotlib.pyplot as plt
from person import Person

def main():
	times = {'t_py':[],'t_cpp':[],'t_numba':[]}
	N = list(range(30,46))
	for n in N:
		t_start = perf_counter()
		f = Person(n)
		f.fib()
		t_stop = perf_counter()
		times['t_cpp'].append(t_stop-t_start)

		t_start = perf_counter()
		fib_py(n)
		t_stop = perf_counter()
		times['t_py'].append(t_stop-t_start)

		t_start = perf_counter()
		fib_numba(n)
		t_stop = perf_counter()
		times['t_numba'].append(t_stop-t_start)

#		print(f'First for loop, n = {n}')

	plt.figure(1)
	plt.plot(N,times['t_py'],N,times['t_numba'],N,times['t_cpp'])
	plt.xlabel('n')
	plt.ylabel('Time [s]')
	plt.title('Times for fibonacci for different languages')
	plt.legend(['Python', 'Numba', 'C++'])
	plt.savefig('MA4_triplecompare.png')

	times_2 = {'t_py':[],'t_numba':[]}
	N_2 = list(range(20,31))
	for n in N_2:
		t_start = perf_counter()
		fib_py(n)
		t_stop = perf_counter()
		times_2['t_py'].append(t_stop-t_start)

		t_start = perf_counter()
		fib_numba(n)
		t_stop = perf_counter()
		times_2['t_numba'].append(t_stop-t_start)

#		print(f'Second for loop, n = {n}')

	plt.figure(2)
	plt.plot(N_2,times_2['t_py'],N_2,times_2['t_numba'])
	plt.xlabel('n')
	plt.ylabel('Time [s]')
	plt.title('Times for fibonacci')
	plt.legend(['Python', 'Numba'])
	plt.savefig('MA4_doublecompare.png')

	n = 47
	val_numba = fib_numba(n)
	f = Person(n)
	val_cpp = f.fib()
	print(f'Value for numba with n = {n}: {val_numba}\nValue for C++ with n = {n}: {val_cpp}')
#Value for numba with n=47: 2971215073
#Value for C++ with n=47: -1323752223

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1)+fib_py(n-2))

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return(fib_numba(n-1)+fib_numba(n-2))

if __name__ == '__main__':
	main()
