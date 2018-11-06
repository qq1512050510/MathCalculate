'''
Created on 2018年11月5日

@author: Yang
'''
import math
from scipy.stats import norm
from scipy.stats import nct
from scipy.stats import t

#已知正态分布密度函数面积，求分位点，参数只需要概率值
def getNormVal(r):
    return (norm.ppf(r))

#非中心t分布，参数 概率值，自由度，非中心参数
print((nct.ppf(0.7,9,5.201630523210968))/math.sqrt(10))
print('###',t.ppf(0.8,9))
#print (t.ppf(0.7,9)*np.sqrt(10)+5.2)

test = getNormVal(0.95)
#print('****',test)
print(pow(10,0.5)*1.6449)
print(math.sqrt(10))

