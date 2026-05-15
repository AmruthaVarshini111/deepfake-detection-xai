# DeepFake Detection using Explainable AI

This project explores deepfake and manipulated image detection using deep learning techniques.

The goal is to classify images as real or fake and understand what the model focuses on during prediction.

Current work:
- image preprocessing
- dataset preparation
- baseline CNN implementation
- Grad-CAM based visualization

Tech used:
Python • PyTorch • OpenCV • NumPy • Matplotlib

Project structure:

```text
deepfake-detection-xai/
├── data/
├── notebooks/
├── src/
├── models/
├── results/
└── requirements.txt
```
## Project Pipeline

1. Image preprocessing
2. CNN-based deepfake classification
3. Prediction generation
4. Grad-CAM based explainability
5. Heatmap visualization

## Future Work

- Real Grad-CAM implementation
- Training on benchmark datasets
- Better generalization across manipulations
- Transformer-based architectures
- Web deployment using Streamlit
## Sample Run

The explainability pipeline successfully generated Grad-CAM based visual explanations for prediction analysis.

Example execution:

```bash
python src/predict.py
python src/explain.py
```

Output generated inside the `results/` directory.