import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv('data/Threat_Detection_Dataset.csv')

# Preprocessing
df['protocol'] = df['protocol'].astype('category').cat.codes

# Create feature matrix X and target vector y
X = df[['source_ip', 'destination_ip', 'protocol', 'payload_size', 'anomaly_score']].copy()
y = df['threat_label']

# Convert IP columns to numerical values
X.loc[:, 'source_ip'] = X['source_ip'].apply(lambda ip: sum([int(octet) for octet in ip.split('.')]))
X.loc[:, 'destination_ip'] = X['destination_ip'].apply(lambda ip: sum([int(octet) for octet in ip.split('.')]))

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'models/threat_detection_model.pkl')
print("Threat detection model trained and saved.")
