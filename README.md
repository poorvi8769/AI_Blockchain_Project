AI_Blockchain_Project/
│
├── app/                           # Flask application folder
│   ├── templates/                 # HTML templates for the web interface
│   │   ├── index.html
│   │   ├── upload.html
│   │   ├── report.html
│   ├── static/                    # Static files (CSS, JS)
│   ├── __init__.py
│   ├── app.py                     # Flask app entry point
│   ├── blockchain.py              # Blockchain integration logic
│   ├── prediction.py              # Model prediction logic
│   └── utils.py                   # Utility functions
│
├── models/                        # Saved models
│   ├── threat_detection_model.pkl
│   ├── anomaly_detection_model.pkl
│   └── resolution_time_model.pkl
│
├── data/                          # Sample datasets
│   ├── Threat_Detection_Dataset.csv
│   ├── Secure_Data_Dataset.csv
│   ├── Blockchain_Transactions_Dataset.csv
│   └── AI_Model_Training_Dataset.csv
│
├── scripts/                       # Model training scripts
│   ├── train_threat_model.py
│   ├── train_anomaly_model.py
│   └── train_resolution_time_model.py
│
├── requirements.txt               # Required Python libraries
├── README.md                      # Project documentation
└── run_project.sh                 # Shell script to set up and run the project
















1. Prerequisites
Before running the project, ensure you have the required software installed:

Python 3.8+: Install Python from the official website.
pip: Comes with Python; verify installation with pip --version.
Node.js (Optional, for blockchain testing): Install from Node.js official website.
Ganache (Blockchain): Install Ganache for local Ethereum blockchain testing.

2. Project Setup
Clone the Repository:

bash
Copy code
git clone https://github.com/poorvi8769/AI_Blockchain_Project.git
cd AI_Blockchain_Project
Create and Activate a Virtual Environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
Install Dependencies: Install all required Python libraries:

bash
Copy code
pip install -r requirements.txt

3. Train the AI Models
Train the models using the provided scripts:

Train Threat Detection Model:

bash
Copy code
python scripts/train_threat_model.py
Train Anomaly Detection Model:

bash
Copy code
python scripts/train_anomaly_model.py
Train Resolution Time Model:

bash
Copy code
python scripts/train_resolution_time_model.py
Each script will save the trained models in the models/ folder.

4. Set Up Blockchain
Start Ganache: Launch Ganache to create a local Ethereum blockchain. Use the default HTTP provider (http://127.0.0.1:8545).

Configure Web3:

Ensure blockchain.py connects to the correct blockchain endpoint (http://127.0.0.1:8545).
Use Ganache-provided accounts for transactions.


5. Run the Flask Application
Start the Flask App:

bash
Copy code
python app/app.py
Access the Application: Open your browser and navigate to:

arduino
Copy code
http://127.0.0.1:5000


6. Analyze Test Data
Upload a Test File:

Use the "Upload CSV" form on the web interface.
Supported test files include datasets like the Threat_Detection_Dataset.csv.
View Results:

The app processes the file using the trained models.
Displays the predictions and analysis results on the "Report" page.
Blockchain Report Hashing:

The analysis report is hashed and stored on the blockchain.
You can verify the report’s integrity via the hash.


7. Verify Report Integrity
Obtain the Report Hash:

The generated hash will be displayed on the "Report" page.
Verify the Hash:

Use the /verify endpoint or a blockchain tool to validate the hash against the stored value.


8. Optional: Use Automation Script
You can automate the entire setup and execution using the run_project.sh script:

Make the script executable:

bash
Copy code
chmod +x run_project.sh
Run the script:

bash
Copy code
./run_project.sh
This script sets up the environment, installs dependencies, trains models, and starts the Flask application.

9. Testing and Debugging
Testing Models: Use test CSV files and observe the predictions.
Debugging Blockchain: Monitor transactions in Ganache to ensure reports are being hashed correctly.
Flask Logs: Check logs in the terminal for any application errors.


10. Deployment
To deploy this project:

Host Flask App:

Use platforms like AWS, Azure, or Heroku for hosting.
Update the blockchain provider (e.g., Infura or Alchemy) for production.
Configure Blockchain:

Migrate from Ganache to a live Ethereum testnet (e.g., Goerli or Ropsten).
Update blockchain.py with the testnet endpoint.
