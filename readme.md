# Mental Disorder Prediction Web App

A machine learning-powered web application for predicting potential mental health disorders based on observed symptoms. The app uses a trained classifier and interactive UI to support early awareness and education on mental health.

## 🚀 Features

* Input multiple observed symptoms through an intuitive checklist.
* Predicts a likely disorder based on learned patterns.
* Designed for educational and awareness purposes only.
* Responsive, clean, and interactive user interface.

## 🧠 Tech Stack

* **Frontend:** HTML, CSS (custom + Tailwind), JS (optionally)
* **Backend:** Python, Flask
* **Model:** Scikit-learn (Random Forest Classifier)
* **Hosting (Dev):** ngrok (for tunnel access)

## 📁 Project Structure

```
mental-disorder-predictor/
├── static/
│   └── style.css         # Styling for the app
├── templates/
│   └── index.html        # Frontend interface
├── flask_app.py          # Flask server
├── model.pkl             # Trained ML model
├── symptom_columns.pkl   # List of symptoms used for input features
├── label_encoder.pkl     # Encoded labels for disorders
├── README.md             # Project info
├── LICENSE               # MIT License
└── requirements.txt      # Python dependencies
```

## 📦 Installation

### Prerequisites:

* Python 3.7+
* pip

### Steps:

```bash
# Clone the repository
git clone https://github.com/yourusername/mental-disorder-predictor.git
cd mental-disorder-predictor

# Create virtual environment
python -m venv venv
source venv/Scripts/activate     # On Windows Git Bash

# Install dependencies
pip install -r requirements.txt

# Run the app
python flask_app.py
```

### Optional: Access from other devices

```bash
# Start ngrok (after installing and authtoken setup)
ngrok http 5000
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This app is **not** a diagnostic tool. It is intended for educational purposes only and should not replace professional mental health advice, diagnosis, or treatment.

---

Developed with ❤️ by Titus Yankson
