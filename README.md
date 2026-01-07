# Road Damage Detection

A comprehensive Streamlit-based web application for detecting and assessing road damage, particularly potholes, using advanced computer vision techniques. The application integrates image processing, machine learning models, and data analysis for urban mobility solutions.

## Features

### 🔐 User Authentication
- Secure login system with user registration
- Password reset functionality
- Session management

### 🖼️ Image Processing & Pothole Detection
- Upload images for pothole detection
- Real-time image resizing and preprocessing
- Contour detection using OpenCV
- Grayscale conversion and morphological operations
- Edge detection and filtering

### 🎥 Video Damage Assessment
- Upload video files for road damage analysis
- YOLO-based object detection for potholes
- Real-time damage percentage calculation
- Smoothed damage assessment using moving averages
- Video output with damage overlays

### 📊 Demand Prediction (Optional)
- CSV data upload for transportation demand analysis
- Linear regression modeling
- Interactive visualizations:
  - Ticket distribution histograms
  - Location-based ride counts
  - Car type distributions
  - Capacity analysis
  - Time-series scatter plots

## Technology Stack

- **Frontend**: Streamlit
- **Computer Vision**: OpenCV, Ultralytics YOLO
- **Machine Learning**: Scikit-learn, PyTorch
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Authentication**: Streamlit Authenticator
- **Image Handling**: Pillow

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/road-damage-detection.git
   cd road-damage-detection
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the YOLO model**:
   - Place your trained YOLO model file (`best.pt`) in a `model/` directory
   - Ensure the model path in `app.py` matches your setup

5. **Configure authentication**:
   - Update `config.yaml` with your desired user credentials
   - Modify cookie settings as needed

## Usage

1. **Run the application**:
   ```bash
   streamlit run app.py
   ```

2. **Access the app**:
   - Open your browser and navigate to `http://localhost:8501`
   - Log in using the configured credentials

3. **Image Analysis**:
   - Upload a JPG image in the "Image Section"
   - View processed images and detection results

4. **Video Analysis**:
   - Upload an MP4 video in the "Video Section"
   - Watch the processed video with damage assessment overlay

5. **Demand Prediction** (if enabled):
   - Upload a CSV file with transportation data
   - Explore various visualizations and analyses

## Project Structure

```
road-damage-detection/
│
├── app.py                 # Main Streamlit application
├── demand.py              # Demand prediction module
├── config.yaml            # Authentication configuration
├── requirements.txt       # Python dependencies
│
├── annotations/           # XML annotation files for training
├── model/                 # Trained YOLO model (not included)
│
├── .venv/                 # Virtual environment
├── .qodo/                 # Development tools
│
└── README.md              # Project documentation
```

## Model Training

The pothole detection uses a YOLO (You Only Look Once) model trained on annotated images. To train your own model:

1. Prepare annotated images in PASCAL VOC format (XML files in `annotations/`)
2. Use Ultralytics YOLO for training:
   ```python
   from ultralytics import YOLO
   model = YOLO('yolov8n-seg.pt')  # or your base model
   model.train(data='data.yaml', epochs=100)
   ```

## Configuration

### Authentication
Edit `config.yaml` to add/remove users:
```yaml
credentials:
  usernames:
    username:
      email: user@example.com
      name: User Name
      password: hashed_password
```

### Model Settings
Adjust detection parameters in `app.py`:
- Confidence threshold: `conf=0.25`
- Image size: `imgsz=640`

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Ultralytics for the YOLO implementation
- Streamlit for the web framework
- OpenCV community for computer vision tools
- Scikit-learn for machine learning utilities

## Future Enhancements

- [ ] Real-time video streaming
- [ ] Mobile app development
- [ ] Integration with GIS systems
- [ ] Advanced damage classification
- [ ] Automated reporting system
- [ ] Multi-language support
