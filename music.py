import discord
from discord.ext import commands
import yt_dlp
import asyncio
from collections import deque
from utils import get_ffmpeg

ytdl_opts = {
    'format': 'bestaudio',
    'noplaylist': True,
    'quiet': True
}

ffmpeg_opts = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}

ytdl = yt_dlp.YoutubeDL(ytdl_opts)

class MusicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.players = {}

    async def get_source(self, url, loop):
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))
        return discord.FFmpegPCMAudio(data['url'], **ffmpeg_opts), data['title']

    @commands.command()
    async def play(self, ctx, *, url):
        """Toca uma música do YouTube."""
        if not ctx.author.voice:
            await ctx.send("Entre num canal de voz primeiro.")
            return

        vc = ctx.voice_client or await ctx.author.voice.channel.connect()

        source, title = await self.get_source(url, ctx.bot.loop)
        vc.play(source, after=lambda e: print(f"Erro: {e}") if e else None)
        await ctx.send(f"Tocando: **{title}**")

    @commands.command()
    async def stop(self, ctx):
        """Para e sai do canal."""
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send("Sai do canal.")
