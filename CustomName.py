
import asyncio
import json

with open('songList.json', 'r') as file:
    songs = json.load(file)


async def find_song(name):

    with open('songList.json', 'r') as file: # Make sure that we have the up to date song list
        songs = json.load(file)
    try:
        result = songs[name]
    except IndexError:
        raise ValueError('Did not find a song by the passed name: {}'.format(name))
        return 'There was an Error. Next time, use try: Except:'
    return result


async def save_song(url, name):
    if url is None or name is None:
        raise ValueError("You did not pass a URL or a name")

    name = name.lower()
    songs[name] = url
    with open('songList.json', 'w') as file:
        json.dump(songs, file, indent=4, separators=(',', ': '), sort_keys=True)

    return
