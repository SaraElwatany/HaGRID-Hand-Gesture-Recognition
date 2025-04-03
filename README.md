# HaGRID Hand Gesture Recognition


## Overview

This project implements hand gesture recognition using classical machine learning models trained on the HaGRID dataset. The final model is a voting classifier composed of the top-performing models to enhance robustness and accuracy.


## Features

- Preprocessed HaGRID Dataset in CSV format.

- Multi-model Voting Classifier combining:

    - SVM with Polynomial Kernel

    - SVM with RBF Kernel

    - Random Forest

    - Extra Trees Classifier

    - Extreme Gradient Boosting (XGBoost)

- Video-based Gesture Prediction using OpenCV & MediaPipe.

- Notebook for Testing on Video.

- Python Script for Local Video Capture.

- Automatic Gesture Stabilization using mode over a sliding window.


# Dataset

The dataset has been stored as a CSV file for easier loading and training. It contains landmark coordinates extracted from HaGRID and labeled gestures.


# Installation


**1- Clone the repository**

```bash
git clone https://github.com/your-username/hagrid-gesture-recognition.git
cd hagrid-gesture-recognition
```

**2- Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate              # On Windows use: venv\Scripts\activate
```

**3- Install dependencies**

```bash
pip install -r requirements.txt
```

# Usage


**1. Train the Model**

Run the training script to train models and save the best ones:

```bash
jupyter Machine_Learning_Model_Building_Final_Project.ipynb
```

**2. Test on Video**

Use the provided Jupyter Notebook to test gestures on a video file:

```bash
jupyter notebook video_test.ipynb
```

**3. Capture and Predict Gestures from Webcam**

Use the Python script to capture video from a webcam and recognize gestures in real-time:

```bash
python capture_video.py
```


# Model Evaluation

|           Model          | Accuracy (%) |   
|--------------------------|--------------|  
|  SVM (Polynomial Kernel) | 97.8 |  
| XGBoost | 97.6 |  
| SVM (RBF Kernel) | 97.3 |  
| Extra-Trees Classifier | 96.5 |  
| Random Forest | 95.1 |  
| Voting Classifier (Final) | 98.1 |


# Results & Stabilization

- The final model achieves 98.1% accuracy.

- To reduce sudden prediction fluctuations, a mode-based sliding window is applied.


# Contributing

Feel free to open issues, suggest improvements, or submit pull requests.


# Acknowledgments

- **HaGRID Dataset:** [Paper Link](https://paperswithcode.com/dataset/hagrid)
- **MediaPipe Hands:** [Google MediaPipe](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker)


# Contact

For any inquiries, reach out via:
📧 Email: sara.abdullah00@eng-st.cu.edu.eg   🔗 GitHub: SaraElwatany
