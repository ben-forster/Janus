import revolt
import asyncio

class Client(revolt.Client):
    async def on_message(self, message: revolt.Message):
        if message.content == "hello":
            await message.channel.send("hi how are you")

async def main():
    async with revolt.utils.client_session() as session:
        client = Client(session, "BOT TOKEN HERE")
        await client.start()

asyncio.run(main())
