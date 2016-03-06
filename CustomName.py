
import asyncio
import json
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(filename)s:%(lineno)d:%(message)s")
log = logging.getLogger(__name__)



async def find_song(name):
    try:
        with open('songList.json', 'x') as file:
            pass
    except FileExistsError:
        pass

    with open('songList.json', 'r') as file: # Make sure that we have the up to date song list
        try:
            songs = json.load(file)
        except json.decoder.JSONDecodeError:
            songs = {}

    try:
        result = songs[name]
    except IndexError:
        log.info('Song not found with that name')
        return None

    return result


async def save_song(url, name):
    if url is None or name is None:
        raise ValueError("You did not pass a URL or a name")

    try:
        with open('songList.json', 'x') as file:
            pass
    except FileExistsError:
        pass

    with open('songList.json', 'r') as file:
        try:
            songs = json.load(file)
        except json.decoder.JSONDecodeError:
            songs = {}


    name = name.lower()
    songs[name] = url
    with open('songList.json', 'w') as file:
        json.dump(songs, file, indent=4, separators=(',', ': '), sort_keys=True)

    return
