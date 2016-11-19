#!/bin/python

import sys
from itertools import izip, cycle

x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

def get_generator(x, v):
    while True:     
        yield x
        x = x + v

if v1 > v2:
    fast = get_generator(x1, v1)
    slow = get_generator(x2, v2)
else:
    fast = get_generator(x2, v2)
    slow = get_generator(x1, v1)
    
for loca1, loca2 in izip(cycle(fast), cycle(slow)):
    if loca1 == loca2:
        print "YES"
        break
    elif loca1 > loca2:
        print "NO"
        break
    continue