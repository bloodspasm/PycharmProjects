# -*- coding:gb2312 -*-
import numpy as np
a = np.arange(10, 41, 10)  # 创建数组array([10, 20, 30, 40])
b = np.arange(4)  # 创建数组 array([0, 1, 2, 3])
a - b  # a,b 数组行列数相同，做减法运算
array([10, 19, 28, 37])
a + b
array([10, 21, 32, 43])
a * b
array([0, 20, 60, 120])
a ** b  # 以ｂ数组中元素作为ａ数组中相应元素的幂做运算
array([1, 20, 900, 64000])
a ** 2  # 简单的幂运算
array([100, 400, 900, 1600])
np.sin(a)
array([-0.54402111, 0.91294525, -0.98803162, 0.74511316])  # 三角函数运算
a < 20  # 对数组中的值进行逻辑判断，返回一个bool值数组
array([True, False, False, False], dtype=bool)

# 矩阵乘法dot
np.dot(a, b)  # 简单一维矩阵乘法
200
d = np.arange(1, 7).reshape(2, 3)
e = np.arange(2, 8).reshape(3, 2)
np.dot(d, e)  # 多维矩阵相乘
array([[28, 34],
       [64, 79]])

print d