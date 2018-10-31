# encoding: utf-8
import numpy as np
import math

print('测试')
def distanceE(r,rh,gamaV,RL,t,th):
    rA = 2*r+2*rh+2;
    print(rA)
    gamaA = gamaV*rA
    RLA = -2*(math.log(RL,math.e))
    tK = gamaA/RLA
    tA = tK*t-th 
    return tA;

