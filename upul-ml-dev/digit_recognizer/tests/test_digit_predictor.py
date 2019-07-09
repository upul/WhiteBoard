import unittest
from pathlib import Path
from imageio import imread
from digit_recognizer.digit_predictor import DigitPredictor
from digit_recognizer.networks import mlp
from digit_recognizer.networks import lenet5
from digit_recognizer.datasets.mnist import MnistDataset


class TestDigitPredictor(unittest.TestCase):
    def test_prediction_mlp(self):
        dataset_cls = MnistDataset
        dataset_args = {'image_size': (28, 28)}
        predictor = DigitPredictor(network_fn=mlp,
                                   dataset_cls=dataset_cls,
                                   dataset_args=dataset_args)
        path = Path(__name__).parent.absolute() / 'digit_recognizer/example'
        for file in path.glob('*.*'):
            result = predictor.predict(imread(file))
            pred = result['prediction']
            conf = result['probability']
            print(f'image: {file.stem} prediction: {pred} probability: {conf}')
            self.assertEqual(pred, int(file.stem))
            self.assertGreater(conf, 0.5)

    def test_prediction_lenet5(self):
        dataset_cls = MnistDataset
        dataset_args = {'image_size': (28, 28, 1)}
        predictor = DigitPredictor(network_fn=lenet5,
                                   dataset_cls=dataset_cls,
                                   dataset_args=dataset_args)
        path = Path(__name__).parent.absolute() / 'digit_recognizer/example'
        for file in path.glob('*.*'):
            result = predictor.predict(imread(file))
            pred = result['prediction']
            conf = result['probability']
            print(f'image: {file.stem} prediction: {pred} probability: {conf}')
            self.assertEqual(pred, int(file.stem))
            self.assertGreater(conf, 0.5)


if __name__ == '__main__':
    unittest.main()