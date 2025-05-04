#!/bin/bash

echo "Setting up the AI and Blockchain Project..."

# Step 1: Set up virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Step 2: Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Step 3: Train models
echo "Training models..."
python scripts/train_threat_model.py
python scripts/train_anomaly_model.py
python scripts/train_resolution_time_model.py

# Step 4: Run the Flask application
echo "Starting the Flask application..."
python app/app.py
