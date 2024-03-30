from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Car Price Prediction</title>
    </head>
    <body>
        <h1>Car Price Prediction</h1>
        <form action="/predict" method="post">
            <label for="horsepower">Horsepower:</label><br>
            <input type="number" id="horsepower" name="horsepower" required><br>
            <label for="enginesize">Engine Size:</label><br>
            <input type="number" id="enginesize" name="enginesize" required><br>
            <label for="curbweight">Curb Weight:</label><br>
            <input type="number" id="curbweight" name="curbweight" required><br>
            <label for="carwidth">Car Width:</label><br>
            <input type="number" id="carwidth" name="carwidth" required><br>
            <label for="highwaympg">Highway MPG:</label><br>
            <input type="number" id="highwaympg" name="highwaympg" required><br><br>
            <input type="submit" value="Predict">
        </form>
    </body>
    </html>
    """

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get user input from the form
        horsepower = float(request.form['horsepower'])
        enginesize = float(request.form['enginesize'])
        curbweight = float(request.form['curbweight'])
        carwidth = float(request.form['carwidth'])
        highwaympg = float(request.form['highwaympg'])

        # Make a prediction
        new_car_features = pd.DataFrame({
            'horsepower': [horsepower],
            'enginesize': [enginesize],
            'curbweight': [curbweight],
            'carwidth': [carwidth],
            'highwaympg': [highwaympg]
        })
        predicted_price = model.predict(new_car_features)

        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Result</title>
        </head>
        <body>
            <h1>Predicted Car Price</h1>
            <p>The predicted price of the car is: $""" + str(predicted_price[0]) + """</p>
        </body>
        </html>
        """

if __name__ == '__main__':
    app.run(port=5000)
