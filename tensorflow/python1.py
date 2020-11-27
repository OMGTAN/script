import tensorflow as tf
import numpy as np

x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1+0.3


Weights = tf.Variable(tf.random_uniform_initializer(-1.0,1.0, None), shape=tf.TensorShape(None))
biases = tf.Variable(tf.zeros([1]), shape=tf.TensorShape(None))

