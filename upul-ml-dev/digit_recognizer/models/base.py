from pathlib import Path
import numpy as np

class Model:
    def __init__(self, dataset_cls, network_fn, dataset_args={}, network_args={}):
        self.name = f'{self.__class__.__name__}_{dataset_cls.__name__}_{network_fn.__name__}'
        self.dataset_cls = dataset_cls
        self.dataset_args = dataset_args

        self.data = dataset_cls(**dataset_args)
        input_shape = self.data.shape
        classes = self.data.classes
        
        self.network = network_fn(input_shape, classes, **network_args)

    def fit(self, epochs, steps_per_epoch, batch_size):
        self.network.compile(loss=self.loss,
                             optimizer=self.optimizer,
                             metrics=self.metrics)

        history = self.network.fit(self.data.build_pipeline(batch_size=batch_size),
                         steps_per_epoch=steps_per_epoch,
                         epochs=epochs)
                         
        training_acc = np.mean(history.history['acc']).item()
        training_loss = np.mean(history.history['loss']).item()
        return {'loss': training_loss, 'accuracy': training_acc}

    def test(self, batch_size):
        self.dataset_args['portion'] = 'test'
        test_dateset = self.dataset_cls(**self.dataset_args).build_pipeline(repeat=False)
        result = self.network.evaluate(test_dateset)
        return {
            'accuracy': result[1].item(),
            'loss': result[0].item()
        }

    def save_weights(self):
        path = (
            Path(__name__).parent.absolute() / 'digit_recognizer/weights').as_posix()
        self.network.save_weights(f'{path}/{self.name}_weights.h5')

    def load_weights(self):
        path = (
            Path(__name__).parent.absolute() / 'digit_recognizer/weights').as_posix()
        self.network.load_weights(f'{path}/{self.name}_weights.h5')

    @property
    def loss(self):
        return 'categorical_crossentropy'

    @property
    def optimizer(self):
        return 'adam'

    @property
    def metrics(self):
        return ['accuracy']
