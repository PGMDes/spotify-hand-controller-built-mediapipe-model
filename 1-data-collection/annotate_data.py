"""
Data Annotation Script
Extracts hand landmarks from collected images using MediaPipe and saves annotations.
"""

import cv2
import mediapipe as mp
import json
import os
from pathlib import Path
from tqdm import tqdm

# Configuration
RAW_DATA_DIR = "../data/raw"
ANNOTATIONS_DIR = "../data/annotations"

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils


def create_annotations_directory():
    """Create annotations directory if it doesn't exist."""
    if not os.path.exists(ANNOTATIONS_DIR):
        os.makedirs(ANNOTATIONS_DIR)
        print(f"Created directory: {ANNOTATIONS_DIR}")


def extract_landmarks(image_path):
    """
    Extract hand landmarks from an image using MediaPipe.
    
    Args:
        image_path: Path to the image file
        
    Returns:
        Dictionary with landmark coordinates or None if no hand detected
    """
    image = cv2.imread(str(image_path))
    if image is None:
        return None
    
    # Convert to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Process with MediaPipe
    with mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=1,
        min_detection_confidence=0.5
    ) as hands:
        results = hands.process(image_rgb)
        
        if not results.multi_hand_landmarks:
            return None
        
        # Extract landmark coordinates
        landmarks = []
        for hand_landmarks in results.multi_hand_landmarks:
            for landmark in hand_landmarks.landmark:
                landmarks.append({
                    'x': landmark.x,
                    'y': landmark.y,
                    'z': landmark.z
                })
        
        return {
            'landmarks': landmarks,
            'image_shape': {
                'height': image.shape[0],
                'width': image.shape[1],
                'channels': image.shape[2]
            }
        }


def annotate_gesture_class(gesture_class):
    """
    Annotate all images in a gesture class folder.
    
    Args:
        gesture_class: Name of the gesture class
        
    Returns:
        Number of successfully annotated images
    """
    gesture_dir = Path(RAW_DATA_DIR) / gesture_class
    if not gesture_dir.exists():
        print(f"Warning: Directory not found: {gesture_dir}")
        return 0
    
    # Get all image files
    image_files = list(gesture_dir.glob("*.jpg")) + list(gesture_dir.glob("*.png"))
    
    if not image_files:
        print(f"No images found in {gesture_dir}")
        return 0
    
    print(f"\nAnnotating {gesture_class}: {len(image_files)} images")
    
    annotations = []
    successful = 0
    
    for image_path in tqdm(image_files):
        landmarks = extract_landmarks(image_path)
        if landmarks:
            annotations.append({
                'image_path': str(image_path.relative_to(Path(RAW_DATA_DIR).parent)),
                'gesture_class': gesture_class,
                'landmarks': landmarks
            })
            successful += 1
    
    # Save annotations to JSON file
    annotation_file = Path(ANNOTATIONS_DIR) / f"{gesture_class}_annotations.json"
    with open(annotation_file, 'w') as f:
        json.dump(annotations, f, indent=2)
    
    print(f"✓ Saved {successful} annotations to {annotation_file}")
    return successful


def main():
    """Main annotation workflow."""
    create_annotations_directory()
    
    print("="*60)
    print("HAND GESTURE DATA ANNOTATION")
    print("="*60)
    
    # Get all gesture class directories
    raw_data_path = Path(RAW_DATA_DIR)
    if not raw_data_path.exists():
        print(f"Error: Raw data directory not found: {RAW_DATA_DIR}")
        return
    
    gesture_classes = [d.name for d in raw_data_path.iterdir() if d.is_dir()]
    
    if not gesture_classes:
        print(f"No gesture class directories found in {RAW_DATA_DIR}")
        return
    
    print(f"\nFound {len(gesture_classes)} gesture classes:")
    for gesture in gesture_classes:
        print(f"  - {gesture}")
    
    print("\nStarting annotation process...")
    
    total_annotated = 0
    for gesture_class in gesture_classes:
        count = annotate_gesture_class(gesture_class)
        total_annotated += count
    
    print("\n" + "="*60)
    print(f"ANNOTATION COMPLETE!")
    print(f"Total images annotated: {total_annotated}")
    print(f"Annotations saved to: {ANNOTATIONS_DIR}")
    print("="*60)


if __name__ == "__main__":
    main()
