# 🎭 Face Emotion Recognition System

## 📌 Overview

This project is a real-time face emotion recognition system that detects human faces from webcam video and classifies emotions using a deep learning model.

It combines computer vision techniques with a CNN-based model to identify emotions such as **happy, sad, angry, surprised, neutral, fear, and disgust**.

---

## 🚀 Features

- Real-time face detection from webcam
- Emotion classification (7 classes)
- Supports HOG and CNN face detection methods
- Lightweight and easy to run

---

## 🧠 Tech Stack

- Python
- OpenCV
- Dlib
- face_recognition
- TensorFlow / Keras

---

## ⚙️ Installation

### 1. Create Environment

```bash
conda create -n emotion python=3.10
conda activate emotion
```

### 2. Install Dependencies

```bash
pip install cmake
pip install opencv-python
conda install -c conda-forge dlib
pip install face_recognition
pip install tensorflow keras
```

> ⚠️ Note: Avoid using Python 3.6. It is outdated and may cause installation issues.

---

## ▶️ Run the Project

```bash
cd src
python faceDetectionImpl.py
```

---

## 📦 Model Files

- Model structure: `model/model.json`
- Model weights:

👉 Download here: **[Google Drive Link HERE]**

> (Weights file is large, so it is hosted externally)

---

## 🧠 Face Detection Methods

### 🔹 HOG (Histogram of Oriented Gradients)

**Pros:**

- Fast on CPU
- Lightweight

**Cons:**

- Requires frontal face
- Less accurate for side angles or occlusion

---

### 🔹 CNN (Dlib)

**Pros:**

- Higher accuracy
- Handles multiple face angles

**Cons:**

- Slower on CPU
- Requires GPU for best performance

---

## 📊 Model Details

- Input: 48x48 grayscale images
- Output: 7 emotion classes
- Architecture: CNN (Convolutional Neural Network)

---

## 💡 Future Improvements

- Deploy as a web application (Flask / FastAPI)
- Improve model accuracy
- Add emotion tracking over time
- Optimize performance for real-time usage

---

## 👨‍💻 Author

**San Sonan**
Backend Developer | Java Spring Boot | AI Enthusiast
