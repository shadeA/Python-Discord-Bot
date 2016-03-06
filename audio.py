import asyncio
import youtube_dl
import discord
import logging
import livestreamer
from errors import *
from CustomName import find_song, save_song
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(filename)s:%(lineno)d:%(message)s")
log = logging.getLogger(__name__)


async def play_audio(message, bot):

    if 'youtube' not in message:

        message = message.split()
        url = await find_song(message[0])
        if url is None:
            return
        await play(url, bot)
        return
        #await bot.send_message(bot.message.author, audio_error.format(user=bot.message.author.name, problem=audio_errorText_URL))


    elif 'youtube' in message:

        message = message.split()
        try:
            url = message[0]
            name = message[1]
            await save_song(url, name)
        except IndexError:
            log.info('{user} did not pass a custom name'.format(user=bot.message.author.name))
            
        await play(url, bot)
        return

async def play(url, bot):

    bot.player = await bot.voice.create_ytdl_player(url)
    bot.player.start()
    if bot.current is not None:
        bot.previous = bot.current

    bot.current = bot.player.title
    await bot.send_message(bot.message.channel, "{userName} started playing {songName}".format(userName=bot.message.author.name, songName=bot.current))
    