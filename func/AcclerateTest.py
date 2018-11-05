'''
Created on Nov 4, 2018

@author: jyp
'''
import math
#from decimal import Decimal
from scipy.stats import chi2 


print('1銆佽瘯楠屾柟妗堣璁�')
print('1.1.1.2(4)')

def getChi2Val(r,n):
    return(chi2.isf(1-r,n));
    
#璁＄畻鍙潬搴︿笅闄愮畻娉�  璁＄畻璇曢獙浜嬩欢
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
#璁＄畻鍙潬搴︾偣浼拌绠楁硶 璁＄畻璇曢獙鏃堕棿
def distancePT(r,rh,R,t,th):
    if r!=0:
        tx = (r+rh)*t/(-math.log(R,math.e))-th
    else:
        tx = math.log(0.5,math.e)*t/math.log(R,math.e)-th
    return tx;
#鍙潬搴︿笅闄�,鐐逛及璁＄畻娉曟祴璇� 璁＄畻鏍锋湰閲� te璇曢獙鏃堕棿
def distanceV(tx,te):
    
    #n = round(Decimal(round(tx/te,1)),0)#鍥涜垗浜斿叆
    n = math.ceil(tx/te)#鍚戜笂鍙栨暣
    return n;

#璁＄畻璇曢獙鎬绘垚鏈�
def allCount(tx,c1,c2):
    nx = round(math.sqrt(c2*tx/c1))
    
    print('test')
    print(nx)
    
    te = round(tx/nx)
    print(te)
    c = c1*nx + c2*te
    return c;

print("(1)瀹氭牱鏈噺")
print("鍙潬搴︿笅闄愮畻娉曟祴璇�")
txe0 = distanceET(0,0,0.7,0.95,10000,100000);
print(txe0)
txe1 = distanceET(1,0,0.7,0.95,10000,100000)
print(txe1)
print("鍙潬搴︾偣浼拌绠楁硶娴嬭瘯")
txp0 = distancePT(0,0,0.96,10000,100000)
print(txp0)
txp1 = distancePT(1,0,0.96,10000,100000)
print(txp1)
print("(2)瀹氳瘯楠屾椂闂�")
#浠诲姟瑕佹眰鏃堕棿
tr = 10000;
print("鍙潬搴︿笅闄愮畻娉曟祴璇�")
print(distanceV(txe0,tr))
print(distanceV(txe1,tr))
print("鍙潬搴︾偣浼拌绠楁硶娴嬭瘯")
print(distanceV(txp0,tr))
print(distanceV(txp1,tr))

print("(3)浼樺寲绠楁硶娴嬭瘯")

print("鍙潬鎬т笅闄愮畻娉�")
print(allCount(txe0,200000,500))
 
