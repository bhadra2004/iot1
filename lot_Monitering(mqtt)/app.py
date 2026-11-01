
from flask import Flask
import requests

app = Flask(__name__)

url = "https://wxwrolktzxqlxwxhsbtz.supabase.co/rest/v1/sensor_data"
key = "sb_publishable_E3CHxZ57Q_aTaNXpx1cR0Q_djba1JJ6"

headers = {"apikey": key}

@app.route("/")
def dashboard():
    response = requests.get(
        url + "?select=*&order=id.desc&limit=10",
        headers=headers,
        timeout=10
    )

    if response.status_code != 200:
        return "Database Error: " + response.text

    data = response.json()

    html = """
    <html>
    <head>
        <meta http-equiv="refresh" content="5">
    </head>
    <body style="text-align:center;font-family:Arial">
        <h1>MQTT Sensor Dashboard</h1>
        <table border="1" align="center" cellpadding="10">
        <tr><th>Temperature</th><th>Humidity</th></tr>
    """

    for row in data:
        html += f"<tr><td>{row['temperature']} C</td><td>{row['humidity']} %</td></tr>"

    html += "</table></body></html>"
    return html

if __name__ == "__main__":
    app.run(debug=True)
