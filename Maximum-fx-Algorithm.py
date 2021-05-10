from math import *
import numpy as np
import random


def calc(x):
    # y = x * sin(x)

    # if int(x, 2) < 10:
    #     x = bin(np.random.randint(10, 32))

    y = 10 * int(str(x), 2) - 100

    # 함수값 음수 나오면 안되는지..?
    if y < 0:
        y = 0
        print("음수")

    return y


def init():
    v = [0 for i in range(10)]
    print(v)
    for i in range(10):
        # v[i] = bin(np.random.randint(0, 32))

        # v[i] = format(np.random.randint(10, 32), 'b')
        v[i] = bin(np.random.randint(10, 32))

        # print(type(v[i]))
        print('v[' + str(i) + ']: {0:0>5}'.format((v[i])[2:]))
    return v


def evaluate(v):
    f = [str(0) for i in range(10)]
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
        if i == 0:
            q[i] = p[i]
        else:
            q[i] = q[i-1] + p[i]
    return p, q


def get_random_list():
    r = [0.0 for i in range(10)]
    r = np.random.rand(10)
    r = r.tolist()
    return r


# random number와 누적 비교, v' 생성
def compare_acc(v, q):
    v_ = [str(0) for i in range(10)]
    r = get_random_list()
    for i in range(10):
        j = 0
        while j < 9:
            if q[j] < r[i] <= q[j+1]:
                v_[i] = v[j+1]
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
    chromosome1 = v_[index1]
    chromosome2 = v_[index2]
    tmp3 = chromosome1

    # crossover
    chromosome1 = chromosome1[0:3] + chromosome2[3:8]
    chromosome2 = chromosome2[0:3] + tmp3[3:8]

    v_[index1] = chromosome1
    v_[index2] = chromosome2

    return v_


def mutate(v_, mutation_quantity):
    index_list = [np.random.randint(0, 10) for i in range(10)]
    for i in range(mutation_quantity):
        randnum = np.random.randint(2, 8)
        a = list(a)
        if a[randnum] == '0':
            a[randnum] = '1'
        elif a[randnum]
        v_[index_list] = (v_[index_list])


# print(v)

loop = 100
crossover_rate = 0.25
mutation_quantity = 5

v = init()

for i in range(loop):
    if i != 0:
        v = v_
        # f = []
        # p = []
        # q = []
        # v_ = []

    f = evaluate(v)
    p, q = get_fitness(f)
    v_ = compare_acc(v, q)
    v_ = crossover(v_, p, crossover_rate)
    print(q)
    print(v_)


