'''
Created on 2018年11月8日

@author: Yang
'''
#import math
from math import sqrt
from scipy.stats import norm
from scipy.stats import nct
#from sympy import * #符号库，计算积分
from scipy.optimize import fsolve


def CalOmegal(RL):
    omegal = float('%.2f'% (norm.ppf(RL)))
    return omegal

#根据样本量n,求K
def sigSideCalK(RL,gama,n):
    omegal = CalOmegal(RL)
    K = float('%.6f' % (nct.ppf(gama,n-1,omegal*sqrt(n))/sqrt(n)))
    # print('K=',K)
    return K

#根据强度系数K，求n
def calSamNum(RL,gama,K):
    omegal = CalOmegal(RL)
    Kpie = float('%.6f' % (nct.ppf(gama,999999,omegal* sqrt(1000000))/ sqrt(1000000)))
    if (K < Kpie):
        print('剩余强度系数取值过小，无法计算')
        return 
    for n in range(2,7):#100000
        x = nct.ppf(gama,n-1,sqrt(n)*omegal)
        diffValue = abs(sqrt(n)*K - x)
        if diffValue < 0.5: #n的数量是由于四舍五入导致的误差，所以把误差精度控制在0.5
            print('样本量n=',n)
            print(diffValue)
            break
    if(n >= 1000000):
        print('计算样本数量失败，调大相差值误差范围')
    return n
          
#单侧限可靠度下限;根据样本量n和下限，求性能样本均值
def sigSideRLnLCalMean(RL,gama,n,L,s):
    K = sigSideCalK(RL,gama,n)
    xMean =  L + (K * s)
    print('单侧限可靠度下限;根据样本量n和下限，，','K=',K,' ','寿命样本均值',' ',xMean)
    return xMean 
  
#单侧限可靠度下限;根据样本量n和上限，求性能样本均值
def sigSideRLnUCalMean(RL,gama,n,U,s):
    K = sigSideCalK(RL,gama,n)
    xMean =  U - (K * s)
    print('单侧限可靠度下限;根据样本量n和上限，','K=',K,' ','寿命样本均值',' ',xMean)
    return xMean  

#单侧限可靠度下限;根据K和上限，求n再反求K，求性能样本均值
def sigSideRLkUCalMean(RL,gama,K,U,s):
    n = calSamNum(RL,gama,K)
    K = sigSideCalK(RL,gama,n)
    xMean =  U - (K * s)
    print('单侧限可靠度下限;根据K和上限，求n再反求K，','K=',K,' ','寿命样本均值',' ',xMean)
    return xMean  

#单侧限可靠度下限;根据K和下限，求n再反求K，求性能样本均值
def sigSideRLkLCalMean(RL,gama,K,L,s):
    n = calSamNum(RL,gama,K)
    K = sigSideCalK(RL,gama,n)
    xMean = float('%.6f' % (L + (K * s)))
    print('侧限可靠度下限;根据K和下限，求n再反求K，','K=',K,' ','寿命样本均值',' ',xMean)
    return xMean 

#单侧限可靠度点估计；已知上限，求均值
def sigSideRPUCalMean(R,U,s):
    K = CalOmegal(R)
    xMean = float('%.6f' % (U - K * s))
    print('可靠点估计,已知上限，','K=',K,' ','寿命样本均值',' ',xMean)
    
#单侧限可靠度点估计；已知下限，求均值
def sigSideRPLCalMean(R,L,s):
    K = CalOmegal(R)
    xMean = float('%.6f' % (L + K * s))
    print('可靠点估计,已知下限，','K=',K,' ','寿命样本均值',' ',xMean)

#双侧限，已知可考度下限和置信度，样本量，上限
def dulSideRLnUCalMean(RL,gama,n,U,s):
    RLL = RLU = 1 - (1-RL)/2
    K = sigSideCalK(RLL,gama,n)
    xMean = float('%.6f' % (U - K * s))
    print('双侧限可靠度下限，已知n求K，上限已知','寿命均值',RLL, K, xMean)
    return (RLL, RLU, K, xMean)

#双侧限，已知可靠度下限和置信度，样本量，下限
def dulSideRLnLCalMean(RL,gama,n,L,s):
    RLL = RLU = 1 - (1-RL)/2
    K = sigSideCalK(RLL,gama,n)
    xMean = float('%.6f' % (L + K * s))
    print('双侧限可靠度下限，已知n求K，下限已知','寿命均值',RLL, K, xMean)
    return (RLL, RLU, K, xMean)

#双侧限，已知可靠度下限和置信度，求n再反求K，上限
def dulSideRLkLCalMean(RL,gama,K,L,s):
    RLL = RLU = 1 - (1-RL)/2
    print(RLL)
    n = calSamNum(RLL,gama,K)
    K = sigSideCalK(RLL,gama,n)
    xMean =  L + (K * s)
    print('双侧限可靠度下限，已知K求n再反求K，下限已知','寿命均值',RLL, K, xMean)
    return (RLL, RLU, K, xMean)
    
#双侧限，已知可靠度下限和置信度，求n再反求K，上限
def dulSideRLkUCalMean(RL,gama,K,U,s):
    RLL = RLU = 1 - (1-RL)/2
    print(RLL)
    n = calSamNum(RLL,gama,K)
    K = sigSideCalK(RLL,gama,n)
    xMean =  U - (K * s)
    print('双侧限可靠度下限，已知K求n再反求K，下限已知','寿命均值',RLL, K, xMean)
    return (RLL, RLU, K, xMean)

#计算符号化正态分布的分布函数，与fsolve一起求解
def calF(x,L,U,R,s):
    return norm.cdf((U-x)/s)+ norm.cdf((x-L)/s)-1-R
#双侧限可考度点估计
def dulSidecalRPNormF(L,U,R,s):
    for i in range(L,U):
        #fsolve参数：第一位函数名，第二个是人为设置试验的初始值，剩下的参数是calF的参数，默认有x,不用写x
        #fsolve有两个值，分别从低到高试探，得到值则退出
        xL = fsolve(calF, i,(L,U,R,s))
        i = i + 25
        if (xL != None):
            print('寿命样本均值xL',xL)
        break
    j = U
    while(j > L):
        xU = fsolve(calF, j,(L,U,R,s))
        j = i - 25
        if (xU != None):
            print('寿命样本均值xU',xU)
        break  
    return(xL,xU)
        

sigSideRLnLCalMean(0.95,0.7,10,200,10)
sigSideRLnUCalMean(0.95,0.7,10,500,10)
sigSideRLkUCalMean(0.95,0.7,3,500,10)
sigSideRLkLCalMean(0.95,0.7,3,200,10)
sigSideRPUCalMean(0.98,500,10)
sigSideRPLCalMean(0.98,200,10)
dulSideRLnUCalMean(0.95,0.7,10,500,10)
dulSideRLnLCalMean(0.95,0.7,10,200,10)
dulSideRLkLCalMean(0.95,0.7,3,200,10)
dulSideRLkUCalMean(0.95,0.7,3,500,10)
dulSidecalRPNormF(300,500,0.98,10)
#完整版



