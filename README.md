# mnist-cnn-classifier

This project implements a Convolutional Neural Network (CNN) to classify handwritten digits from the MNIST dataset. The model is designed to achieve over 95% test accuracy and includes visualization of predictions on sample images.

## Project Structure

```
mnist-cnn-classifier
├── src
│   ├── __init__.py
│   ├── data_loading.py
│   ├── model.py
│   ├── train.py
│   ├── evaluate.py
│   └── utils
│       ├── __init__.py
│       └── visualization.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd mnist-cnn-classifier
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Load the MNIST dataset and preprocess the data using the `data_loading.py` script.
2. Define the CNN architecture in `model.py`.
3. Train the model using the `train.py` script.
4. Evaluate the model's performance on the test dataset with `evaluate.py`.
5. Visualize the model's predictions using the functions in `utils/visualization.py`.

## Model Architecture

The CNN model consists of multiple convolutional layers followed by pooling layers, and it is compiled with appropriate loss and optimizer settings.

## Performance

The model is expected to achieve over 95% accuracy on the test dataset. Visualization of predictions on sample images is included to demonstrate the model's performance.

## License

This project is licensed under the MIT License.