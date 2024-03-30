import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

def main():
    # Load the dataset
    DataCar = pd.read_csv('CarPrice_Assignment.csv')

    # Drop NaN values, reset index, and drop duplicates
    DataCar.dropna(inplace=True)
    DataCar.reset_index(drop=True, inplace=True)
    DataCar.drop_duplicates(inplace=True)

    # One-hot encode categorical variables
    DataCar = pd.get_dummies(DataCar, columns=['fueltype', 'aspiration', 'carbody', 'drivewheel', 'enginelocation', 'enginetype', 'cylindernumber', 'fuelsystem'])

    # Selected features
    selected_features = ['horsepower', 'enginesize', 'curbweight', 'carwidth', 'highwaympg']

    # Prepare features and target
    X = DataCar[selected_features]
    y = DataCar['price']

    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'Mean Squared Error (MSE): {mse}')
    print(f'R-squared (R2): {r2}')

    # Save the trained model
    joblib.dump(model, 'model.pkl')

if __name__ == "__main__":
    main()
