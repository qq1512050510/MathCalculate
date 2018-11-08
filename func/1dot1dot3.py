'''
Created on 2018年11月5日

@author: Yang
'''
import math
from scipy.stats import norm
from scipy.stats import nct

#已知正态分布密度函数面积，求分位点，参数只需要概率值

#可靠度下限算法，根据样本量n,求剩余强度系数K和寿命均值
def distanceETCalTime(RL,gama,n,t,s):
    #根据正态分布概率值，求分位点；omegal
    #'%.4f'控制小数的精度，标准的四舍五入，round()函数逢5如果前面是偶数就舍掉了
    omegal = float('%.4f' % (norm.ppf(RL)))
    #非中心t分布，参数: 概率值，自由度，非中心参数
    K = float('%.4f' % (nct.ppf(gama,n-1,omegal*math.sqrt(n))/math.sqrt(n)))
    xMean =  t + (K * s)
    print('K=',K,' ','寿命样本均值',' ',xMean)
    return xMean 

#可靠度下限算法，根据剩余强度系数K，求样本量和寿命均值
def distanceETCalNum(RL,gama,K,t,s):
    omegal = float('%.4f' % (norm.ppf(RL)))
    sampNum = calSamNum(gama,omegal,K)
    K = float('%.4f' % (nct.ppf(gama, sampNum-1, math.sqrt(sampNum)*omegal)/math.sqrt(sampNum)))
    print('K=' , K)
    xMean = t + K * s
    print('n=',sampNum,' ','寿命样本均值',' ',xMean)
    return(sampNum , xMean)

#根据强度系数K，求样本量
def calSamNum(gama,omegal,K):
    for n in range(2,10000000):
        x = nct.ppf(gama,n-1,math.sqrt(n)*omegal)
        diffValue = abs(math.sqrt(n)*K - x)
        if diffValue < 0.5: #n的数量是由于四舍五入导致的误差，所以把误差精度控制在0.5
            print('样本量n=',n)
            return n
  
#可靠度点估计，计算寿命样本均值
def distancePTCalTime(R,t,s):
    K =  float('%.4f' % (norm.ppf(R)))
    xMean = t + K *s
    print('寿命样本均值',xMean)
    return xMean

print('可靠度下限算法')
distanceETCalTime(0.95,0.7,10,1000,10)
distanceETCalNum(0.95,0.7,3,1000,10)
print('可靠度点估计')
distancePTCalTime(0.98,1000,10)


