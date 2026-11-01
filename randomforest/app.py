
from flask import Flask
import asyncio
import joblib
import pandas as pd
from randomforest.client import get_air

app = Flask(__name__)
model = joblib.load("air_model.pkl")

@app.route("/")
def dashboard():
    try:
        data = asyncio.run(get_air())

        features = ["PM2.5", "PM10", "NO2", "SO2", "O3"]
        X = pd.DataFrame([data], columns=features)

        prediction = model.predict(X)[0]

    except Exception as e:
        return "Error: " + str(e), 500

    html = """
    <html>
    <head>
        <title>Air Quality Dashboard</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                background: #eef2f7;
            }
            table {
                margin: auto;
                border-collapse: collapse;
                background: white;
            }
            th, td {
                border: 1px solid gray;
                padding: 12px 25px;
            }
            th {
                background: #2563eb;
                color: white;
            }
        </style>
    </head>
    <body>
        <h1>Air Quality Monitoring Dashboard</h1>
        <table>
            <tr>
                <th>Parameter</th>
                <th>Value</th>
            </tr>
    """

    for key, value in data.items():
        html += f"<tr><td>{key}</td><td>{value}</td></tr>"

    html += "</table>"
    html += f"<h2>Predicted Air Quality: {prediction}</h2>"
    html += "</body></html>"

    return html

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
