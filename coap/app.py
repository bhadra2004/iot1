
from flask import Flask
import asyncio
from randomforest.client import get_environment

app = Flask(__name__)

@app.route("/")
def dashboard():
    try:
        data = asyncio.run(get_environment())
    except Exception as e:
        return "Error: " + str(e), 500

    html = """
    <html>
    <head>
        <title>Environmental Dashboard</title>
        <style>
            body {
                text-align: center;
                font-family: Arial;
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
        <h1>Environmental Monitoring Dashboard</h1>
        <table>
        <tr><th>Parameter</th><th>Value</th></tr>
    """

    for key, value in data.items():
        html += f"<tr><td>{key}</td><td>{value}</td></tr>"

    html += "</table></body></html>"
    return html

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
