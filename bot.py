import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix="!", intents=intents)

target_channel_id = 1386814435758313702 

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_raw_reaction_add(payload):
    if str(payload.emoji) == "🎵":
        guild = bot.get_guild(payload.guild_id)
        channel = guild.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        
        if "http" in message.content:
            target_channel = guild.get_channel(target_channel_id)
            await target_channel.send(f"🎵 **Link marked by <@{payload.user_id}>:**\n{message.content}")

bot.run(os.getenv("TOKEN"))
