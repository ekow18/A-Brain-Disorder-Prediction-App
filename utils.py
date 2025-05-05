import joblib
import os
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

# Load model files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, 'model')
model = joblib.load(os.path.join(MODEL_DIR, 'disorder_model.pkl'))
symptom_columns = joblib.load(os.path.join(MODEL_DIR, 'symptom_columns.pkl'))
label_encoder = joblib.load(os.path.join(MODEL_DIR, 'label_encoder.pkl'))

symptom_keywords = {
    'hallucinations': ['hearing voices', 'seeing things'],
    'insomnia': ['no sleep', 'can’t sleep', 'trouble sleeping'],
    'fatigue': ['tired', 'exhausted'],
    'anxiety': ['nervous', 'anxious'],
    'depressed mood': ['sad', 'hopeless', 'depressed'],
    # add more
}

def extract_symptoms(text):
    text = text.lower()
    tokens = word_tokenize(text)
    found = set()
    for symptom, keywords in symptom_keywords.items():
        if any(k in text for k in keywords):
            found.add(symptom)
    return list(found)

def predict_disorder(symptoms):
    input_vector = [0] * len(symptom_columns)
    for s in symptoms:
        if s in symptom_columns:
            input_vector[symptom_columns.index(s)] = 1
    prediction = model.predict([input_vector])[0]
    return label_encoder.inverse_transform([prediction])[0]
