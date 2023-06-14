#!/usr/bin/python3

import discord
from discord.ext import commands
import os

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')

#BOT EXTENSION DOCS (commands.Bot):
# https://discordpy.readthedocs.io/en/stable/ext/commands/index.html
#BOT inherets Client attributes/methods as well:
# https://discordpy.readthedocs.io/en/stable/api.html?highlight=message#client
#DOCS ON EVENTS:
# https://discordpy.readthedocs.io/en/stable/api.html?highlight=message#discord-api-events
#DOCS ON DISCORD MODELS (MESSAGE, EMOJI, etc)
# https://discordpy.readthedocs.io/en/stable/api.html#discord-models



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)

@bot.command()
async def test(ctx, *args):
    print("lel")
    if bot.user == ctx.author:
        await ctx.send("lol")
        return
    message = " ".join(args)
    await ctx.send(message)

@bot.event
async def on_message(message):
    if bot.user == message.author:
        return
    await message.add_reaction('<:calculon:1118489374733123614>')
    #for emoji in message.guild.emojis:
        #print(emoji)
        #await message.add_reaction('<:pepe:1118472044078706689>')
    #print(bot.get_emoji(1118472044078706689))

    await bot.process_commands(message)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_reaction_add(reaction, user):
    if user == bot.user:
        return
    await reaction.message.add_reaction('<:pepe:1118472044078706689>')

bot.run(TOKEN)