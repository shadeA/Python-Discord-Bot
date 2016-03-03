import asyncio
import requests
import discord
import logging
import datetime
import json
from text import *

logging.basicConfig(level=logging.INFO)

log = logging.getLogger(__name__)

#Remember to add a '-debug' opt-in command so that the error can be directly send to the user.
#Also add either a dedicated api key or make the user submit there own. It would have to be through pm 

date = None


update_url = "http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002"
parameters = {"appid":None, "count":"2", "maxlength":"300", "format":"json"}


async def steam(data, bot):
    _send = await bot.send_message()
    if data is None: 
        log.critical("No data was passed") #This is a safety function. It is never actually going to be triggered.

    if '-help' in data:
        _send(bot.message.author, )
    data = [item.lower() for item in data] #Translate the dict to lower so that both -ID and -id work. Thanks to Eric for pointing this out not even a second after I opeened the commands


    try:
        _id = data[data.index("-id") + 1]
        _mode = data[data.index("-mode") + 1]
        # parameters["appid"] = game

    except ValueError: #if an option is not found is not found
        _send(bot.message.author, error_master.format(bot.message.author.name, errorText_Options))
    
    except IndexError: #if an option param is not found
        _send(bot.message.author, error_master.format(bot.message.author.name, errorText_Param))
        # Implemented thee new error system
    except Exception as e:
        log.error(e)
        _send(bot.message.author, error_unknown.format(bot.message.author, e)) #lets enable debugging by default


    # if mode not in {'update', 'profile', 'playtime' }: 
    response = requests.get(update_url, params=parameters)

    content = response.json()
    #Took me awhile to realize it was a multilevel dict and not the traditional 'object' format I was used to from node.js


