import tensorflow as tf
import numpy as np
from pathlib import Path

PATH = path = Path(
    __name__).parent.absolute() / 'digit_recognizer/datasets/raw_data'
TRAIN_FILE = (PATH / 'train.tfrecords').as_posix()
TEST_FILE = (PATH / 'test.tfrecords').as_posix()
NPZ_FILE = (PATH / 'mnist.npz').as_posix()


def convert_to_tfrecords(npz_file, tf_train_file, tf_test_file):
    def _int64_feature(value):
        return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

    def _bytes_feature(value):
        return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

    def _write_tfrecords(dataset, tf_file):
        with tf.python_io.TFRecordWriter(tf_file) as writer:
            for image, label in dataset:
                image_raw = image.tostring()
                rows, cols = image.shape
                example = tf.train.Example(features=tf.train.Features(
                    feature={
                        'height': _int64_feature(rows),
                        'width': _int64_feature(cols),
                        'depth': _int64_feature(1),
                        'label': _int64_feature(int(label)),
                        'image_raw': _bytes_feature(image_raw)
                    }))
                writer.write(example.SerializeToString())

    data = np.load(npz_file, mmap_mode='r')
    train_set = list(zip(data['x_train'], data['y_train']))
    test_set = list(zip(data['x_test'], data['y_test']))

    print('converting training file')
    _write_tfrecords(train_set, tf_train_file)

    print('converting testing file')
    _write_tfrecords(test_set, tf_test_file)

    print('convertion completed')


if __name__ == "__main__":
    convert_to_tfrecords(NPZ_FILE, TRAIN_FILE,
                         TEST_FILE)
