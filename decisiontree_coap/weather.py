
import requests
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

url = "https://archive-api.open-meteo.com/v1/archive"

params = {
    "latitude": 10.0159,
    "longitude": 76.3419,
    "start_date": "2025-01-01",
    "end_date": "2025-12-31",
    "hourly": "temperature_2m,relative_humidity_2m,precipitation,cloud_cover,wind_speed_10m,surface_pressure,weather_code"
}

response = requests.get(url, params=params, timeout=60)
response.raise_for_status()

data = response.json()["hourly"]
df = pd.DataFrame(data)

def classify_weather(code):
    if code in [0, 1]:
        return "Clear"
    elif code in [2, 3]:
        return "Cloudy"
    elif code in [51, 53, 55]:
        return "Drizzle"
    elif code in [61, 63, 65]:
        return "Rain"
    else:
        return None

df["weather_class"] = df["weather_code"].apply(classify_weather)

df = df.dropna()

features = [
    "temperature_2m",
    "relative_humidity_2m",
    "precipitation",
    "cloud_cover",
    "wind_speed_10m",
    "surface_pressure"
]

X = df[features]
y = df["weather_class"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(
    max_depth=5,
    random_state=42
)

model.fit(X_train, y_train)

prediction = model.predict(X_test)

print("Weather Classification Using Decision Tree")
print("Accuracy:", accuracy_score(y_test, prediction))

print("\nSample Predictions:")
print(pd.DataFrame({
    "Actual": y_test.values[:10],
    "Predicted": prediction[:10]
}))
