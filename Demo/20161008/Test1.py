#coding:utf-8
import tensorflow as tf 
import numpy as np 

# TF中要定义的几个重要东西
x_data = np.random.rand(100).astype(np.float32)
#print x_data
y_data = x_data*0.1 + 0.3
#print y_data

#定义权值
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))

#定义冲量
biases = tf.Variable(tf.zeros([1]))

#输入层x * 权值 + 冲量 !!!!!!!!!!!!!!!!!!!!!!!!!
y = Weights * x_data + biases

#导入到激励函数中  !!!!!!!!!!!!!!!!!!!!!!!!!
loss = tf.reduce_mean(tf.square(y-y_data))

#优化器 !!!!!!!!!!!!!!!!!!!!!!!!
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

for step in range(200):
	sess.run(train)
	if step % 20 == 0:
		print(step, sess.run(Weights), sess.run(biases))