# Crop Recommendation System

End-to-end crop recommendation project with:
- **Frontend (React)**: UI for entering soil + weather inputs and viewing predicted crop
- **Backend (Flask REST API)**: serves the trained model via API
- **Model**: trained using soil + weather features (N, P, K, temperature, humidity, pH, rainfall)

## Repo Structure
- `frontend/` – React UI
- `server/ml_backend/` – Flask API + model files + backend code

## How to Run (Local)

### 1) Backend (Flask API)

cd server/ml_backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py

### 2) Frontend (React)
cd frontend
npm install
npm start

### 3)Docker
docker build -t crop-recommendation .
docker run -p 5000:5000 crop-recommendation

