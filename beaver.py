#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 13:57:19 2020

@author: aidan
"""

import numpy as np
import turing

n = 2
m = turing.machine(n)
t = turing.tape(20)

m.lst[0].set_write([1,1])
m.lst[1].set_write([1,1])
m.lst[0].set_move([1,-1])
m.lst[1].set_move([-1, 0])

m.lst[0].set_halt([False, False])
m.lst[1].set_halt([False, True])
m.lst[0].set_state([1, 0])
m.lst[1].set_state([0, 1])


#Current space
pos = t.start

while(m.lst[m.st].halt[t.t[pos]] == False):
    pos = m.run(t, pos)

print(sum(t.t))
