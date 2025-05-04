from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model, label encoder, and symptom columns
model = joblib.load(r"C:\Users\pyank\OneDrive\Desktop\Programing\Data Analysis\Ella\disorder_app\disorder_model.pkl")
label_encoder = joblib.load(r"C:\Users\pyank\OneDrive\Desktop\Programing\Data Analysis\Ella\disorder_app\label_encoder.pkl")
symptom_columns = joblib.load(r"C:\Users\pyank\OneDrive\Desktop\Programing\Data Analysis\Ella\disorder_app\symptom_columns.pkl")

# Home page route
@app.route('/')
def home():
    return render_template('index.html', symptoms=symptom_columns)

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Create a dictionary with all symptoms set to 0
    input_data = {symptom: 0 for symptom in symptom_columns}
    
    # Get selected symptoms from the form
    selected_symptoms = request.form.getlist('symptoms')
    for symptom in selected_symptoms:
        input_data[symptom] = 1  # Mark the symptom as present (1)
    
    # Convert the dictionary to a DataFrame
    input_df = pd.DataFrame([input_data])

    # Make a prediction using the trained model
    prediction = model.predict(input_df)[0]
    
    # Decode the label using label encoder
    disorder = label_encoder.inverse_transform([prediction])[0]

    return render_template('index.html', symptoms=symptom_columns, prediction=disorder)

if __name__ == '__main__':
    app.run(debug=True)

# To run the Flask app, save this code in a file named `flask_app.py` and run it using the command:
# python flask_app.py
# Then, open your web browser and go to `http://
print("Thank you for using the disorder prediction app!")