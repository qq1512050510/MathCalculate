# encoding: utf-8
import math
import tensorflow as tf

print('demo1')
def distanceE(r,rh,gamaV,RL,t,th):
    rA = 2*r+2*rh+2;
    print(rA)
    gamaA = gamaV*rA
    RLA = -2*(math.log(RL,math.e))
    tK = gamaA/RLA
    tA = tK*t-th 
    return tA;
def distanceP(r,rh,RL,t,th):
    return;
sess = tf.Session();
print (sess.run(tf.log(2.718)))
account = sess.run(tf.add(1,10))
print(account)
a = tf.add(2,10)
print(a)
print(sess.run(a))
