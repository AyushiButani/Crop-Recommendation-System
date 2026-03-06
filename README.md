# Crop Recommendation System

End-to-end crop recommendation project (ML + API + UI + Docker) that predicts the best crop based on soil and weather conditions.

## What’s Included
- **ML Model (Python, scikit-learn, XGBoost/Random Forest):** trained on soil + weather features
- **Backend (Flask REST API):** serves predictions via API (model serialized with `joblib`)
- **Frontend (React):** UI to input features and view recommended crop
- **Streamlit Demo (optional):** quick interactive testing UI (inside `smart_recommender/`)
- **Docker (optional):** containerized setup for reproducible runs

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

## Run Locally (Recommended)

### 1) Backend (Flask REST API)
</> Bash
cd server/ml_backend

# create + activate virtual env
python3 -m venv venv
source venv/bin/activate

# install deps + run API
pip install -r requirements.txt
python app.py

2) Frontend (React)
cd frontend
npm install
npm start

Streamlit Demo
cd smart_recommender

# create + activate virtual env
python3 -m venv venv
source venv/bin/activate

# install deps + run Streamlit
pip install -r requirements.txt
streamlit run app.py

