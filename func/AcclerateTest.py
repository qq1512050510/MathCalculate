'''
Created on Nov 4, 2018

@author: yp
'''
import math
#from decimal import Decimal
from scipy.stats import chi2
import scipy.constants as C

print('1、试验方案设计')
print('1.1.1.2(4)')

def getChi2Val(r,n):
    return(chi2.isf(1-r,n));
    
#计算可靠度下限算法  计算试验时间
def distanceET(r,rh,gamaV,RL,t,th):
    if r!=0:
        n = 2*r+2*rh+2;
        gamaP = getChi2Val(gamaV, n)
        #print(gamaP)
        RLA = -2*(math.log(RL,math.e))
        tK = gamaP/RLA
        tx = tK*t-th 
    else:
        upValue = math.log((1-gamaV),math.e)
        downValue = math.log(RL,math.e)
        tx = (upValue/downValue)*t-th
    return tx;
#计算可靠度点估计算法 计算试验时间
def distancePT(r,rh,R,t,th):
    if r!=0:
        tx = (r+rh)*t/(-math.log(R,math.e))-th
    else:
        tx = math.log(0.5,math.e)*t/math.log(R,math.e)-th
    return tx;
#可靠度下限,点估计算法测试 计算样本量 te试验时间
def distanceV(tx,te):
    
    #n = round(Decimal(round(tx/te,1)),0)#四舍五入
    n = math.ceil(tx/te)#向上取整
    return n;

#计算试验总成本
def allCount(tx,c1,c2):
    nx = round(math.sqrt(c2*tx/c1))
    
    print('test')
    print(nx)
    
    te = round(tx/nx)
    print(te)
    c = c1*nx + c2*te
    return c;
def calAF(Ea,T0,T):
    Ea = Ea*1.60*1e-19
    T0 = T0 + 273.15
    T = T + 273.15
    AF = math.exp((1/T0-1/T)*Ea/C.k)
    return AF;
def Caln(te,tx,AF):
    n = tx/(te*AF)
    return math.ceil(n);
print("(4)数值例")

Ea = 1
T0 = 25
T = 49.7
n = 3
AF = calAF(Ea,T0,T);
print(AF)


print("(1)定样本量")
print("可靠度下限算法测试")
txe0 = distanceET(0,0,0.7,0.95,10000,100000);
print(txe0)
txxe0 = txe0/(n*AF)
print(txxe0)

txe1 = distanceET(1,0,0.7,0.95,10000,100000)
print(txe1)

txxe1 = txe1/(n*AF)
print(txxe1)

print("可靠度点估计算法测试")
txp0 = distancePT(0,0,0.96,10000,100000)
print(txp0)
te0 = txp0/(n*AF)
print(te0)
txp1 = distancePT(1,0,0.96,10000,100000)
print(txp1)
te1 = txp1/(n*AF)
print(te1)
print("(2)定试验时间")
#任务要求时间
tr = 10000;
print("可靠度下限算法测试")
print(distanceV(txe0,tr))
print(distanceV(txe1,tr))
print("可靠度点估计算法测试")
print(distanceV(txp0,tr))
print(distanceV(txp1,tr))

print("(2)定试验事件")
tE =  1000
r0 = 0
r1 = 1
print(Caln(tE,txe0,AF))
print(Caln(tE,txe1,AF))

print(Caln(tE,txp0,AF))
print(Caln(tE,txp1,AF))
 
