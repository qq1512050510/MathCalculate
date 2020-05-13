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
# myfont = fm.FontProperties(fname=r'D:\Fonts\simkai.ttf')

#plt.title("ECG")
x = [0, 10, 20, 29.9, 30, 40, 50, 60]
y = [0, 0, 0, 0, 1, 1, 1, 1]
# x = np.arange(0, 70, 10)
print(len(x))
print(y)
print(x)
#plt.title("原始ECG信号的实际分类标签", y=-1)

# fontproperties 设置中文显示，fontsize 设置字体大小
plt.xlabel("时间/秒")
plt.ylabel("实际标签")
plt.plot(x, y)
plt.yticks((0, 0.5, 1))
plt.show()
