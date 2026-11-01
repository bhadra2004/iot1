
import asyncio
import json
import aiocoap

async def get_air():
    protocol = await aiocoap.Context.create_client_context()

    request = aiocoap.Message(
        code=aiocoap.GET,
        uri="coap://127.0.0.1:5683/air"
    )

    response = await protocol.request(request).response

    if not response.code.is_successful():
        raise RuntimeError(response.payload.decode())

    return json.loads(response.payload.decode())

if __name__ == "__main__":
    data = asyncio.run(get_air())
    print("Received:", data)
