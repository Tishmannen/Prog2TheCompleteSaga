import math
import random
import matplotlib.pyplot as plt

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

#pi approx: 3.028
#pi = 3.141592653589793
#pi approx: 3.1496
#pi = 3.141592653589793
#pi approx: 3.14404
#pi = 3.141592653589793