
import asyncio
import json


class song(object):
    """
    The class which handles saving, loading, 
    and storing custom song names.
    """

    def __init__(self, name):
        self.result = None
        self.songs = { 'rickroll':'urlthinghere' }
        with open('songList', 'r') as file:
            self.songs = json.load(file)

    async def find_song(self, name):
        self.result = self.songs.get(name.lower())
        if self.result is None:
            return None
        return self.result

    async def save_song(self, url, name):
        if url is None or name is None:
            raise ValueError("You did not pass a URL or a name")
            return None
        name = name.lower()
        self.songs[name] = url
        with open('songList.txt', 'r') as file:
            json.dump(self.songs, file, indent=4, separators=(',', ': '), sort_keys=True)





