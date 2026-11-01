
from flask import Flask
import requests

app = Flask(__name__)

url = "https://wxwrolktzxqlxwxhsbtz.supabase.co/rest/v1/sensor_data"
key = "sb_publishable_E3CHxZ57Q_aTaNXpx1cR0Q_djba1JJ6"

headers = {
    "apikey": key
}

@app.route("/")
def dashboard():
    try:
        response = requests.get(
            url + "?select=*&order=id.desc&limit=10",
            headers=headers,
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
    except (requests.RequestException, ValueError):
        return "Unable to fetch sensor data"

    html = """
    <html>
    <head>
        <title>IoT Dashboard</title>
        <meta http-equiv="refresh" content="5">
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
                padding: 12px 25px;
                border: 1px solid #ccc;
            }
            th {
                background: #2563eb;
                color: white;
            }
        </style>
    </head>
    <body>
        <h1>Temperature and Humidity Dashboard</h1>
        <table>
            <tr>
                <th>Temperature (°C)</th>
                <th>Humidity (%)</th>
            </tr>
    """

    for row in data:
        html += f"""
        <tr>
            <td>{row['temperature']}</td>
            <td>{row['humidity']}</td>
        </tr>
        """

    html += "</table></body></html>"
    return html

if __name__ == "__main__":
    app.run(debug=True)
