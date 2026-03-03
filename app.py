from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained model
with open("model/house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    size = float(request.form['size'])

    input_data = pd.DataFrame({'Square_Feet': [size]})
    prediction = model.predict(input_data)

    return render_template('index.html',
                           prediction_text=f"Predicted House Price: ₹ {prediction[0]:,.2f}")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)