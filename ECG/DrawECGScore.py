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
"""
x = [0, 10, 10.01, 20, 20.01, 25, 25.01, 30, 30.01, 35, 40, 40.01, 50, 60]
y = [0, 0, 0.2, 0.2, 0.35, 0.35, 0.4, 0.4, 0.8, 0.8, 0.8, 1, 1, 1]
"""

x = [0, 30, 30.01, 35, 35.01, 40, 40.01, 45, 45.01, 60]
y = [0, 0, 0.3, 0.3, 0.8, 0.8, 0.4, 0.4, 0.9, 0.9]
# x = np.arange(0, 70, 10)
print(len(x))
print(y)
print(x)

# fontproperties 设置中文显示，fontsize 设置字体大小
plt.xlabel("时间/秒")
plt.ylabel("分类得分")
plt.plot(x, y)
plt.yticks((0, 0.5, 1))
plt.show()
