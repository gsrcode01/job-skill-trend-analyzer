import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os

os.makedirs("output", exist_ok=True)
df = pd.read_csv("data/historical_trends.csv")

months = df["Month"].values.reshape(-1, 1)

python_demand = df["Python"].values

model = LinearRegression()

model.fit(months, python_demand)

next_month = np.array([[6]])

prediction = model.predict(next_month)

print("Predicted Python demand:", int(prediction[0]))

plt.figure(figsize=(8, 5))

plt.scatter(months, python_demand)

plt.plot(months, model.predict(months))

plt.scatter(next_month, prediction)

plt.xlabel("Month")

plt.ylabel("Python Demand")

plt.title("Python Demand Forecast")

plt.savefig("output/forecast.png")

print("Forecast graph generated successfully")

plt.close()
