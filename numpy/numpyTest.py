# -*- coding:gb2312 -*-
import numpy as np
a = np.arange(10, 41, 10)  # ��������array([10, 20, 30, 40])
b = np.arange(4)  # �������� array([0, 1, 2, 3])
a - b  # a,b ������������ͬ������������
array([10, 19, 28, 37])
a + b
array([10, 21, 32, 43])
a * b
array([0, 20, 60, 120])
a ** b  # �ԣ�������Ԫ����Ϊ����������ӦԪ�ص���������
array([1, 20, 900, 64000])
a ** 2  # �򵥵�������
array([100, 400, 900, 1600])
np.sin(a)
array([-0.54402111, 0.91294525, -0.98803162, 0.74511316])  # ���Ǻ�������
a < 20  # �������е�ֵ�����߼��жϣ�����һ��boolֵ����
array([True, False, False, False], dtype=bool)

# ����˷�dot
np.dot(a, b)  # ��һά����˷�
200
d = np.arange(1, 7).reshape(2, 3)
e = np.arange(2, 8).reshape(3, 2)
np.dot(d, e)  # ��ά�������
array([[28, 34],
       [64, 79]])

print d