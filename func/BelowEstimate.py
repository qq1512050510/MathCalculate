# encoding: utf-8
import math
#from decimal import Decimal
#from scipy.stats import f
from scipy.stats import chi2


print('1、试验方案设计')
print('1.1.1.1 (4)')
#计算卡方值
def getX2Val(r,n):
    #卡方分布表
    aList = [0.95,0.9,0.8,0.7,0.5,0.3,0.2,0.1,0.05,0.01,0.001]
    nList = [1,2,3,4,5,6,7,8,9,10]
    lists = [[0.004,0.02,0.06,0.15,0.46,1.07,1.64,2.71,3.84,6.64,10.83], 
             [0.10,0.21,0.45,0.71,1.39,2.41,3.22,4.6,5.99,9.21,13.82], 
             [0.35,0.58,1.01,1.42,2.37,3.66,4.64,6.52,7.82,11.34,16.27],
             [0.71,1.06,1.65,2.2,3.36,4.88,5.99,7.78,9.49,13.28,18.47],
             [1.14,1.61,2.34,3,4.35,6.06,7.29,9.24,11.07,15.09,20.52],
             [1.63,2.2,3.07,3.83,5.35,7.23,8.56,10.64,12.59,16.81,22.46],
             [2.17,2.83,3.82,4.67,6.35,8.38,9.8,12.02,14.07,18.48,24,32],
             [2.73,3.49,4.59,5.53,7.34,9.52,11.03,13.36,15.51,20.09,26.12],
             [3.32,4.17,5.38,6.39,8.34,10.66,12.24,14.68,16.92,21.67,27.88],
             [3.94,4.86,6.18,7.27,9.34,11.78,13.44,15.99,18.31,23.21,29.59]
            ]
    a= round(1-r, 2);
    columnNo = aList.index(a)
    rowNo = nList.index(n)
    return lists[rowNo][columnNo];

def getChi2Val(r,n):
    return(chi2.isf(1-r,n));
    
#计算可靠度下限算法  计算试验事件
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
n=3;
print("(1)定样本量")
print("可靠度下限算法测试")
txe0 = distanceET(0,0,0.7,0.95,10000,100000);
print(txe0)
print(txe0/n)
txe1 = distanceET(1,0,0.7,0.95,10000,100000)
print(txe1)
print(txe1/n)
print("可靠度点估计算法测试")
txp0 = distancePT(0,0,0.96,10000,100000)
print(txp0)
txp1 = distancePT(1,0,0.96,10000,100000)
print(txp1)
print("(2)定试验时间")
#任务要求时间
tr = 10000;
print("可靠度下限算法测试")
print(distanceV(txe0,tr))
print(distanceV(txe1,tr))
print("可靠度点估计算法测试")
print(distanceV(txp0,tr))
print(distanceV(txp1,tr))

print("(3)优化算法测试")

print("可靠性下限算法")
print(allCount(txe0,200000,500))
 
