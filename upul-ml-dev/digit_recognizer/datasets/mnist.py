import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
from pathlib import Path


class MnistDataset:
    def __init__(self, portion='train', image_size=(28, 28), num_classes=10):
        self.portion = portion
        self.image_size = image_size
        self.num_classes = num_classes

    def build_pipeline(self, repeat=True, batch_size=64):
        dataset = tf.data.TFRecordDataset(self._data_file())
        dataset = dataset.map(self._decode_example)
        if repeat:
            dataset = dataset.repeat()
        dataset = dataset.shuffle(10000)
        dataset = dataset.batch(batch_size)
        return dataset

    @property
    def shape(self):
        return self.image_size

    @property
    def classes(self):
        return self.num_classes

    def _data_file(self):
        path = Path(
            __name__).parent.absolute() / 'digit_recognizer/datasets/raw_data'
        if self.portion == 'train':
            return (path / 'train.tfrecords').as_posix()

        elif self.portion == 'test':
            return (path / 'test.tfrecords').as_posix()

        raise RuntimeError('unrecognized data portion name: {}'.format(
            self.portion))

    def _decode_example(self, record):

        features = tf.io.parse_single_example(
            record,
            features={
                'image_raw': tf.io.FixedLenFeature([], tf.string),
                'label': tf.io.FixedLenFeature([], tf.int64)
            })

        image = tf.io.decode_raw(features['image_raw'], tf.uint8)
        image = tf.reshape(image, self.image_size)
        image = tf.cast(image, tf.float32) / 255.

        label = tf.one_hot(tf.cast(features['label'], tf.int32),
                           self.num_classes)

        return [image, label]