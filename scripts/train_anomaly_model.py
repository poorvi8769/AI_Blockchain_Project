import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load dataset
df = pd.read_csv('data/Secure_Data_Dataset.csv')

# Preprocessing: Extract relevant features
df['log_count'] = df['access_logs'].apply(lambda x: len(x.split(',')))
X = df[['log_count']]

# Train Isolation Forest for anomaly detection
model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
model.fit(X)

# Save the trained model
joblib.dump(model, 'models/anomaly_detection_model.pkl')
print("Anomaly detection model trained and saved.")
