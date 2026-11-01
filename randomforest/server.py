
import asyncio
import json
import requests
import aiocoap
import aiocoap.resource as resource

url = "https://air-quality-api.open-meteo.com/v1/air-quality"

params = {
    "latitude": 10.0159,
    "longitude": 76.3419,
    "current": "pm2_5,pm10,nitrogen_dioxide,sulphur_dioxide,ozone"
}

class AirQuality(resource.Resource):
    async def render_get(self, request):
        try:
            response = await asyncio.to_thread(
                requests.get, url, params=params, timeout=15
            )
            response.raise_for_status()
            data = response.json()["current"]

            readings = {
                "PM2.5": data["pm2_5"],
                "PM10": data["pm10"],
                "NO2": data["nitrogen_dioxide"],
                "SO2": data["sulphur_dioxide"],
                "O3": data["ozone"]
            }

            print("Air Quality:", readings)

            return aiocoap.Message(
                code=aiocoap.CONTENT,
                payload=json.dumps(readings).encode()
            )
        except Exception as e:
            return aiocoap.Message(
                code=aiocoap.INTERNAL_SERVER_ERROR,
                payload=str(e).encode()
            )

async def main():
    site = resource.Site()
    site.add_resource(["air"], AirQuality())

    await aiocoap.Context.create_server_context(
        site, bind=("127.0.0.1", 5683)
    )

    print("CoAP Server Running...")
    await asyncio.get_running_loop().create_future()

asyncio.run(main())
