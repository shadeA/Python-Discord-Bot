import asyncio
import youtube_dl
import discord
import logging
import livestreamer
from errors import *

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


async def play_audio(message, bot):
    _send = await bot.send_message()
    url = None
    custom_name = None
    message = message.split()
    try:
        url = message[0]
        custom_name = message[1]
    except IndexError:
        log.info("User did not supply a custom name")





    if 'youtube' in message:
        bot.player = await bot.voice.create_ytdl_player(message)
        bot.player.start()
        bot.current = bot.player.title
        await _send(bot.message.channel, "{userName} started playing {songName}".format(userName=bot.message.author.name, songName=bot.current))
            # I send client.current rather then client.player.title for consistency. Oddly enough, I never really learned if this is good or bad. Just seems right. Hopefully it is.
        return

    if bot.current is not None: #If a previous song has been played
        bot.previous = bot.current #Replace old previous song with the current song to prepare for the next song

    if bot.player is not None and bot.player.is_playing():
        bot.player.stop()
        logging.info('Stopped {} from playing'.format(bot.current))