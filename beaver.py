#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 13:57:19 2020

@author: aidan
"""

import time
import numpy as np
from random import *
import turing

t0 = time.time()
n = 3
N1 = 200
N2 = 10000
m = turing.machine(n)
t = turing.tape(int(2.1*N1))

'''
2 state solution
m.lst[0].set_write([1,1])
m.lst[1].set_write([1,1])
m.lst[0].set_move([1,-1])
m.lst[1].set_move([-1, 0]
m.lst[0].set_halt([False, False])
m.lst[1].set_halt([False, True])
m.lst[0].set_state([1, 0])
m.lst[1].set_state([0, 1])
'''

scores = [1]

for i in range(N2):
    t = turing.tape(int(2.1*N1))
    halt_flag = True
    
    #Random guessing
    for j in range(n):
        m.lst[j].set_write([randint(0,1), randint(0,1)])
        m.lst[j].set_move([randint(-1,1), randint(-1,1)])
        m.lst[j].set_state([randint(0,n-1), randint(0,n-1)])
        m.lst[j].set_halt([False, False])
    
    #Set the halt
    m.lst[randint(0,n-1)].set_halt([False, True])
    
    #Current space
    pos = t.start
    
    #Iteration count
    count = 0
    
    while(m.lst[m.st].halt[t.t[pos]] == False):
        pos = m.run(t, pos)
        count += 1
        if (count > N1):
            halt_flag = False
            break
    
    score = sum(t.t)
    if (halt_flag):
        if (score > max(scores)):
            print(score)
            print(m)
        scores.append(score)


scores.sort()
print("Highscore: ", scores[-1])
print("Time: %.2f" %(time.time() - t0))
