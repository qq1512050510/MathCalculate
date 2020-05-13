# -*- coding: utf-8 -*-
"""
Spyder 编辑器
ECG 文件处理

"""
from matplotlib import pyplot as plt
import numpy as np
import re
import matplotlib


# fname 为 你下载的字体库路径，注意 SimHei.ttf 字体的路径

# fname 为 你下载的字体库路径，注意 SimHei.ttf 字体的路径

plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['font.serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False
#myfont = fm.FontProperties(fname=r'D:\Fonts\simkai.ttf')

plt.title("ECG")

file = open("D:\DISK\ECG数据\MIT-BIH-data\\05261dat.txt", 'r')

target1 = 4379905
target2 = 4394905
i = 1;
list = [];
for line in file.readlines():
    if i >= target1 and i <= target2:
        lineList = re.split(" |\x09", line)
        list.append(float(lineList[-2]))
    if i > target2:
        break
    i += 1
print(list)
# map进行类型转换
y = list
x = np.arange(0, 60, float(60) / float(len(y)))
print(len(x))
print(y)
print(x)
plt.title("ECG")

# fontproperties 设置中文显示，fontsize 设置字体大小
plt.xlabel("时间/秒")
plt.ylabel("原始信号")
plt.plot(x, y)
plt.show()
