import argparse
import json
import importlib
import digit_recognizer.datasets


def training(configs):
    datasets_module = importlib.import_module('digit_recognizer.datasets')
    if 'dataset' not in configs:
        return f'required parameter: dataset is missing'
    dataset_cls = getattr(datasets_module, configs['dataset'])

    dataset_args = configs.get('dataset_args', {})

    model_module = importlib.import_module('digit_recognizer.models')
    if 'model' not in configs:
        return f'required parameter: model is missing'
    model_cls = getattr(model_module, configs['model'])

    network_module = importlib.import_module('digit_recognizer.networks')

    network_fn = getattr(network_module, configs['network'])
    if 'network' not in configs:
        return f'required parameter: network is missing'

    network_args = configs.get('network_args', {})
    model = model_cls(dataset_cls=dataset_cls,
                      network_fn=network_fn,
                      dataset_args=dataset_args,
                      network_args=network_args)

    epochs, batch_size, steps_per_epoch = _read_training_parameters(configs)
    print('\ntraining starts')
    training_result = model.fit(epochs=epochs,
              batch_size=batch_size,
              steps_per_epoch=steps_per_epoch)
    
    print('\ntesting starts')
    test_result = model.test(batch_size=batch_size)
    print()

    if configs.get("save_weights"):
        model.save_weights()

    return {'status': 'success', 'train': training_result, 'test': test_result}


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--configs', type=str)
    return parser.parse_args()


def _read_training_parameters(configs):
    epochs = configs['train_args']['epochs'] if 'epochs' in configs[
        'train_args'] else 5
    batch_size = configs['train_args'][
        'batch_size'] if 'batch_size' in configs['train_args'] else 32
    steps_per_epoch = configs['train_args'][
        'steps_per_epoch'] if 'steps_per_epoch' in configs[
            'train_args'] else int(60000 / batch_size)
    return epochs, batch_size, steps_per_epoch


def main():
    args = _parse_args()
    configs = json.loads(args.configs)
    training(configs)


if __name__ == "__main__":
    main()