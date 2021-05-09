from math import *
import numpy as np
import random


def calc(x):
    # y = x * sin(x)
    y = 10 * int(x) - 100
    return y


def init():
    v = [0 for i in range(10)]
    print(v)
    for i in range(10):
        # v[i] = bin(np.random.randint(0, 32))
        v[i] = format(np.random.randint(0, 32), 'b')
        # v[i] = bin(random.randint(0, 32))
        # format()
        # print(type(v[i]))
        # tmp = format(v[i], 'b')
        print('v[' + str(i) + ']: {0:0>5}'.format(v[i]))
        # v[i] = initNum
    return v


def evaluate(v):
    f = [0 for i in range(10)]
    for i in range(10):
        f[i] = calc(v[i])
    return f


def get_fitness(f):
    total = 0
    p = [0.0 for i in range(10)]
    q = [0.0 for i in range(10)]

    # Total Fitness degree
    for i in range(10):
        total += f[i]

    # Select Probability
    for i in range(10):
        p[i] = f[i] / total

    # Accumulated Probability
    for i in range(10):
        q[i] += p[i]

    return p, q


def get_random_list():
    r = [0.0 for i in range(10)]
    r = np.random.rand(10)
    r = r.tolist()
    return r


# random number와 누적 비교, v' 생성
def compare_acc(v, q):
    v_ = [0 for i in range(10)]
    r = get_random_list()
    for i in range(10):
        j = 0
        while True:
            if q[j] < r[i] <= q[j+1]:
                v_[i] = v[j+1]
                break
            j = j + 1

    return v_


def crossover(v_, p, crossover_rate):
    r = get_random_list()
    tmp = sorted(p)
    for i in range(10):
        if p[i] == tmp[0]:
            index1 = i
        if p[i] == tmp[1]:
            index2 = i
    chromosome1 = bin(v_[index1])
    chromosome2 = bin(v_[index2])
    tmp3 = chromosome1

    # crossover
    chromosome1 = chromosome1[0:3] + chromosome2[3:8]
    chromosome2 = chromosome2[0:3] + tmp3[3:8]

    # int형으로 변환
    chromosome1 = int(chromosome1, 2)
    chromosome2 = int(chromosome2, 2)

    v_[index1] = chromosome1
    v_[index2] = chromosome2

    return v_


# print(v)

crossover_rate = 0.25

v = init()
f = evaluate(v)
p, q = get_fitness(f)
v_ = compare_acc(v, q)
v_ = crossover(v_, p, crossover_rate)

