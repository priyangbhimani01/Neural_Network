# -*- coding: utf-8 -*-
"""Exercise_4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PhPgXvDc6d1KhAu9yk4sKHpf9SwS8ltJ
"""

import tensorflow as tf
import numpy as np

layer_1 = tf.keras.layers.Dense(units=100, activation='relu')
layer_2 = tf.keras.layers.Dense(units=25, activation='relu')
layer_3 = tf.keras.layers.Dense(units=4, activation='softmax')

model = tf.keras.models.Sequential([layer_1, layer_2, layer_3])

x = np.array([[200, 17], [120, 5], [425, 20], [212, 18], [220, 19]])
y = np.array([2, 3, 0, 1, 2])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
model.fit(x, y, epochs=100)

x_new = np.array([[200, 17], [50, 1]])
out = model.predict(x_new)
print(out)