import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf

def lenet5(input_shape, num_classes, activation='relu', dropout_amount=0.1):
    model = tf.keras.models.Sequential()

    model.add(
        tf.keras.layers.Conv2D(32,
                               kernel_size=(3, 3),
                               activation=activation,
                               input_shape=input_shape))
    model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))

    model.add(
        tf.keras.layers.Conv2D(64,
                               kernel_size=(3, 3),
                               activation=activation,
                               input_shape=input_shape))
    model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))
    model.add(tf.keras.layers.Dropout(dropout_amount))

    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(128, activation=activation))
    model.add(tf.keras.layers.Dropout(dropout_amount))
    model.add(tf.keras.layers.Dense(num_classes, activation='softmax'))

    return model

if __name__ == "__main__":
    from digit_recognizer.datasets import MnistDataset
    ds = MnistDataset(image_size=(28, 28, 1)).build_pipeline()
    network = lenet5((28, 28, 1), 10)
    network.compile(loss='categorical_crossentropy',
                             optimizer='adam',
                             metrics=['accuracy'])
    network.fit(ds, steps_per_epoch=128, epochs=10)

