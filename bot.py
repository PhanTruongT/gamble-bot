import os
from twitchio.ext import commands


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
        await self._ws.send_privmsg(os.environ["INIT_CHANNEL"], "!gamble 1")


if __name__ == "__main__":
    bot = Bot()
    bot.run()
