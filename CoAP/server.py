import asyncio
import random
import aiocoap.resource as resource
import aiocoap

class TemperatureResource(resource.Resource):
    def generate_temperature(self):
        temp = random.uniform(1, 40)
        print(temp)
        return temp

    async def render_get(self, request):
        temp = self.generate_temperature()
        return aiocoap.Message(payload=f"{temp}".encode())

async def main():
    root = resource.Site()
    root.add_resource(['temperature'], TemperatureResource())
    await aiocoap.Context.create_server_context(root, bind=('localhost', 5683))

    # Run forever
    await asyncio.get_running_loop().create_future()


if __name__ == "__main__":
    asyncio.run(main())