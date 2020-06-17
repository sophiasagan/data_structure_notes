#iterative

# To Analyze
# 1. does number of steps increase if input size increases?
# 2. go line by line, figure out big-O of each line and add
# 3. If loop: 
    # 3.1 look at code inseide loop and repeat step 2
    # 3.2 calculate how many time the loop will run
    # 3.3 reuslt of 3.1 x result of 3.2

#--Reference: https://www.bigocheatsheet.com/ --
#--Reference: http://pythontutor.com/visualize.html#mode=edit --

import math
from math import sqrt

# Constant time == O(1)
def mult_2(n): # O(1) + O(1) = 0(2) => O(1)
    print(n) # O(1)
    if n == 5:# O(1)
        print("hooray")# O(1)
    return n * 2 # O(1)


# Linear time == O(n)
def foo(n): #O(n)
    for i in range(0, n): # O(n)
        # the total runtime of the code in the loop is O(1)
        print(i)# O(1)
        print(i)# O(1)


# Quadratic time (Polynomial time)
def bar(n): #O(1) + O(n^2) + O(1) ==> O(n^2)
    s = 0 # O(1)

    # O(n) * O(n) = O(n^2)
    for i in range(0,n): #O(n)
        for j in range(0,n): # O(n) * O(1) = O(n) this loop runs in linear time
            s += i * j # O(1)

    return s #O(1)


# O(n) * O(sqrt(n)) == O(n * sqrt n) == O(n ^ 1.5)
def baz(n):
    s = 0

    for i in range(n): # O(n)
        for j in range(int(sqrt(n))): #0(sqrt(n)) or O(n^0.5)
            s += i * j # O(1)

    return s


# When the input is halved (or another division) every step of the loop
# Think logarithmic!
# log(n)
def divider(n):
    while n >= 1: # O(log(n))
        print(n) # O(1)
        n = n // 2  # O(1)

        # n = 8
        # number of steps = 3

        # n = 16
        # number of steps = 4

        #n = 32
        # number of steps = 5 


