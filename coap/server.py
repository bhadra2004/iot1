
import asyncio
import json
import requests
import aiocoap
import aiocoap.resource as resource

weather_url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=10.0159&longitude=76.3419"
    "&current=temperature_2m,relative_humidity_2m,weather_code"
)

air_url = (
    "https://air-quality-api.open-meteo.com/v1/air-quality"
    "?latitude=10.0159&longitude=76.3419"
    "&current=pm10,pm2_5,carbon_monoxide,"
    "nitrogen_dioxide,ozone,european_aqi"
)

db_url = "https://wxwrolktzxqlxwxhsbtz.supabase.co/rest/v1/environment_data"
key = "sb_publishable_E3CHxZ57Q_aTaNXpx1cR0Q_djba1JJ6"

headers = {
    "apikey": key,
    "Content-Type": "application/json"
}

def get_data():
    weather = requests.get(weather_url, timeout=15)
    air = requests.get(air_url, timeout=15)

    weather.raise_for_status()
    air.raise_for_status()

    w = weather.json()["current"]
    a = air.json()["current"]

    data = {
        "temperature": w["temperature_2m"],
        "humidity": w["relative_humidity_2m"],
        "weather_code": w["weather_code"],
        "pm10": a["pm10"],
        "pm2_5": a["pm2_5"],
        "carbon_monoxide": a["carbon_monoxide"],
        "nitrogen_dioxide": a["nitrogen_dioxide"],
        "ozone": a["ozone"],
        "european_aqi": a["european_aqi"]
    }

    response = requests.post(
        db_url, json=data, headers=headers, timeout=15
    )
    print("Database Status:", response.status_code)
    if response.status_code != 201:
        print(response.text)

    return data

class Environment(resource.Resource):
    async def render_get(self, request):
        try:
            data = await asyncio.to_thread(get_data)
            print("CoAP GET:", data)
            return aiocoap.Message(
                code=aiocoap.CONTENT,
                payload=json.dumps(data).encode()
            )
        except Exception as e:
            return aiocoap.Message(
                code=aiocoap.INTERNAL_SERVER_ERROR,
                payload=str(e).encode()
            )

async def main():
    site = resource.Site()
    site.add_resource(["environment"], Environment())

    await aiocoap.Context.create_server_context(
        site, bind=("127.0.0.1", 5683)
    )

    print("CoAP Server Running on port 5683")
    await asyncio.get_running_loop().create_future()

asyncio.run(main())
