#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 13:58:08 2020

@author: aidan
"""

import numpy as np

class machine(object):
    def __init__(self, n_):
        #Number of states
        self.n = n_
        
        #List of state objects
        self.lst = []
        
        #What state you are currently in
        self.st = 0
        
        for j in range(n_):
            self.lst.append(state(j))
    
    def __str__(self):
        s = ""
        for j in range(self.n):
            s += str(self.lst[j])
        return s
    
    def run(self, t, p):
        x1 = t.t[p]
        t.t[p] = int(self.lst[self.st].write[x1])
        p += self.lst[self.st].move[x1]
        self.st = self.lst[self.st].state[x1]
        return p
        
    
class state(object):
    def __init__(self, n_):
        self.n = n_
        self.write = np.array([False, False])
        self.move = np.array([0, 0], dtype=np.int16)
        self.state = np.array([0, 0], dtype=int)
        self.halt = np.array([False, False])
        
    def set_write(self, lst):
        self.write = lst
        
    def set_move(self, lst):
        self.move = lst

    def set_state(self, lst):
        self.state = lst
        
    def set_halt(self, lst):
        self.halt = lst
    
    def __str__(self):
        s = str(self.n) + "\n" + str(self.write) + "\n"
        s += str(self.move) + "\n"
        s += str(self.state) + "\n"
        s += str(self.halt) + "\n"
        return s
    
class tape(object):
    def __init__(self, n_):
        self.n = n_
        self.t = np.zeros(n_, dtype=int)
        
        # start in the middle of the tape
        self.start = int(n_//2)
    
        
    
    
        