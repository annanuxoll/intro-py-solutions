#Gaussian random numbers 
import math
import random
import sys

# def gaussian_random_num():
# 	u = random.random()
#     v = random.random()
#     w1 = math.sin(2 * pi * v)
#     w2 = math.sqrt(-2 * ln_u)
#     w = w1 * w2
#     print w

# Box-Muller formula: w = sin(2 pi v) (-2 ln u)^1/2
#set random numbers u and v

num = int(sys.argv[1])
def gaussian_random_num_list(num):
    w_list = []
    pi = math.pi
    e = math.e

    for i in range(num):
        u = random.random()
        v = random.random()
        # default log base is e
        ln_u = math.log(u)
        w1 = math.sin(2 * pi * v)
        w2 = math.sqrt(-2 * ln_u)
        w = w1 * w2
        w_list.append(w)
    total = 0
    item = 0
    while item <= (num-1): 
	    total += w_list[item]
	    item += 1
    print "When %d numbers are generated, the average is %d" % (num, total/num)
    print "The highest is %d" % max(w_list)
    print "The lowest is %d" % min(w_list)

gaussian_random_num_list(num)