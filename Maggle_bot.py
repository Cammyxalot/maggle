
import discord
from discord.ext import commands
import youtube_dl


client = commands.Bot(command_prefix = '!',description = "Bot Wanned")
# token = myTokenHere
TOKEN = ''

@client.event
async def on_ready():
    print("Bot is online beep boop")

@client.command(pass_context=True)
async def join(ctx):
    if (ctx.author.voice):
        voice_channel = ctx.message.author.voice.channel
        await voice_channel.connect()
    else:
        await ctx.send("T'es même pas dans un channel gros wanned")

@client.command(pass_contect=True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Bye Bye la miff'")
    else:
        await ctx.send("C'est pas un channel connard")

@client.command(pass_context=True)

async def play(ctx,url):
    if (ctx.voice_client):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options':'-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        player = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
            player.play(source)

@client.command(pass_context=True)
async def pause(ctx):
    await ctx.voice_client.pause()
    await ctx.send("J'fais une pause le sang!") 

@client.command(pass_context=True)
async def resume(ctx):
    await ctx.voice_client.resume()
    await ctx.send("Et zé reparti!")
    

client.run(TOKEN)