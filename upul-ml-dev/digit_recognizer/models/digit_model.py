from digit_recognizer.models.base import Model
from digit_recognizer.datasets.mnist import MnistDataset
from digit_recognizer.networks import mlp
from digit_recognizer.networks import lenet5
import numpy as np


class DigitModel(Model):
    def __init__(self,
                 dataset_cls=MnistDataset,
                 network_fn=lenet5,
                 dataset_args={'image_size': (28, 28, 1)},
                 network_args={}):
        self.network_fn = network_fn
        super().__init__(dataset_cls, network_fn, dataset_args, network_args)

    def predict_on_image(self, image):
        if image.dtype == np.uint8:
            image = (image / 255).astype(np.float32)
        image = np.expand_dims(image, 0)
        
        if self.network_fn == lenet5:
            image = np.expand_dims(image, 3)
        
        prediction = self.network.predict(image, batch_size=1)
        return np.argmax(prediction), np.max(prediction)
