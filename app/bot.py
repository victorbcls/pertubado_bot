import asyncio
import datetime
import time
import discord
from discord.ext import commands, tasks
import os
import traceback
import read
import config



# Bot configuration
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
# Event handler for bot ready
@bot.event
async def on_ready():
    print(f"{bot.user} is connected to Discord!")
    routine_audio.start()

# Function to play audio in a voice channel
async def play_audio(voice_channel, path):
    try:
        voice_client = await voice_channel.connect()
        time.sleep(0.5)
        audio_source = discord.FFmpegPCMAudio(path)
        voice_client.play(audio_source)

        while voice_client.is_playing():
            await asyncio.sleep(1)
        await voice_client.disconnect()
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to play the daily audio
async def daily():
    try:
        channel_id = 123456789  # Replace with the ID of the voice channel
        voice_channel = bot.get_channel(channel_id)
        await play_audio(voice_channel, "./mp3/daily.mp3")

    except Exception as e:
        print(f"An error occurred: {e}")




# Plays audio when user registered with a joke in config.py enter a allowed channel in config.py
@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        print(f"{member} joined channel {member.voice.channel}")
        joke = config.jokes.get(str(member), None)
        if joke and str(member.voice.channel) in config.allowed_channels:
            path = f"./mp3/{joke}"
            await play_audio(member.voice.channel, path)



# Background task to play audio at a specific time
@tasks.loop(minutes=1)
async def routine_audio():
    now = datetime.datetime.utcnow()
    if now.hour == 13 and now.minute == 0:
        await daily()


# Command to make the bot play audio with command !play, !toque
@bot.command(aliases=["toque"])
async def play(ctx):
    try:
        channel = ctx.author.voice.channel
        audio = ctx.message.content.replace("!play", "").replace(".mp3",'').strip()
        should_play = bool(audio.strip())
        print(should_play)

        if should_play:
            audio_path = f'./mp3/{audio}.mp3'
            print(audio_path)
            if os.path.isfile(audio_path):
                await play_audio(channel,audio_path)
        else:
            await ctx.send("Cannot paly this.")

    except Exception as e:
        traceback.print_exc()
        print("An error occurred.")

# Command to make the bot speak text with command !talk, !fala, !habla
@bot.command(aliases=["fala", "habla" ])
async def talk(ctx):
    try:
        channel = ctx.author.voice.channel
        message = ctx.message.content.replace("!fala", "").replace("!habla", "").replace("!talk", "")
        should_talk = bool(message.strip())

        if should_talk:
            await channel.connect()
            filename = read.readAndSave(message)  # You need to define this function
            guild = ctx.guild
            voice_client = discord.utils.get(bot.voice_clients, guild=guild)
            audio_source = discord.FFmpegPCMAudio(filename)
            voice_client.play(audio_source, after=lambda _: asyncio.run_coroutine_threadsafe(disconnect_and_clear(voice_client), loop=voice_client.loop).result())
        else:
            await ctx.send("Cannot speak this.")

    except Exception as e:
        await disconnect_and_clear(voice_client)
        traceback.print_exc()
        print("An error occurred.")

# Function to disconnect from the voice channel and clear audio files genretade by text
async def disconnect_and_clear(voice_client):
    await voice_client.disconnect()
    dir = './habla'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

# Replace 'TOKEN' with your bot token
bot.run(TOKEN)
