# -*-coding:gbk-*-
# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

"""
Please note, this code is only for python 3+. If you are using python 2+, please modify the code accordingly.
"""
from __future__ import print_function
import tensorflow as tf
import numpy as np

def add_layer(inputs, in_size, out_size, activation_function=None):
    # add one more layer and return the output of this layer
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


# Make up some real data

# 间隔采样 numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)[source] 维度
# 1 个神经元
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]  # 矩阵变成1 列的
print (x_data)
print ("####################")

# 此概率分布的均值（对应着整个分布的中心centre）
# 此概率分布的标准差（对应于分布的宽度，scale越大越矮胖，scale越小，越瘦高）
# 输出的shape(格式)，默认为None，只输出一个值
noise=np.random.normal(0, 0.05, x_data.shape)
print (noise)
print ("####################")
y_data=np.square(x_data) - 0.5 + noise

# define placeholder for inputs to network
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])
# add hidden layer
# 隐藏层
# add_layer(输入, 输入神经元, 输出神经元, 激励函数)
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
# add output layer
# 输出层
prediction = add_layer(l1, 10, 1, activation_function=None)

# the error between prediction and real data
# 误差 reduce_mean 平均值   reduce_sum求和 tf.square 平方
# reduction_indices的默认值时None，即把input_tensor降到 0维，也就是一个数。
# 对于2维input_tensor，reduction_indices=0时，按列；reduction_indices=1时，按行。
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),
                                    reduction_indices=[1]))

# 练习  0.1=学习效率 minimize=减下误差
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

# important step
# tf.initialize_all_variables() no long valid from
# 2017-03-02 if using tensorflow >= 0.12
if int((tf.__version__).split('.')[1]) < 12:
    init = tf.initialize_all_variables()
else:
    init = tf.global_variables_initializer()
sess = tf.Session() # 初始化服务
sess.run(init)  # 初始化变量

for i in range(10000):
    # training
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:
        # to see the step improvement
        print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
