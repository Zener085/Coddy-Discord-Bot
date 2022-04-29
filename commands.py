import discord
import asyncio

from dotenv import load_dotenv, find_dotenv
from os import getenv

client: discord.Client

load_dotenv(find_dotenv())


async def do_command(_client: discord.Client, message: discord.Message):
    global client
    client = _client
    match message.content:
        case "$Alert": await alert_members()
        case _: await message.channel.send("Unknown command")


async def alert_members():
    global client
    alert = ""
    members_on_channel: list[discord.Member] = client.get_channel(int(getenv("MAIN_VOICE_CHANNEL"))).members

    for user in client.users:
        if user not in members_on_channel and user != client.user:
            alert += f"{user.mention}, "

    await client.get_channel(int(getenv("GLOBAL_CHANNEL"))).send(alert[:-2] + " переходите в голосовой канал!")
