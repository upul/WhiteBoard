import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf


def mlp(input_shape, num_classes, activation='relu', dropout_amount=0.1):

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten(input_shape=input_shape))
    for layer_size in [128, 64]:
        model.add(tf.keras.layers.Dense(layer_size, activation=activation))
        model.add(tf.keras.layers.Dropout(dropout_amount))
    model.add(tf.keras.layers.Dense(num_classes, activation='softmax'))
    return model
