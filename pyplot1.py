#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 13:50:17 2019
-Colatz conjecture pyplot thing
@author: joshuaswanson
"""

import matplotlib.pyplot as plt


def f(x):
    temp = [x]
    c=0
    while x != 1:
        if x%2==0:
            x = x//2
        else:
            x = (x*3)+1
        c+=1
        
    temp.append(c)
    return temp

xcords = []
ycords = []

count = 1
big = []
while count <=100000:
    big.append(f(count))
    xcords.append(f(count)[0])
    ycords.append(f(count)[1])
    count+=1



plt.scatter(xcords,ycords, s=0.0005)
plt.ylabel('Number of Steps')
plt.xlabel('Input Number')
plt.label('Colatz Algorithm Steps')
plt.show()