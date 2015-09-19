# Gaussian random numbers 
import math
import random
import sys

# def gaussian_random_num():
# 	u = random.random()
#   v = random.random()
#   w1 = math.sin(2 * pi * v)
#   w2 = math.sqrt(-2 * ln_u)
#   w = w1 * w2

# Box-Muller formula: w = sin(2 pi v) (-2 ln u)^1/2
# set random numbers u and v
# I need to redo this with list comprehensions, probably

num = int(sys.argv[1])
def gaussian_random_num_list(num):
    w_list = []
    pi = math.pi
    for i in range(num):
        u = random.random()
        v = random.random()
        # default log base is e
        ln_u = math.log(u)
        w1 = math.sin(2 * pi * v)
        w2 = math.sqrt(-2 * ln_u)
        w = w1 * w2
        w_list.append(w)
    
    total = 0.0
    item = 0
    while item <= (num-1): 
	    total += w_list[item]
	    item += 1

    print "When %d numbers are generated, the average is %r" % (num, total/num)
    print "The highest is %r" % max(w_list)
    print "The lowest is %r" % min(w_list)

    # test that it actually generates gaussian random numbers 
    # find the difference of each number from the mean, square that value
    new_list = []
    count = 0
    while count <= (num-1): 
	    new_list.append((total/num - w_list[count]) ** 2)
	    count += 1
    
    # find the average of the deviations squared (the variance)
    new_total = 0.0
    item = 0
    while item <= (num-1): 
	    new_total += new_list[item]
	    item += 1
    # the standard deviation is the square root of the variance
    print "The expected std dev is 1"
    print "The measured std dev is %r" % math.sqrt(new_total/num)


gaussian_random_num_list(num)