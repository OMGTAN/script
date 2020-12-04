import tensorflow as tf
import numpy as np

from tensorflow.keras.datasets import fashion_mnist

batch_size = 256
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
x_train = tf.cast(x_train, tf.float32) / 255  #在进行矩阵相乘时需要float型，故强制类型转换为float型
x_test = tf.cast(x_test, tf.float32) / 255  #在进行矩阵相乘时需要float型，故强制类型转换为float型
train_iter = tf.data.Dataset.from_tensor_slices(
    (x_train, y_train)).batch(batch_size)
test_iter = tf.data.Dataset.from_tensor_slices(
    (x_test, y_test)).batch(batch_size)

num_inputs = 784
num_outputs = 10

W = tf.Variable(
    tf.random.normal(shape=(num_inputs, num_outputs),
                     mean=0,
                     stddev=0.01,
                     dtype=tf.float32))
b = tf.Variable(tf.zeros(num_outputs, dtype=tf.float32))


def softMax(logits, axis=-1):
    return tf.exp(logits) / tf.reduce_sum(tf.exp(logits), axis, keepdims=True)


def net(X):
    logits = tf.matmul(tf.reshape(X, shape=(-1, W.shape[0])), W) + b
    return softMax(logits)


y_hat = np.array([[0.1, 0.3, 0.6], [0.3, 0.2, 0.5]])
y = np.array([0, 2], dtype='int32')
ttt = tf.one_hot(y, depth=3)
tf.boolean_mask(y_hat, tf.one_hot(y, depth=3))


def cross_entropy(y_hat, y):
    y = tf.cast(tf.reshape(y, shape=[-1, 1]), dtype=tf.int32)
    y = tf.one_hot(y, depth=y_hat.shape[-1])
    y = tf.cast(tf.reshape(y, shape=[-1, y_hat.shape[-1]]), dtype=tf.int32)
    return -tf.math.log(tf.boolean_mask(y_hat, y) + 1e-8)


def accuracy(y_hat, y):
    return np.mean((tf.argmax(y_hat, axis=1) == y))


accuracy(y_hat, y)


# 描述,对于tensorflow2中，比较的双方必须类型都是int型，所以要将输出和标签都转为int型
def evaluate_accuracy(data_iter, net):
    acc_sum, n = 0.0, 0
    for _, (X, y) in enumerate(data_iter):
        y = tf.cast(y, dtype=tf.int64)
        acc_sum += np.sum(
            tf.cast(tf.argmax(net(X), axis=1), dtype=tf.int64) == y)
        n += y.shape[0]
    return acc_sum / n


print(evaluate_accuracy(test_iter, net))
num_epochs, lr = 5, 0.1


# 本函数已保存在d2lzh包中方便以后使用
def train_ch3(net,
              train_iter,
              test_iter,
              loss,
              num_epochs,
              batch_size,
              params=None,
              lr=None,
              trainer=None):
    for epoch in range(num_epochs):
        train_l_sum, train_acc_sum, n = 0.0, 0.0, 0
        for X, y in train_iter:
            with tf.GradientTape() as tape:
                y_hat = net(X)
                l = tf.reduce_sum(loss(y_hat, y))
            grads = tape.gradient(l, params)
            if trainer is None:
                # 如果没有传入优化器，则使用原先编写的小批量随机梯度下降
                for i, param in enumerate(params):
                    param.assign_sub(lr * grads[i] / batch_size)
            else:
                # tf.keras.optimizers.SGD 直接使用是随机梯度下降 theta(t+1) = theta(t) - learning_rate * gradient
                # 这里使用批量梯度下降，需要对梯度除以 batch_size, 对应原书代码的 trainer.step(batch_size)
                trainer.apply_gradients(
                    zip([grad / batch_size for grad in grads], params))

            y = tf.cast(y, dtype=tf.float32)
            train_l_sum += l.numpy()
            train_acc_sum += tf.reduce_sum(
                tf.cast(tf.argmax(y_hat, axis=1) == tf.cast(y, dtype=tf.int64),
                        dtype=tf.int64)).numpy()
            n += y.shape[0]
        test_acc = evaluate_accuracy(test_iter, net)
        print('epoch %d, loss %.4f, train acc %.3f, test acc %.3f' %
              (epoch + 1, train_l_sum / n, train_acc_sum / n, test_acc))


trainer = tf.keras.optimizers.SGD(lr)
train_ch3(net, train_iter, test_iter, cross_entropy, num_epochs, batch_size,
          [W, b], lr)
