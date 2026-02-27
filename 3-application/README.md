# Application Phase - Spotify Hand Controller

## Overview
This phase applies the trained hand gesture recognition model to control Spotify playback in real-time.

## Architecture

The application consists of four main components:

1. **Hand Detector** (`hand_detector.py`): Uses the trained model to detect hands and recognize gestures from webcam
2. **Gesture Mapping** (`gesture_mapping.py`): Maps recognized gestures to Spotify actions
3. **Spotify Controller** (`spotify_controller.py`): Interfaces with Spotify API to control playback
4. **Main Application** (`main.py`): Orchestrates all components

## Setup

### 1. Spotify API Credentials
You need to create a Spotify API application to get credentials:

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create a new app
3. Note your Client ID and Client Secret
4. Add `http://localhost:8888/callback` to Redirect URIs

### 2. Configuration
Copy the example configuration:
```bash
cp ../config/config.example.py ../config/config.py
```

Edit `../config/config.py` and add your Spotify credentials:
```python
SPOTIFY_CLIENT_ID = "your_client_id"
SPOTIFY_CLIENT_SECRET = "your_client_secret"
SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback"
```

### 3. Install Dependencies
```bash
pip install -r ../requirements.txt
```

## Running the Application

### Basic Usage
```bash
python main.py
```

### Command Line Arguments
```bash
python main.py --model-path ../models/saved_models/best_model.h5 \
               --camera-id 0 \
               --confidence-threshold 0.7
```

Arguments:
- `--model-path`: Path to trained model (default: ../models/saved_models/best_model.h5)
- `--camera-id`: Camera device ID (default: 0)
- `--confidence-threshold`: Gesture confidence threshold (default: 0.7)
- `--debug`: Enable debug visualization

## Gesture Controls

Default gesture mappings:

| Gesture | Spotify Action |
|---------|---------------|
| Open Palm | Pause/Play |
| Fist | Stop |
| Thumbs Up | Volume Up |
| Peace Sign | Next Track |
| Pointing | Previous Track |
| Swipe Left | Seek Backward |
| Swipe Right | Seek Forward |

## Customization

### Modify Gesture Mappings
Edit `gesture_mapping.py` to customize which gestures trigger which actions:

```python
GESTURE_ACTIONS = {
    'open_palm': 'play_pause',
    'fist': 'stop',
    'thumbs_up': 'volume_up',
    # Add your custom mappings
}
```

### Add New Gestures
1. Collect and annotate data for new gesture (Phase 1)
2. Retrain model with new gesture class (Phase 2)
3. Add mapping in `gesture_mapping.py`

## Troubleshooting

### Camera Not Working
- Check camera permissions
- Try different camera ID: `--camera-id 1`

### Spotify Connection Issues
- Ensure Spotify app is running
- Check API credentials in config
- Verify redirect URI is correct

### Poor Gesture Recognition
- Ensure good lighting
- Keep hand centered in frame
- Adjust confidence threshold
- Consider retraining model with more data

## Performance Tips

- **Lighting**: Use consistent, bright lighting
- **Background**: Plain backgrounds work best
- **Distance**: Keep hand 30-60cm from camera
- **Speed**: Perform gestures slowly and deliberately
- **Single Hand**: Use one hand at a time

## Development

### Testing Individual Components

Test hand detector:
```bash
python hand_detector.py --test
```

Test Spotify controller:
```bash
python spotify_controller.py --test
```

Test gesture mapping:
```bash
python gesture_mapping.py --test
```

### Running Tests
```bash
cd ../tests
pytest test_hand_detector.py
pytest test_spotify_controller.py
```

## Next Steps

- Experiment with different gesture mappings
- Add support for multi-hand gestures
- Integrate with other music services
- Create a GUI for easier control
