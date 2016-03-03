import asyncio
import youtube_dl
import discord
import logging

logging.basicConfig(level=logging.INFO)

async def play_audio(message, audio_type, client):
    if client.player is not None and client.player.is_playing():
        client.player.stop()
        logging.info('Stopped {} from playing'.format(client.current))

    if audio_type == 'url':
        if client.current is not None:
            client.previous = client.current

        client.player = await client.voice.create_ytdl_player(message)
        client.player.start()
        client.current = client.player.title
        await client.send_message(client.message.channel, "{userName} started playing {songName}".format(userName=client.message.author.name, songName=client.current))
            # I send client.current rather then client.player.title for consistency. Oddly enough, I never really learned if this is good or bad. Just seems right. Hopefully it is.
        return
    elif audio_type == 'file':

        if '.mp3' not in message:
            logging.error('Path passed did not contain a .mp3 extension. Due to limitations in my skills, this is nessasary. Inform the user.')
            await client.send_message(client.message.author, "{}, The song you reequested did not contain a .mp3 extension. Make sure this is in your file name.")
            return
        if client.current is not None:
            client.previous = client.current

        client.player = client.voice.create_ffmpeg_player("media/" + message)
        client.player.start()
        client.current = message.replace('.mp3', "", 1)
        await client.send_message(client.message.channel, "{userName} started playing {songName}".format(userName=client.message.author.name, songName=client.current))
        return

