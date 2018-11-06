'''
Created on 2018年11月5日

@author: Yang
'''
import math
from scipy.stats import norm
from scipy.stats import nct

#已知正态分布密度函数面积，求分位点，参数只需要概率值
def getNormVal(r):
    return (norm.ppf(r))

#可靠度下限算法，根据样本量n,求剩余强度系数K和寿命均值
def distanceETCalTime(RL,gama,n,t,s):
    #根据正态分布概率值，求分位点；omegal
    #'%.4f'控制小数的精度，标准的四舍五入，round()函数逢5如果前面是偶数就舍掉了
    omegal = float('%.4f' % (norm.ppf(RL)))
    print(omegal)
    #非中心t分布，参数: 概率值，自由度，非中心参数
    K = float('%.4f' % (nct.ppf(gama,n-1,omegal*math.sqrt(n))/math.sqrt(n)))
    print(K)
    xMean =  t + (K * s)
    return(xMean)

#可靠度下限算法，根据剩余强度系数K，求样本量和寿命均值
def distanceETCalNum(RL,gama,K,t,s):
    omegal = float('%.4f' % (norm.ppf(RL)))
    print (10/8)

print(distanceETCalTime(0.95,0.7,10,1000,10));
