import asyncio
import youtube_dl
import discord
import logging
import livestreamer
from errors import *
from CustomName import find_song, save_song
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


async def play_audio(message, bot):


    message = message.split()

    if 'youtube' not in message or 'twitch' not in message:
        try:
            url = await find_song(message)
        except Exception as e:
            log.error(e)
            await bot.send_message(bot.message.author, audio_error.format(user=bot.message.author.name, problem=audio_errorText_URL))


    elif 'youtube' in message or 'twitch' in message:

        try:
            url = message[0]
            name = message[1]
            song.save_song(url, name)
        except:
            log.info('{user} did not pass a custom name'.format(bot.message.author.name))

        bot.player = await bot.voice.create_ytdl_player(url)
        bot.player.start()
        if bot.current is not None:
            bot.previous = bot.current

        bot.current = bot.player.title
        await bot.send_message(bot.message.channel, "{userName} started playing {songName}".format(userName=bot.message.author.name, songName=bot.current))




    