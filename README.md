# Crop Recommendation System

End-to-end crop recommendation project (ML + API + UI + Docker) that predicts the best crop based on soil and weather conditions.

## What’s Included
- **ML Model (Python, scikit-learn, XGBoost/Random Forest):** trained on soil + weather features
- **Backend (Flask REST API):** serves predictions via API (model serialized with `joblib`)
- **Frontend (React):** UI to input features and view recommended crop
- **Smart Recommender Module:** notebooks/scripts + Streamlit demo for interactive testing
- **Docker:** containerized setup for reproducible runs

---

## Repository Structure
- `frontend/` — React UI
- `server/ml_backend/` — Flask API + model + backend code
- `smart_recommender/` — notebooks/scripts + Streamlit demo + Dockerfile (if present)

---

## Model Inputs
Soil + weather features:
- **N, P, K, temperature, humidity, pH, rainfall**

---

## Run Locally

### 1) Backend (Flask REST API)

cd server/ml_backend

# create + activate virtual env
python3 -m venv venv
source venv/bin/activate

# install deps + run API
pip install -r requirements.txt
python app.py


