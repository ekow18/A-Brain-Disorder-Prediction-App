from flask import Flask, render_template, request, session, redirect, url_for
from utils import extract_symptoms, predict_disorder
import os
import nltk
nltk.data.path.append('C:\Users\pyank\OneDrive\Desktop\Programing\Data Analysis\Ella\disorder_app\punkt')  # Adjust path as needed

app = Flask(__name__)
app.secret_key = 'super_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    session.clear()
    session['history'] = []
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    session['history'].append({'sender': 'user', 'message': user_input})

    symptoms = extract_symptoms(user_input)
    if not symptoms:
        bot_message = "Hmm, I didn’t catch any symptoms. Could you describe how you’re feeling in a bit more detail?"
    else:
        diagnosis = predict_disorder(symptoms)
        bot_message = f"Thanks for sharing. Based on what you said, it might be related to <strong>{diagnosis}</strong>. Remember, this isn’t a diagnosis — please talk to a professional."

    session['history'].append({'sender': 'bot', 'message': bot_message})
    return render_template('chat.html', history=session['history'])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
