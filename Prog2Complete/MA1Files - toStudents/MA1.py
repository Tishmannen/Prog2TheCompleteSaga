"""
Solutions to module 1
Student: Thor Lindberg
Mail: thor.ronnegard@gmail.com
Reviewed by: Tom
Reviewed date: 05/09-2022
"""

import random
import time


def power(x, n):         # Optional
    pass


def multiply(m, n):      # Compulsory
    if n == 0 or m == 0:
        return 0
    else:
        return m+multiply(m,n-1)


def divide(t, n):        # Optional
    pass


def harmonic(n):         # Compulsory
    if n == 1:
        return 1
    else:
        return 1/n+harmonic(n-1)


def digit_sum(x):        # Optional
    pass


def get_binary(x):       # Optional
    pass


def reverse(s):          # Optional
    pass


def largest(a):          # Compulsory
    if len(a) <= 1:
        return a[0]
    elif a[0] <= a[1]:
        return largest(a[1:])
    else:
        return largest([a[0]]+a[2:])


def count(x, s):         # Compulsory
    if s == []:
        return 0
    if type(s[-1]) == list:
        if s[-1] == x:
            return 1+count(x,s[:-1])
        else:
            return count(x,s[-1])+count(x,s[:-1])
    else:
        if s[-1] == x:
            return 1+count(x,s[:-1])
        else:
            return count(x,s[:-1])
    

def zippa(l1, l2):       # Compulsorys
    if len(l1) == 0 or len(l2) == 0:
        return [*l1,*l2]
    else:
        return [l1[0], *zippa(l2,l1[1:])]


def bricklek(f, t, h, n): # Compulsory
    if n == 1:
        return [f+'->'+t]
    else:
        return bricklek(f,h,t,n-1)+[f+'->'+t]+bricklek(h,t,f,n-1)


def main():
    """ Demonstates my implementations """
    # Write your demonstration code here
    print('Bye!')
    

if __name__ == "__main__":
    main()
    
####################################################    
    
"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 16: Time for bricklek with 50 bricks:
  #2^50-1= 35.7 million years
  
  
  
  
  Exercise 17: Time for Fibonacci:

a)

Code for excercise 17:
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

import time
def fib_time(n):
    tstart = time.perf_counter()
    fib(n)
    tstop = time.perf_counter()
    print ( f" Measured time : {tstop - tstart } seconds with n = : {n}")

    
for i in range(2,22,2):
    fib_time(i)


TIMES:

  n=2:  3.90e-6
  n=4:  5.30e-6
  n=6:  1.05e-5
  n=8:  2.46e-5
  n=10: 6.24e-5
  n=12: 1.61e-4
  n=14: 4.17e-4
  n=16: 1.09e-3
  n=18: 2.86e-3
  n=20: 7.71e-3

should be 2.61
5.3/3.9=1.36
10.5/5.30=1.98
24.6/10.5=2.34
6.24/2.46=2.54
16.1/6.24=2.58
4.17/1.61=2.59
10.9/4.17=2.61
2.86/1.09=2.62
7.71/2.86=2.70
It seems to be correct

b)
n=20: 7.71e-3s -> n=50: 7.71e-3*1.618e30=14335s = 3h59m
n=100: 7.71e-3*1.618e80 = 12.8 million years

  Exercise 20: Comparison sorting methods:

  Sticksort:
  t(1000) = 1s
  c = 1/1000^2
  t(10^6) = (10^6)^2/1000^2 = 11.6 days
  t(10^9) = (10^9)^2/1000^2 = 31700 years
  
  Mergesort:
  t(1000) = 1s
  c = 1/(1000*log(1000))
  t(10^6) = 10^6*log(10^6)*c = 33min 20s
  t(10^9) = 10^9*log(10^9)*c = 34.7 days
  
  Exercise 21: Comparison Theta(n) and Theta(n log n)
  c = 1/(10*log(10))
  A=B <=> 1/(10*log(10))*n*log(n) = n
  <=> n = 10^10
  Answer: n > 10^10
  
  
  
  
  
  
  





"""