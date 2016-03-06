debugText = "\n**Debug log below:**\n**{debug}**"


steam_error = """{user}, there was an error handling your command,
make sure you include {problem} and the correct spelling/formatting.
An example for csgo updates is: 
       .steam -id 730 -mode update
Remember you need use the game/user ID rather than the game/user name.
A full list of game IDs can be found at:
       https://steamdb.info/search/"""

steam_errorUnknown = "{user}, an unknown error has occured."


steam_errorText_Options = "the required options"
steam_errorText_ID = "the correct game/user ID"
steam_errorText_Param = "all of the needed parameters"


helpText = """{user}, the commands/options are as follow:
       -id is a required parameter that precedes the game or user id you are going to be using
       -mode is a required parameter that precedes the action that you will be doing. Allowed actions are:
               update: Gets reecent updatees/news for the game that corresponds to the game ID passeed with -id
               user: Gets information about the user that matches the passed Steam64 ID through -id"""


audio_error = """{user}, there was an error playing your song,
make sure that {problem}"""

audio_errorUnknown = "{user}, there was an unknown audio error."

audio_errorText_URL = """you are using either a youtube.com URL, a twitch.com URL,
 or a valid song name. Use .songlist to get a list of song names."""

