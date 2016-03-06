import asyncio
import discord
import argparse
import logging
import os
from audio import play_audio
from steamWEBAPI import steam
from tokenObj import createUser


log = logging.getLogger('core')
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(filename)s:%(lineno)d:%(message)s")



parser = argparse.ArgumentParser()
parser.add_argument("username", help='The username of the Discord account you want to use')
parser.add_argument("password", help='The password of the Discord account you want to use.')
args = parser.parse_args()

clearconsole = lambda: os.system('cls')
clearconsole()

if not discord.opus.is_loaded():
    # the 'opus' library here is opus.dll on windows
    # or libopus.so on linux in the current directory
    # you should replace this with the location the
    # opus library is located in and with the proper filename.
    discord.opus.load_opus("libopus-0.dll")





class Bot(discord.Client):

    def __init__(self):
        super().__init__()
        self.message = None
        self.player = None
        self.current = None
        self.previous = None
        self.file_name = None


    async def on_message(self, message): #On a message
        #Start checking which command it was. Would like to use a switch statement but python doesnt have one.
        self.message = message


        if message.content.startswith('.join') and any(message.author.roles[x].name == 'admin' for x in range(1, 10)): #When telling the bot to join a channel
            channel_name = message.content[5:].strip() #Format the message
            check = lambda c: c.name == channel_name and c.type == discord.ChannelType.voice
            channel = discord.utils.find(check, message.server.channels)

            await self.delete_message(message)

            if self.is_voice_connected():
                await self.voice.disconnect()
                log.INFO('Disconnected from a voice channel')
                log.debug("I don't think I'm doing the whole 'logging' thing right. I'm just typing it all out in a string rather than use variables.")

            await self.join_voice_channel(channel)
            # self.starter = message.author
        elif message.content.startswith('.play') and any(message.author.roles[x].name == 'admin' for x in range(1, 10)):
            if not self.is_voice_connected():
                log.error('Not in a voice channel')
                log.debug('The user was not in a voice channel and attempted to play audio. They should get their memory checked.')
                await self.send_message(message.author, '{authorName}, type .join "channel name" before attempting to play audio.')
                return
            playItem = message.content[5:].strip()

            await self.delete_message(message)

            await play_audio(playItem, self)


        elif message.content.startswith('.stop') and any(message.author.roles[x].name == 'admin' for x in range(1, 10)):
            await self.delete_message(message)

            if self.player is not None and self.player.is_playing():
                self.player.stop()
                log.info("Stopped '{}' from playing".format(self.current))
            else:
                log.info("User attempted to stop a song while a song is not playing")

        elif message.content.startswith('.steam') and any(message.author.roles[x].name == 'admin' for x in range(1, 10)):
            data = message.content[6:].strip()
            data = data.split()

            await steam(data, self)
            await self.delete_message(message)
        elif message.content.startswith('.token') and any(message.author.roles[x].name == 'admin' for x in range(1, 10)):
            data = message.content[6:].strip()
            data = data.split()
            await createUser(data)
            await self.delete_message(message)

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')


bot = Bot()
bot.run(args.username, args.password)
