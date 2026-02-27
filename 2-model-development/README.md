# Model Development Phase

## Overview
This phase involves building and training a custom hand detection and gesture recognition model, similar to MediaPipe's hand tracking functionality.

## Model Architecture

Our model consists of two main components:

### 1. Hand Detection Model
- Detects the presence and location of hands in an image
- Outputs bounding box coordinates for each detected hand

### 2. Hand Landmark Model
- Takes the detected hand region as input
- Predicts 21 3D hand landmarks
- Outputs gesture classification

## Files

- **model_architecture.py**: Defines the neural network architecture
- **train.py**: Training script for the model
- **evaluate.py**: Evaluation and testing script
- **data_preprocessing.py**: Data preprocessing and augmentation utilities
- **utils.py**: Training utilities (loss functions, metrics, etc.)

## Training the Model

### 1. Prepare the Data
Ensure you have completed the data collection phase and have annotated data in `../data/annotations/`.

### 2. Preprocess the Data
```bash
python data_preprocessing.py
```

This will:
- Load annotated data
- Apply data augmentation
- Split into train/validation/test sets
- Save processed data to `../data/processed/`

### 3. Train the Model
```bash
python train.py --epochs 100 --batch-size 32 --learning-rate 0.001
```

Training arguments:
- `--epochs`: Number of training epochs (default: 100)
- `--batch-size`: Batch size for training (default: 32)
- `--learning-rate`: Learning rate (default: 0.001)
- `--checkpoint-dir`: Directory to save checkpoints (default: ../models/checkpoints)
- `--resume`: Resume from a checkpoint

### 4. Evaluate the Model
```bash
python evaluate.py --model-path ../models/saved_models/best_model.h5
```

This will:
- Load the trained model
- Run evaluation on test set
- Generate performance metrics (accuracy, precision, recall, F1)
- Create confusion matrix
- Save results to evaluation report

## Model Performance Targets

- **Hand Detection**: mAP > 0.95
- **Landmark Prediction**: Mean error < 5 pixels
- **Gesture Classification**: Accuracy > 95%
- **Inference Speed**: > 30 FPS on CPU

## Monitoring Training

Training metrics are logged and can be visualized using TensorBoard:
```bash
tensorboard --logdir ../models/checkpoints/logs
```

## Model Export

After training, export the model for deployment:
```bash
python export_model.py --model-path ../models/saved_models/best_model.h5 --output-format tflite
```

Supported formats:
- TensorFlow SavedModel
- TensorFlow Lite (.tflite)
- ONNX (.onnx)

## Next Steps

After training and evaluating your model, proceed to the **3-application** phase to integrate it into the Spotify controller application.
