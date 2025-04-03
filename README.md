Diabetes Prediction API
This project is a Flask-based API for predicting diabetes using machine learning. The model is trained using random forest (RF) and can predict whether a person has diabetes based on their medical data.

🚀 Features
Accepts JSON input via a POST request

Uses a pre-trained RF model

Returns prediction results (1 = Diabetes, 0 = No Diabetes)

Built with Flask, Scikit-Learn, and NumPy

📂 Project Structure
bash
Copy
Edit
├── model.pkl               # Trained RF model
├── app.py                  # Flask API script
├── requirements.txt        # Dependencies
├── README.md               # Project Documentation
└── dataset.csv             # (Optional) Dataset used for training
📦 Installation
Clone the repository:

sh
Copy
Edit
git clone https://github.com/Ajmeer-007/diabetes-prediction.git
cd diabetes-prediction
Install dependencies:

sh
Copy
Edit
pip install -r requirements.txt
Run the Flask server:

sh
Copy
Edit
python app.py
🔥 API Usage
Send a POST request with patient data:

sh
Copy
Edit
curl -X POST "http://127.0.0.1:5000/predict" \
     -H "Content-Type: application/json" \
     -d '{
          "pregnancies": 0,
          "glucose": 108,
          "bp": 88,
          "st": 33,
          "insulin": 111,
          "bmi": 35,
          "dpf": 0.74,
          "age": 65
        }'
✅ Response:
json
Copy
Edit
{
  "prediction": 1
}
(1 = Diabetes detected, 0 = No diabetes)

🛠 Model Training
To retrain the model:

Open train_model.py (if available).

Train the model:

sh
Copy
Edit
python train_model.py
Save the new model as model.pkl.

🏆 Future Improvements
Improve model accuracy with hyperparameter tuning

Deploy using Docker & Cloud Services

Add a frontend UI for easier access

🤝 Contributing
Feel free to contribute! Fork the repo, create a branch, and submit a PR.
