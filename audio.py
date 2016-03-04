import asyncio
import youtube_dl
import discord
import logging
import livestreamer

logging.basicConfig(level=logging.INFO)

async def play_audio(message, bot):
    _send = bot.send_message()

    if bot.player is not None and bot.player.is_playing():
        bot.player.stop()
        logging.info('Stopped {} from playing'.format(bot.current))

    if bot.current is not None: #If a previous song has been played
        bot.previous = bot.current #Replace old previous song with the current song to prepare for the next song

    if 'youtube' in message:
        message = message.split()
        try:
            url = message[0]
            name = message[1]
        except IndexError:
            _send(bot.message.author, audio_error)

        bot.player = await bot.voice.create_ytdl_player(message)
        bot.player.start()
        bot.current = bot.player.title
        await bot.send_message(bot.message.channel, "{userName} started playing {songName}".format(userName=bot.message.author.name, songName=bot.current))
            # I send client.current rather then client.player.title for consistency. Oddly enough, I never really learned if this is good or bad. Just seems right. Hopefully it is.
        return


