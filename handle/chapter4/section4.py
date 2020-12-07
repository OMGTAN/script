import tensorflow as tf
import numpy as np

X = tf.random.uniform((2, 20))


class CenteredLayer(tf.keras.layers.Layer):
    def __init__(self):
        super().__init__()

    def call(self, inputs):
        return inputs - tf.reduce_mean(inputs)


class myDense(tf.keras.layers.Layer):
    def __init__(self, units):
        super().__init__()
        self.units = units

    def build(self, input_shape):
        self.w = self.add_weight(name='w',
                                 shape=[input_shape[-1], self.units],
                                 initializer=tf.random_normal_initializer())
        self.b = self.add_weight(name='b',
                                 shape=[self.units],
                                 initializer=tf.zeros_initializer())

    def call(self, inputs):
        y_pred = tf.matmul(inputs, self.w) + self.b
        return y_pred