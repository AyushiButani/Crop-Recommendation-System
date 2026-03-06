# 1. Start with a "Kitchen" that already has Python installed
FROM python:3.9-slim

# 2. Create a folder inside the container for our project
WORKDIR /app

# 3. Copy our "Shopping List" of tools and install them
COPY requirements.txt .
RUN pip install -r requirements.txt

# 4. Copy your App code and your AI Brain (.pkl file) into the container
COPY . .

# 5. Tell the container to open Port 8501 (Streamlit's default door)
EXPOSE 8501

# 6. The command to start the app when the box is opened
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]