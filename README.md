# 🌾 Crop Recommendation System

> **An end-to-end machine learning system that recommends the best crop to grow based on soil and weather conditions.**
> 
> Achieved **99% accuracy** with XGBoost. Published in **Gradiva Journal**.

[![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-Used-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![Flask](https://img.shields.io/badge/Flask-REST_API-black?logo=flask)](https://flask.palletsprojects.com/)
[![React](https://img.shields.io/badge/React-Frontend-61DAFB?logo=react)](https://react.dev/)
[![Research Paper](https://img.shields.io/badge/Published-Gradiva_Journal-green)](https://github.com/AyushiButani/Crop-Recommendation-System/blob/main/Crop_Recommendation_Research_Paper.pdf)

---

## 📌 About This Project

This was my **final-year Bachelor's capstone project**, built by a team of 3. It uses machine learning to support sustainable agriculture by helping farmers make data-driven crop decisions based on soil nutrients (N, P, K), temperature, humidity, soil pH, and rainfall.

The system covers the full ML lifecycle: from raw data to a trained model to a deployed REST API with a React frontend, where a user enters their conditions and gets a recommended crop in real time.

---

## 👥 Team & My Role

This was a 3-person group project. I led the **entire Data Science and Data Analytics side** of the work, along with the research paper and project documentation. My teammates worked on the React frontend and full-stack integration.

### 🎯 My Contributions

**Data Analysis & Preprocessing**
- Performed Exploratory Data Analysis on soil and weather data across **22 crop categories** and **7 input features**
- Cleaned the data: handled missing values, normalized features, and prepared model-ready inputs
- Built correlation analysis and feature distributions using **pandas, Seaborn, and Matplotlib**

**Machine Learning**
- Trained and compared **3 classifiers**: Naive Bayes, Decision Tree, XGBoost
- Tuned hyperparameters using GridSearchCV and applied cross-validation for reliable evaluation
- Evaluated models on accuracy, precision, recall, and F1-score
- **Final model: XGBoost, 99% accuracy**, saved with `joblib` for deployment

**Deployment**
- Built a **Flask REST API** to serve real-time predictions from the trained model
- Designed the request/response schema so the React frontend could integrate cleanly

**Research & Documentation**
- Authored the **research paper published in Gradiva Journal** ([View Paper](https://github.com/AyushiButani/Crop-Recommendation-System/blob/main/Crop_Recommendation_Research_Paper.pdf))
- Wrote the project reports and technical documentation

---

## 🛠️ Tech Stack

| Layer | Tools |
|---|---|
| **Data & ML** | Python, pandas, NumPy, scikit-learn, Seaborn, Matplotlib |
| **Models** | XGBoost, Decision Tree, Naive Bayes |
| **Backend** | Flask (REST API) |
| **Frontend** | React.js, CSS *(teammate-owned)* |
| **Model Persistence** | joblib |

---

## 📊 Results

| Model | Accuracy |
|---|---|
| Decision Tree | ~90% |
| Naive Bayes | ~99% |
| **XGBoost** | **>99%** ✅ |

After comparing all three classifiers, XGBoost emerged as the top performer with the highest accuracy across the 7 input features (N, P, K, temperature, humidity, pH, rainfall). It was selected as the final production model due to its robust handling of non-linear feature relationships and consistent performance across all 22 crop categories.

---

## 📁 Repository Structure

| Folder / File | Description |
|---|---|
| `frontend/` | React frontend *(teammate-owned)* |
| `server/ml_backend/` | Flask REST API + trained ML model |
| `smart_recommender/` | Core ML logic, notebooks, training scripts |
| `Crop_Recommendation_Research_Paper.pdf` | Published research paper |
| `README.md` | This file |
---

## 🚀 How To Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/AyushiButani/Crop-Recommendation-System.git
cd Crop-Recommendation-System
```

### 2. Run the Flask backend
```bash
cd server/ml_backend
python -m venv venv
source venv/bin/activate    # macOS/Linux
# venv\Scripts\activate     # Windows
pip install -r requirements.txt
python app.py
```
Backend runs at `http://localhost:5000`

### 3. Run the React frontend
```bash
cd frontend
npm install
npm start
```
Frontend runs at `http://localhost:3000`

---

## 📄 Research Publication

This project supported a peer-reviewed research paper published in **Gradiva Journal**.

- 📘 [Research Paper (PDF)](https://github.com/AyushiButani/Crop-Recommendation-System/blob/main/Crop_Recommendation_Research_Paper.pdf)
- 📜 [Publication Certificate](https://github.com/AyushiButani/Crop-Recommendation-System/blob/main/Publication_Certificate_Gradiva.jpeg)

---

## 📫 Contact

I'm currently looking for full-time Data Analyst and Data Science roles.

- 📧 **Email:** ayushibutani9@gmail.com
- 💼 **LinkedIn:** [linkedin.com/in/ayushi-butani](https://www.linkedin.com/in/ayushi-butani/)
- 🌐 **GitHub:** [github.com/AyushiButani](https://github.com/AyushiButani)
- 📊 **Tableau Public:** [public.tableau.com/app/profile/ayushibutani](https://public.tableau.com/app/profile/ayushibutani)
