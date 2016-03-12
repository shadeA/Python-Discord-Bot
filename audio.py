import asyncio
import youtube_dl
import discord
import logging
import livestreamer
from errors import *
from CustomName import find_song, save_song
from tokenObj import check

log = logging.getLogger('audio')
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(filename)s:%(lineno)d:%(content)s")



async def play_audio(content, bot):
    
    try:
        await check(bot.message.author)
    except ValueError:
        log.e("ValueError")


#     if 'youtube' not in content:

#         content = content.split()
#         url = await find_song(content[0])
#         if url is None:
#             return
#         await play(url, bot)
#         return
#         #await bot.send_message(bot.message.author, audio_error.format(user=bot.message.author.name, problem=audio_errorText_URL))


#     elif 'youtube' in content:

#         content = content.split()
#         try:
#             url = content[0]
#             name = content[1]
#             await save_song(url, name)
#         except IndexError:
#             log.info('{user} did not pass a custom name'.format(user=bot.message.author.name))
            
#         await play(url, bot)
#         return

# async def play(url, bot):

#     bot.player = await bot.voice.create_ytdl_player(url)
#     bot.player.start()
#     if bot.current is not None:
#         bot.previous = bot.current

#     bot.current = bot.player.title
#     await bot.send_message(bot.message.channel, "{userName} started playing {songName}".format(userName=bot.message.author.name, songName=bot.current))
#     