# encoding: utf-8
'''
Created on Nov 4, 2018

@author: jyp
'''

import math
from scipy.stats import chi2
print("2.7 Bayes")

def distanceEval(t,th,m,n,r,rh,RL,gama):
    if r==0:
        print((math.log(1-gama)/math.log(RL))*math.pow(t, m))
        tx = (math.log(1-gama)/math.log(RL))*math.pow(t, m) - math.pow(th,m)
        print('-------------------')
        print(math.log(1-gama))
        print(math.log(RL))
        print((math.log(1-gama)/math.log(RL)))
        print(1.2040/0.0513)
        print(math.pow(t, m))
        print(math.pow(th,m))
        print((23.47)*(63095.7) - math.pow(th,m))
        print('-------------------')
    else:
        print((math.pow(t,m)*chi2.isf(1-gama,2*r+2*rh+2))/(-2*math.log(RL)))
        tx = (math.pow(t,m)*chi2.isf(1-gama,2*r+2*rh+2))/(-2*math.log(RL)) - math.pow(th,m)
        print
        
        print('tx',tx)
    return tx;

def pointEval(t,th,m,n,r,rh,Rp,gama):
    if r==0:
        tx = math.log(0.5)*math.pow(t, m)/math.log(Rp) - math.pow(th,m)
        print()
    else:
        tx = (r+rh)*math.pow(t, m)/(-math.log(Rp))-math.pow(th,m)
        print()
    return tx;


def countDistance(tx,t,m):
    n = tx/math.pow(t,m)
    return n;

print("可靠度下限估计")
# t历史实验时间没给
t = 10000
th = 100000
m = 1.2
n = 3
r0 = 0
r1 = 1
rh = 0
Rp = 0.96 
gama = 0.7
tx0 = distanceEval(10000,100000,1.2,3,0,0,0.95,0.7)
print(tx0)
tx1 = distanceEval(10000,100000,1.2,3,1,0,0.95,0.7)
print(tx1)

print("可靠度点估计")

ptx0 = pointEval(t,th,m,n,r0,rh,Rp,gama)
print(ptx0)
ptx1 = pointEval(t,th,m,n,r1,rh,Rp,gama)
print(ptx1)




ptx0 = 468982
cD0 = countDistance(ptx0,t,m);
print(cD0)
ptx1 = 1987982
cD1 = countDistance(ptx1,t,m);
print(cD1)
