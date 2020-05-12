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
plt.title("ECG")


yline = input();
ysplit = re.split(" ", yline)
#map进行类型转换
y = list(map(eval,ysplit))
x = np.arange(0, len(y))
print(len(x))
print(y)
print(x)
plt.title("ECG")

# fontproperties 设置中文显示，fontsize 设置字体大小
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y)
plt.show()
