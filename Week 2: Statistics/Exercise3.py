import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib
matplotlib.use('TkAgg') #Had issues with the weyland backend for matplotlib
import matplotlib.pyplot as plt

data = pd.read_csv('Car_Data.csv')

#print(data.head())

#----------DESCRIPTIVE STATS----------

print("Correlation between Price and Mileage: ")

p_corr = data.corr(method="pearson", min_periods=1)
print(f"Pearson: {p_corr["Price"]["Mileage"]}")

k_corr = data.corr(method="kendall", min_periods=1)
print(f"Kendall: {k_corr["Price"]["Mileage"]}")

s_corr = data.corr(method="spearman")
print(f"Spearman: {s_corr["Price"]["Mileage"]}")

c_corr = data.corr()
print(f"correlation coefficient: {c_corr["Price"]["Mileage"]}")

#Doing it the hard way

delta_price = delta_price = 0
sum1 = sum2 = sum3 = 0

for i in range(len(data.columns)):
    delta_mileage = int(data.iloc[i+1]["Mileage"]) - int(data.iloc[i]["Mileage"])
    delta_price = int(data.iloc[i+1]["Price"]) - int(data.iloc[i]["Price"])

    sum1 = delta_mileage*delta_price + sum1

    sum2 = delta_mileage*delta_mileage + sum2
    sum3 = delta_price*delta_price + sum3

corr_coeff = sum1 / (np.sqrt(sum2)*np.sqrt(sum3))
print(f"correlation coefficient2: {corr_coeff}")

#----------LINEAR REGRESSION----------

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error

from sklearn.model_selection import train_test_split


X_train, X_val, y_train, y_val = train_test_split(data['Mileage'].values.reshape(-1, 1), data['Price'].values, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predicted_train = model.predict(X_train)
predicted_val = model.predict(X_val)

mse_train = mean_squared_error(y_train, predicted_train)
mse_val = mean_squared_error(y_val, predicted_val)

print(f"Training mse: {mse_train}")
print(f"Validation mse: {mse_val}")

plt.figure(figsize=(10, 5))

plt.scatter(X_train, y_train, color='blue', label='Training Data')
plt.plot(X_train, predicted_train, color='red', label='Model Prediction on Training Data')

plt.scatter(X_val, y_val, color='green', label='Validation Data')
plt.plot(X_val, predicted_val, color='orange', linestyle='--', label='Model Prediction on Validation Data')

plt.xlabel('Mileage')
plt.ylabel('Price')
plt.title('Linear Regression: Training vs Validation')
plt.legend()
plt.show()

while True:
    try:
        mileage = int(input("Enter mileage: "))
        if mileage < 0:
            print("Please enter a positive number")
            continue
        
        pris = model.predict([[mileage]])[0]
        print(f"{pris.round(0)} USD")

        break
    except ValueError:
        print("Please enter a valid number")


