"""
Data Collection Script
Captures hand gesture images from webcam for training the hand detection model.
"""

import cv2
import os
import time
from datetime import datetime

# Configuration
OUTPUT_DIR = "../data/raw"
CAPTURE_FPS = 5  # Frames per second to capture
GESTURE_CLASSES = [
    "open_palm",
    "fist",
    "thumbs_up",
    "peace_sign",
    "pointing",
    "swipe_left",
    "swipe_right",
]


def create_output_directory():
    """Create output directory if it doesn't exist."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created directory: {OUTPUT_DIR}")


def collect_gesture_data(gesture_name, num_samples=100):
    """
    Collect images for a specific gesture.
    
    Args:
        gesture_name: Name of the gesture to collect
        num_samples: Number of samples to collect
    """
    gesture_dir = os.path.join(OUTPUT_DIR, gesture_name)
    if not os.path.exists(gesture_dir):
        os.makedirs(gesture_dir)
    
    cap = cv2.VideoCapture(0)
    
    print(f"\n{'='*60}")
    print(f"Collecting data for gesture: {gesture_name}")
    print(f"Target samples: {num_samples}")
    print(f"Press 's' to start/pause collection")
    print(f"Press 'q' to finish this gesture")
    print(f"{'='*60}\n")
    
    collecting = False
    count = 0
    frame_interval = 1.0 / CAPTURE_FPS
    last_capture_time = 0
    
    while count < num_samples:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Flip frame horizontally for mirror effect
        frame = cv2.flip(frame, 1)
        
        # Display info on frame
        info_text = f"Gesture: {gesture_name} | Collected: {count}/{num_samples}"
        status_text = "COLLECTING" if collecting else "PAUSED"
        cv2.putText(frame, info_text, (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, status_text, (10, 60), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, 
                   (0, 255, 0) if collecting else (0, 0, 255), 2)
        
        # Capture frame if collecting
        if collecting:
            current_time = time.time()
            if current_time - last_capture_time >= frame_interval:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                filename = f"{gesture_name}_{timestamp}_{count:04d}.jpg"
                filepath = os.path.join(gesture_dir, filename)
                cv2.imwrite(filepath, frame)
                count += 1
                last_capture_time = current_time
                print(f"Captured: {filename}")
        
        cv2.imshow('Data Collection', frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            collecting = not collecting
            print(f"Collection {'started' if collecting else 'paused'}")
        elif key == ord('q'):
            print(f"Finished collecting {gesture_name}: {count} samples")
            break
    
    cap.release()
    cv2.destroyAllWindows()
    return count


def main():
    """Main data collection workflow."""
    create_output_directory()
    
    print("="*60)
    print("HAND GESTURE DATA COLLECTION")
    print("="*60)
    print("\nGesture classes to collect:")
    for i, gesture in enumerate(GESTURE_CLASSES, 1):
        print(f"  {i}. {gesture}")
    
    input("\nPress Enter to start collection...")
    
    total_samples = 0
    for gesture in GESTURE_CLASSES:
        samples = collect_gesture_data(gesture)
        total_samples += samples
        
        print(f"\n✓ Completed {gesture}: {samples} samples")
        
        if gesture != GESTURE_CLASSES[-1]:
            input("\nPress Enter to continue to next gesture...")
    
    print("\n" + "="*60)
    print(f"DATA COLLECTION COMPLETE!")
    print(f"Total samples collected: {total_samples}")
    print(f"Data saved to: {OUTPUT_DIR}")
    print("="*60)


if __name__ == "__main__":
    main()
