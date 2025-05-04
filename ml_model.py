import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load merged data
data = pd.read_csv(r"C:\Users\pyank\OneDrive\Desktop\Programing\Data Analysis\Ella\merged_final.csv")

# Drop rows where the target 'Disorder Name' is missing
data = data.dropna(subset=['Disorder Name'])

# Drop unnecessary columns (keep only symptom-related + target)
symptom_columns = [
    col for col in data.columns 
    if col not in ['Disorder Category', 'DSM-5 Code (ICD-9)', 'DSM-5 Code (ICD-10)', 'Page Number', 'Specifiers/Notes', 'Disorder Name']
]
X = data[symptom_columns].fillna(0)

# Encode the target variable
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(data['Disorder Name'])

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model performance
from sklearn.metrics import accuracy_score, classification_report
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Create a directory to save the files if it doesn't exist
output_dir = r"C:\Users\pyank\OneDrive\Desktop\Programing\Data Analysis\Ella\disorder_app"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the trained model, label encoder, and symptom columns
model_file = os.path.join(output_dir, 'disorder_model.pkl')
label_encoder_file = os.path.join(output_dir, 'label_encoder.pkl')
symptom_columns_file = os.path.join(output_dir, 'symptom_columns.pkl')

# Save model, label encoder, and symptom columns
joblib.dump(model, model_file)
joblib.dump(label_encoder, label_encoder_file)
joblib.dump(X.columns.tolist(), symptom_columns_file)

print("Model and related files saved successfully at:")
print(f"Model saved to: {model_file}")
print(f"Label Encoder saved to: {label_encoder_file}")
print(f"Symptom Columns saved to: {symptom_columns_file}")
