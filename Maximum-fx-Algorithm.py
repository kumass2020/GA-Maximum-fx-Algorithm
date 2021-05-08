from math import *
# import numpy as np
import random


def calc(self, x):
    y = x * sin(x)
    return y


v = [0 for i in range(10)]
print(v)
for i in range(10):
    # v[i] = bin(np.random.randint(0, 32))
    v[i] = format(random.randint(0, 32), 'b')
    # v[i] = bin(random.randint(0, 32))
    # format()
    # print(type(v[i]))
    # tmp = format(v[i], 'b')
    print('{0:0>5}'.format(v[i]))
    # v[i] = initNum

print(v)



