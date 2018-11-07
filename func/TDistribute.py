#-*-coding:utf-8 -*-
'''
Created on 2018年11月6日
方程求解

@author: adp
'''
from scipy.stats import t;
import math

r = 0.7
wl = 1.6449
n = 10;
#print(t.isf(1-r,n-1)+math.sqrt(n)*wl)
#print(math.sqrt(n))
#print((t.isf(1-r,n-1)+math.sqrt(n)*wl)/math.sqrt(n))

from scipy.integrate import odeint 
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import root,fsolve 
from scipy.stats import nct
from scipy.stats import chi2
#plt.rc('text', usetex=True) 
#使用latex ## 使用scipy.optimize模块的root和fsolve函数进行数值求解方程 #
# 1、求解f(x)=2*sin(x)-x+1 
rangex1 = np.linspace(-2,8) 
rangey1_1,rangey1_2 = 2*np.sin(rangex1),rangex1-1 
plt.figure(1) 
plt.plot(rangex1,rangey1_1,'r',rangex1,rangey1_2,'b--') 
plt.title('$2sin(x)$ and $x-1$') 
def f1(x): 
    return np.sin(x)*2-x+1 
sol1_root = root(f1,[2]) 
sol1_fsolve = fsolve(f1,[2]) 
print(f1(sol1_fsolve))
print(123)
print(sol1_fsolve)
plt.scatter(sol1_fsolve,2*np.sin(sol1_fsolve),linewidths=9) 
#plt.show()





def f2(x):
    return np.array([3*x[0]+2*x[1]-3,x[0]-2*x[1]-5]) 
sol2_root = root(f2,[0,0]) 
sol2_fsolve = fsolve(f2,[0,0]) 
print(sol2_fsolve) 
# [2. -1.5] 
a = np.array([[3,2],[1,-2]]) 
b = np.array([3,5]) 
x = np.linalg.solve(a,b) 
print(x) 
# [2. -1.5]



## 4、非线性方程 
def f4(x): 
    return np.array(np.sin(2*x-np.pi)*np.exp(-x/5)-np.sin(x)) 
init_guess =np.array([[0],[3],[6],[9]]) 
sol4_root = root(f4,init_guess) 
sol4_fsolve = fsolve(f4,init_guess) 
print(sol4_fsolve)

omegal = 1.6449;
#[r,omegal]
vF = [0.7,1.6449,10]
def ftest(x)->vF:
    #nct.pdf(x, df, nc, loc=0, scale=1)
    #nct.ppf(gama,n-1,omegal*math.sqrt(n));
    #nct.ppf(q, df, nc, loc=0, scale=1)
    #nct.pdf(x,n-1,omegal*math.sqrt(n));
    return nct.pdf(x,vF[2]-1,vF[1]*math.sqrt(n));

p_root = root(ftest,[0.09537223630811965]) 
p_solve = fsolve(ftest,[0.09537223630811965]) 
print('----------')
n = 3
print(math.sqrt(n)*2.8092)
print(p_root)
print(p_solve)
#print(p_solve)
print('----------')

tt = [123,2];
def test(x)->tt:
    #nct.pdf(x, df, nc, loc=0, scale=1)
    #nct.ppf(gama,n-1,omegal*math.sqrt(n));
    #nct.ppf(q, df, nc, loc=0, scale=1)
    return tt[0]*x
print(test(1))




def pTest(a)->tt:
    return chi2.isf(a,tt[1])

print(pTest(0.7))
p_root = root(pTest,[0.7133498878774649]) 
p_solve = fsolve(pTest,[0.7133498878774649]) 
print(p_root)
print(p_solve)