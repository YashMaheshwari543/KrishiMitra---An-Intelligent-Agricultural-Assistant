# 🌾 KrishiMitra - Intelligent Agricultural Assistant

An AI-powered Smart Agriculture Assistant that helps farmers make data-driven decisions through Machine Learning and Deep Learning models.

KrishiMitra provides crop recommendations, fertilizer suggestions, plant disease detection, and access to government agricultural schemes through an easy-to-use Streamlit web application.

---

## 🚀 Features

### 🌾 Crop Recommendation System

Predicts the most suitable crop based on soil and environmental conditions such as:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* pH Value
* Rainfall

### 🌱 Fertilizer Recommendation System

Recommends the most appropriate fertilizer based on:

* Soil Type
* Crop Type
* Temperature
* Humidity
* Moisture
* NPK Values

### 🦠 Crop Disease Detection

Uses a Deep Learning CNN model to identify plant diseases from leaf images.

Supported Classes:

* Healthy
* Leaf Spot
* Blight
* Rust

### 📜 Government Schemes Information

Provides quick access to important agricultural schemes and farmer welfare programs.

---

## 🛠️ Technology Stack

### Programming Language

* Python

### Machine Learning & Deep Learning

* Scikit-Learn
* PyTorch
* NumPy
* Pandas

### Web Framework

* Streamlit

### Data Visualization

* Matplotlib

### Image Processing

* Pillow (PIL)
* TorchVision

---

## 📂 Project Structure

```text
KrishiMitra/
│
├── app.py
├── Crop_Page.py
├── Fertilizer_Page.py
├── Crop_Disease_Page.py
│
├── model.pkl
├── fertilizer_model.pkl
├── new_model.pth
│
├── Dataset/
│
├── CropRecommendation.ipynb
├── FertilizerRecommendation.ipynb
├── Crop_disease.ipynb
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YashMaheshwari543/KrishiMitra---An-Intelligent-Agricultural-Assistant.git
```

### Move to Project Directory

```bash
cd KrishiMitra---An-Intelligent-Agricultural-Assistant
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🎯 Project Workflow

1. Collect agricultural datasets
2. Perform data preprocessing
3. Train ML models for crop and fertilizer prediction
4. Train CNN model for disease detection
5. Deploy models using Streamlit
6. Generate real-time recommendations

---

## 📈 Key Highlights

* End-to-End Machine Learning Project
* Deep Learning Based Disease Classification
* Interactive Streamlit Dashboard
* Real-World Agriculture Use Case
* Multiple AI Modules in a Single Platform

---

## 🔮 Future Enhancements

* Weather API Integration
* Multi-language Support
* Mobile Application
* Real-time Disease Detection
* Crop Yield Prediction
* Market Price Forecasting

---

## 👨‍💻 Author

**Yash Maheshwari**

MCA | Data Analytics & Data Science Enthusiast

GitHub: https://github.com/YashMaheshwari543

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
