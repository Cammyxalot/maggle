
import discord
from discord.ext import commands
import youtube_dl
import asyncio


client = commands.Bot(command_prefix = '!',description = "Bot Wanned")
# token = myTokenHere OTc4MjI4ODQ1NjcwOTY5MzQ0.GAqrSu.M-1CUYSlInwl7OTNNbI02VP_vK_iqghb35GeBE
TOKEN = 'OTc4MjI4ODQ1NjcwOTY5MzQ0.GAqrSu.M-1CUYSlInwl7OTNNbI02VP_vK_iqghb35GeBE'
queue = []
@client.event
async def on_ready():
    print("Bot is online beep boop")

@client.command(pass_context=True)
async def join(ctx):
    predefUrl = 'https://www.youtube.com/watch?v=Qu84tcGExSQ'
    if (ctx.author.voice):
        voice_channel = ctx.message.author.voice.channel
        await voice_channel.connect()
        player = ctx.voice_client
        FFMPEG_OPTIONS = {
                'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                'options':'-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(predefUrl, download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
                player.play(source)

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
async def pause(ctx):
    ctx.voice_client.pause()
    await ctx.send("J'fais une pause le sang!") 

@client.command(pass_context=True)
async def resume(ctx):
    ctx.voice_client.resume()
    await ctx.send("Et zé reparti!")

@client.command(pass_context=True)
async def play(ctx,url):
    try:
        player = ctx.voice_client
        if (player):
            player.stop()
            FFMPEG_OPTIONS = {
                'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                'options':'-vn'}
            YDL_OPTIONS = {'format':"bestaudio"}

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
                queue.append(player)
                player.play(source)
    except:
        await ctx.send("Je peut pas lire ça le sang")
 
client.run(TOKEN)