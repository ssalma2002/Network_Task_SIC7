
import asyncio
import aiocoap.resource as resource
import aiocoap.resource as resource
import aiocoap
async def main():
    protocol = await aiocoap.Context.create_client_context()
    msg = aiocoap.Message(code=aiocoap.GET, uri="coap://localhost/temperature")
    response = await protocol.request(msg).response
    print(response)
    print(f"Payload (decoded): {response.payload.decode()} °C")

if __name__ == "__main__":
    asyncio.run(main())