import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
df = pd.read_csv('data/AI_Model_Training_Dataset.csv')

# Preprocessing: Extract features and target
X = df['features'].apply(lambda x: [float(f) for f in x.split(',')]).tolist()
y = df['resolution_time']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'models/resolution_time_model.pkl')
print("Resolution time model trained and saved.")
