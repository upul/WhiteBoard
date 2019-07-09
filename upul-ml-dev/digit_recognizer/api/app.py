from flask import Flask, jsonify, request
from imageio import imread
from digit_recognizer.digit_predictor import DigitPredictor
from training import run_training
from digit_recognizer.networks import lenet5
from digit_recognizer.datasets.mnist import MnistDataset

app = Flask(__name__)


@app.route('/api/v1/predict', methods=['POST'])
def do_prediction():
    if 'image' not in request.files:
        return jsonify({
            'message':
            'invalid syntax, example: curl -X POST -F image=@8.png http://localhost:8080/api/v1/predict'
        }), 422

    try:
        image = imread(request.files["image"])
        predictor = DigitPredictor(network_fn=lenet5,
                                   dataset_cls=MnistDataset,
                                   dataset_args={'image_size': (28, 28, 1)})
        return jsonify(predictor.predict(image)), 200
    except Exception as ex:
        message = 'internal error has occurred. message: {}'.format(str(ex))
        return jsonify({'message': message}), 500


@app.route('/api/v1/train', methods=['POST'])
def do_training():
    training_args = request.json
    try:
        status = run_training.training(training_args)
        return jsonify({'message': status}), 200

    except Exception as ex:
        message = 'internal error has occurred. message: {}'.format(str(ex))
        return jsonify({'message': message}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)