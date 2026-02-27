"""
Hand Detection and Gesture Recognition Model Architecture
Inspired by MediaPipe's hand tracking approach.
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


class HandDetectionModel(keras.Model):
    """
    Hand detection model to locate hands in images.
    Similar to MediaPipe's palm detection model.
    """
    
    def __init__(self, input_shape=(256, 256, 3), num_anchors=2016):
        super(HandDetectionModel, self).__init__()
        
        self.input_shape = input_shape
        self.num_anchors = num_anchors
        
        # Backbone: MobileNetV2 for feature extraction
        self.backbone = keras.applications.MobileNetV2(
            input_shape=input_shape,
            include_top=False,
            weights='imagenet'
        )
        
        # Detection head
        self.conv1 = layers.Conv2D(256, 3, padding='same', activation='relu')
        self.conv2 = layers.Conv2D(256, 3, padding='same', activation='relu')
        
        # Output: [batch, num_anchors, 4 + 1] (bbox + confidence)
        self.bbox_head = layers.Conv2D(num_anchors * 5, 1, padding='same')
        
    def call(self, inputs, training=False):
        x = self.backbone(inputs, training=training)
        x = self.conv1(x)
        x = self.conv2(x)
        bbox_output = self.bbox_head(x)
        
        # Reshape to [batch, num_anchors, 5]
        batch_size = tf.shape(inputs)[0]
        bbox_output = tf.reshape(bbox_output, [batch_size, -1, 5])
        
        return bbox_output


class HandLandmarkModel(keras.Model):
    """
    Hand landmark model to predict 21 3D hand landmarks.
    Similar to MediaPipe's hand landmark model.
    """
    
    def __init__(self, input_shape=(256, 256, 3), num_landmarks=21):
        super(HandLandmarkModel, self).__init__()
        
        self.input_shape = input_shape
        self.num_landmarks = num_landmarks
        
        # Backbone: MobileNetV2
        self.backbone = keras.applications.MobileNetV2(
            input_shape=input_shape,
            include_top=False,
            weights='imagenet'
        )
        
        # Landmark prediction head
        self.global_pool = layers.GlobalAveragePooling2D()
        self.fc1 = layers.Dense(512, activation='relu')
        self.dropout1 = layers.Dropout(0.3)
        self.fc2 = layers.Dense(256, activation='relu')
        self.dropout2 = layers.Dropout(0.3)
        
        # Output: [batch, num_landmarks * 3] (x, y, z for each landmark)
        self.landmark_head = layers.Dense(num_landmarks * 3)
        
    def call(self, inputs, training=False):
        x = self.backbone(inputs, training=training)
        x = self.global_pool(x)
        x = self.fc1(x)
        x = self.dropout1(x, training=training)
        x = self.fc2(x)
        x = self.dropout2(x, training=training)
        landmarks = self.landmark_head(x)
        
        # Reshape to [batch, num_landmarks, 3]
        landmarks = tf.reshape(landmarks, [-1, self.num_landmarks, 3])
        
        return landmarks


class GestureRecognitionModel(keras.Model):
    """
    Gesture recognition model that classifies hand gestures.
    Takes hand landmarks as input.
    """
    
    def __init__(self, num_landmarks=21, num_classes=7):
        super(GestureRecognitionModel, self).__init__()
        
        self.num_landmarks = num_landmarks
        self.num_classes = num_classes
        
        # Input: [batch, num_landmarks * 3]
        self.fc1 = layers.Dense(128, activation='relu')
        self.dropout1 = layers.Dropout(0.3)
        self.fc2 = layers.Dense(64, activation='relu')
        self.dropout2 = layers.Dropout(0.3)
        self.fc3 = layers.Dense(32, activation='relu')
        
        # Output: [batch, num_classes]
        self.classifier = layers.Dense(num_classes, activation='softmax')
        
    def call(self, inputs, training=False):
        # Flatten landmarks if needed
        if len(inputs.shape) == 3:
            x = tf.reshape(inputs, [-1, self.num_landmarks * 3])
        else:
            x = inputs
            
        x = self.fc1(x)
        x = self.dropout1(x, training=training)
        x = self.fc2(x)
        x = self.dropout2(x, training=training)
        x = self.fc3(x)
        output = self.classifier(x)
        
        return output


class HandGestureModel(keras.Model):
    """
    End-to-end hand gesture recognition model.
    Combines hand detection, landmark prediction, and gesture classification.
    """
    
    def __init__(self, num_classes=7):
        super(HandGestureModel, self).__init__()
        
        self.hand_detector = HandDetectionModel()
        self.landmark_predictor = HandLandmarkModel()
        self.gesture_classifier = GestureRecognitionModel(num_classes=num_classes)
        
    def call(self, inputs, training=False):
        # Note: In practice, hand detection output would be used to crop
        # the image before feeding to landmark predictor
        # This is a simplified version
        
        landmarks = self.landmark_predictor(inputs, training=training)
        gesture = self.gesture_classifier(landmarks, training=training)
        
        return {
            'landmarks': landmarks,
            'gesture': gesture
        }


def create_model(model_type='full', num_classes=7):
    """
    Factory function to create different model variants.
    
    Args:
        model_type: 'detection', 'landmark', 'gesture', or 'full'
        num_classes: Number of gesture classes
        
    Returns:
        Keras model instance
    """
    if model_type == 'detection':
        return HandDetectionModel()
    elif model_type == 'landmark':
        return HandLandmarkModel()
    elif model_type == 'gesture':
        return GestureRecognitionModel(num_classes=num_classes)
    elif model_type == 'full':
        return HandGestureModel(num_classes=num_classes)
    else:
        raise ValueError(f"Unknown model type: {model_type}")


if __name__ == "__main__":
    # Test model creation
    print("Creating models...")
    
    detection_model = create_model('detection')
    print(f"✓ Hand Detection Model: {detection_model.count_params():,} parameters")
    
    landmark_model = create_model('landmark')
    print(f"✓ Hand Landmark Model: {landmark_model.count_params():,} parameters")
    
    gesture_model = create_model('gesture')
    print(f"✓ Gesture Recognition Model: {gesture_model.count_params():,} parameters")
    
    full_model = create_model('full')
    print(f"✓ Full Hand Gesture Model: {full_model.count_params():,} parameters")
