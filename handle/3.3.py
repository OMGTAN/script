from typing import NamedTuple
import tensorflow as tf

num_inputs = 2
num_examples = 1000
true_w = [2, -3.4]
true_b = 4.2
features = tf.random.normal(shape=(num_examples, num_inputs), stddev=1)
labels = true_w[0] * features[:, 0] + true_w[1] * features[:, 1] + true_b
labels += tf.random.normal(labels.shape, stddev=0.01)

from tensorflow import data as tfdata

batch_size = 10
dataset = tfdata.Dataset.from_tensor_slices((features, labels))
dataset = dataset.shuffle(buffer_size=num_examples)
dataset = dataset.batch(batch_size)
data_iter = iter(dataset)

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow import initializers as init
model = keras.Sequential()
model.add(layers.Dense(1, kernel_initializer=init.RandomNormal(stddev=0.01)))

from tensorflow import losses
loss = losses.MeanSquaredError()

from tensorflow.keras import optimizers
trainer = optimizers.SGD(learning_rate=0.03)

num_epochs = 3
for epoch in range(1, num_epochs + 1):
    for (batch, (X, y)) in enumerate(dataset):
        with tf.GradientTape() as tape:
            l = loss(model(X, training=True), y)

        grads = tape.gradient(l, model.trainable_variables)
        trainer.apply_gradients(zip(grads, model.trainable_variables))

    l = loss(model(features), labels)
    print('epoch %d, loss %f' % (epoch, l))
