from digit_recognizer.models import DigitModel


class DigitPredictor:
    def __init__(self, network_fn, dataset_cls, dataset_args):
        self.model = DigitModel(network_fn=network_fn,
                                dataset_cls=dataset_cls,
                                dataset_args=dataset_args)
        self.model.load_weights()

    def predict(self, image):
        prediction = self.model.predict_on_image(image)
        return {
            'prediction': prediction[0].item(),
            'probability': round(prediction[1].item(), 4)
        }
