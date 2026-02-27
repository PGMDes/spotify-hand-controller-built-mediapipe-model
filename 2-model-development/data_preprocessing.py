"""
Data Preprocessing and Augmentation
Prepares annotated data for model training.
"""

import json
import cv2
import numpy as np
from pathlib import Path
from sklearn.model_selection import train_test_split
import albumentations as A


# Configuration
ANNOTATIONS_DIR = "../data/annotations"
PROCESSED_DIR = "../data/processed"
IMAGE_SIZE = (256, 256)
TRAIN_SPLIT = 0.7
VAL_SPLIT = 0.15
TEST_SPLIT = 0.15


def load_annotations(annotation_file):
    """Load annotations from JSON file."""
    with open(annotation_file, 'r') as f:
        return json.load(f)


def get_augmentation_pipeline():
    """
    Create data augmentation pipeline.
    
    Returns:
        Albumentations transform pipeline
    """
    return A.Compose([
        A.HorizontalFlip(p=0.5),
        A.Rotate(limit=15, p=0.5),
        A.RandomBrightnessContrast(p=0.5),
        A.GaussNoise(p=0.3),
        A.Blur(blur_limit=3, p=0.3),
        A.CLAHE(p=0.3),
    ], keypoint_params=A.KeypointParams(format='xy', remove_invisible=False))


def normalize_landmarks(landmarks, image_shape):
    """
    Normalize landmark coordinates to [0, 1] range.
    
    Args:
        landmarks: List of landmark dictionaries with x, y, z coordinates
        image_shape: Tuple of (height, width)
        
    Returns:
        Normalized landmarks array of shape (21, 3)
    """
    normalized = []
    for lm in landmarks:
        # x and y are already normalized in MediaPipe output
        normalized.append([lm['x'], lm['y'], lm['z']])
    return np.array(normalized, dtype=np.float32)


def preprocess_image(image_path, target_size=IMAGE_SIZE):
    """
    Load and preprocess an image.
    
    Args:
        image_path: Path to image file
        target_size: Target image size (height, width)
        
    Returns:
        Preprocessed image array
    """
    image = cv2.imread(str(image_path))
    if image is None:
        raise ValueError(f"Failed to load image: {image_path}")
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, target_size)
    image = image.astype(np.float32) / 255.0  # Normalize to [0, 1]
    
    return image


def process_dataset(gesture_classes, augment=True):
    """
    Process all annotations and create train/val/test splits.
    
    Args:
        gesture_classes: List of gesture class names
        augment: Whether to apply data augmentation
        
    Returns:
        Dictionary with train/val/test splits
    """
    all_samples = []
    
    # Load all annotations
    for gesture_class in gesture_classes:
        annotation_file = Path(ANNOTATIONS_DIR) / f"{gesture_class}_annotations.json"
        if not annotation_file.exists():
            print(f"Warning: Annotation file not found: {annotation_file}")
            continue
        
        annotations = load_annotations(annotation_file)
        for ann in annotations:
            all_samples.append({
                'image_path': ann['image_path'],
                'gesture_class': ann['gesture_class'],
                'landmarks': ann['landmarks']
            })
    
    print(f"Loaded {len(all_samples)} samples")
    
    # Split dataset
    train_samples, temp_samples = train_test_split(
        all_samples, train_size=TRAIN_SPLIT, random_state=42, 
        stratify=[s['gesture_class'] for s in all_samples]
    )
    
    val_ratio = VAL_SPLIT / (VAL_SPLIT + TEST_SPLIT)
    val_samples, test_samples = train_test_split(
        temp_samples, train_size=val_ratio, random_state=42,
        stratify=[s['gesture_class'] for s in temp_samples]
    )
    
    print(f"Train: {len(train_samples)}, Val: {len(val_samples)}, Test: {len(test_samples)}")
    
    # Process and save splits
    dataset = {
        'train': process_split(train_samples, 'train', augment=augment),
        'val': process_split(val_samples, 'val', augment=False),
        'test': process_split(test_samples, 'test', augment=False)
    }
    
    return dataset


def process_split(samples, split_name, augment=False):
    """
    Process a data split.
    
    Args:
        samples: List of sample dictionaries
        split_name: Name of the split ('train', 'val', or 'test')
        augment: Whether to apply data augmentation
        
    Returns:
        Processed dataset dictionary
    """
    print(f"\nProcessing {split_name} split...")
    
    images = []
    landmarks = []
    labels = []
    
    augmentation = get_augmentation_pipeline() if augment else None
    
    for sample in samples:
        try:
            # Load image
            image_path = Path("..") / sample['image_path']
            image = preprocess_image(image_path)
            
            # Get landmarks
            lm_data = normalize_landmarks(
                sample['landmarks']['landmarks'],
                sample['landmarks']['image_shape']
            )
            
            # Apply augmentation if enabled
            if augmentation:
                # Convert landmarks to keypoints format for augmentation
                keypoints = [(lm[0] * IMAGE_SIZE[1], lm[1] * IMAGE_SIZE[0]) 
                           for lm in lm_data]
                
                transformed = augmentation(image=image, keypoints=keypoints)
                image = transformed['image']
                
                # Convert keypoints back to normalized landmarks
                new_keypoints = transformed['keypoints']
                for i, (x, y) in enumerate(new_keypoints):
                    lm_data[i][0] = x / IMAGE_SIZE[1]
                    lm_data[i][1] = y / IMAGE_SIZE[0]
            
            images.append(image)
            landmarks.append(lm_data)
            labels.append(sample['gesture_class'])
            
        except Exception as e:
            print(f"Error processing {sample['image_path']}: {e}")
            continue
    
    return {
        'images': np.array(images),
        'landmarks': np.array(landmarks),
        'labels': labels
    }


def save_processed_dataset(dataset):
    """Save processed dataset to disk."""
    processed_path = Path(PROCESSED_DIR)
    processed_path.mkdir(parents=True, exist_ok=True)
    
    for split_name, split_data in dataset.items():
        split_path = processed_path / split_name
        split_path.mkdir(exist_ok=True)
        
        np.save(split_path / 'images.npy', split_data['images'])
        np.save(split_path / 'landmarks.npy', split_data['landmarks'])
        
        with open(split_path / 'labels.json', 'w') as f:
            json.dump(split_data['labels'], f)
        
        print(f"✓ Saved {split_name} split: {len(split_data['images'])} samples")


def main():
    """Main preprocessing workflow."""
    print("="*60)
    print("DATA PREPROCESSING")
    print("="*60)
    
    # Get gesture classes from annotation directory
    annotations_path = Path(ANNOTATIONS_DIR)
    if not annotations_path.exists():
        print(f"Error: Annotations directory not found: {ANNOTATIONS_DIR}")
        return
    
    annotation_files = list(annotations_path.glob("*_annotations.json"))
    gesture_classes = [f.stem.replace('_annotations', '') for f in annotation_files]
    
    if not gesture_classes:
        print(f"No annotation files found in {ANNOTATIONS_DIR}")
        return
    
    print(f"\nFound {len(gesture_classes)} gesture classes:")
    for gesture in gesture_classes:
        print(f"  - {gesture}")
    
    # Process dataset
    dataset = process_dataset(gesture_classes, augment=True)
    
    # Save processed data
    save_processed_dataset(dataset)
    
    print("\n" + "="*60)
    print("PREPROCESSING COMPLETE!")
    print(f"Processed data saved to: {PROCESSED_DIR}")
    print("="*60)


if __name__ == "__main__":
    main()
