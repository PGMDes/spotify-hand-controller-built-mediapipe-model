# Spotify Hand Controller with MediaPipe

Control Spotify playback using hand gestures detected by MediaPipe.

## Project Structure

```
spotify-hand-controller-built-mediapipe-model/
│
├── data/                      # Data for model training
│   ├── raw/                  # Raw dataset files
│   ├── processed/            # Processed/cleaned datasets
│   └── annotations/          # Labeled data and annotations
│
├── notebooks/                 # Jupyter notebooks for experimentation
│
├── models/                    # Model files
│   ├── saved_models/         # Trained models
│   └── checkpoints/          # Training checkpoints
│
├── training/                  # Training scripts
│   ├── train.py             # Model training script
│   ├── evaluate.py          # Model evaluation script
│   └── utils.py             # Training utilities
│
├── src/                       # Application source code
│   ├── main.py              # Main entry point
│   ├── hand_detector.py     # Hand gesture detection
│   ├── spotify_controller.py # Spotify API integration
│   ├── gesture_mapping.py   # Gesture to action mapping
│   └── utils.py             # Application utilities
│
├── tests/                     # Unit tests
│   ├── test_hand_detector.py
│   └── test_spotify_controller.py
│
├── config/                    # Configuration files
│   ├── config.py            # Main configuration
│   └── config.example.py    # Example configuration
│
├── assets/                    # Images, icons, and other assets
│
├── docs/                      # Documentation
│
├── requirements.txt           # Python dependencies
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Spotify API

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create a new app and get your credentials
3. Copy `config/config.example.py` to `config/config.py`
4. Fill in your Spotify API credentials

### 3. Prepare Data (for model training)

Place your training data in the `data/raw/` directory.

### 4. Train Model (Optional)

If you want to train a custom model:

```bash
python training/train.py
```

### 5. Run Application

```bash
python src/main.py
```

## Gesture Mappings

- **Thumbs Up**: Play
- **Thumbs Down**: Pause
- **Swipe Right**: Next Track
- **Swipe Left**: Previous Track
- **Open Palm**: Volume Up
- **Closed Fist**: Volume Down

You can customize these mappings in `src/gesture_mapping.py`.

## Development Workflow

### Model Development

1. Collect and prepare data in `data/raw/`
2. Experiment in Jupyter notebooks (`notebooks/`)
3. Write training scripts in `training/`
4. Save trained models to `models/saved_models/`

### Application Development

1. Implement features in `src/`
2. Write tests in `tests/`
3. Update documentation in `docs/`
4. Test with `pytest tests/`

## Requirements

- Python 3.8+
- Webcam
- Spotify Premium account (for full playback control)

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Write tests
4. Submit a pull request

## License

MIT License

## Acknowledgments

- [MediaPipe](https://mediapipe.dev/) for hand detection
- [Spotipy](https://spotipy.readthedocs.io/) for Spotify API integration
