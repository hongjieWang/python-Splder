# -*- coding:utf-8 -*-
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import numpy as np


def testInstallTensirflow():
    hello = tf.constant("hello tensorflow")
    sess = tf.Session()
    print(sess.run(hello))


"""
题目：
有函数

y = 0.5*x + 2
在此函数基础上，增加绝对值不超过0.05的扰动，利用keras进行函数拟合
预期结果：y=a1*x+a2

a1接近0.5， a2接近2，则拟合成功

"""

# 生成-1到1的200均匀分佈的數字
x = np.linspace(-1, 1, 200)
np.random.shuffle(x)

# 利用x生成y，并随机加入0.05之内的扰动
y = 0.5 * x + 2 + np.random.normal(0, 0.05, (200,))

plt.scatter(x, y)
plt.show()

# 截取160个数据作为训练数据
# 截取40个数据作为测试数据
x_train = x[:160]
x_test = x[160:]
y_train = y[:160]
y_test = y[160:]

# 新建一个流式网络
model = Sequential()

# 增加一个全连接层，输入一个参数，输出一个参数
model.add(Dense(output_dim=1, input_dim=1))

# 编译网络，损失函数mse，优化函数 sgd
model.compile(loss='mse', optimizer='sgd')

# 训练301次
for step in range(500):
    cost = model.train_on_batch(x_train, y_train)

    # 每100次打印一次损失
    if step % 100 == 0:
        print("cost:", cost)

# 使用测试数据，测试损失
cost = model.evaluate(x_test, y_test, batch_size=40)
print("test cost:", cost)

# 获取第一层网络的权重
W, b = model.layers[0].get_weights()
print("w:", W, " b:", b)

# 画图展示训练结果
y_pred = model.predict(x_test)
plt.scatter(x_test, y_test)
plt.plot(x_test, y_pred)

plt.show()


