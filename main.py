import commands
import recommend_logging
import discord

from dotenv import load_dotenv, find_dotenv
from os import getenv

load_dotenv(find_dotenv())


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return "Coddy Servers' bot"

    async def on_ready(self):
        """Alerts when bot is connected"""
        embed = discord.Embed()
        embed.description = "Author of this bot is [Timothy](https://github.com/Zener085)"
        await self.get_channel(int(getenv("COMMAND_CHANNEL"))).send(f"Connected. Bot is {self}.\n", embed=embed)

    async def on_message(self, message: discord.Message):
        """Answer to the messages from channels\n
            :param message the message from the channel"""

        if message.author == self.user:
            return

        if message.channel.id == int(getenv("COMMAND_CHANNEL")):
            await commands.do_command(self, message)
            return

    async def on_member_join(self, member: discord.Member):
        with open("users.txt", 'r') as file:
            check_members = file.readline().split()

        if member.display_name not in check_members:
            await member.kick(reason="Тебе нельзя присоединиться к этому каналу.")
            await self.get_channel(int(getenv("COMMAND_CHANNEL"))).send(member.display_name + " tried to join")


client = MyClient(intents=discord.Intents.all())

if __name__ == "__main__":
    client.run(getenv("TOKEN"))
