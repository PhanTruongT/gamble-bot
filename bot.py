import os
from twitchio.ext import commands
import asyncio


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            irc_token=os.environ["TOKEN"],
            client_id=os.environ["CLIENT_ID"],
            nick=os.environ["NICK"],
            prefix=os.environ["PREFIX"],
            initial_channels=[os.environ["INIT_CHANNEL"]],
        )

    async def event_ready(self):
        loop = asyncio.get_event_loop()
        task = loop.create_task(self.gamble(5))
        await task

    async def gamble(self, i):
        for i in range(i):
            await bot._ws.send_privmsg(os.environ["INIT_CHANNEL"], "!gamble 100")
            await asyncio.sleep(2)


if __name__ == "__main__":
    bot = Bot()
    bot.run()
