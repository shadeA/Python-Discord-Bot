error_master = "{user}, there was an error handling your command,\n"
"make sure you include {problem} and the"
" correct spelling/formatting.\n"
"An example for csgo updates is: \n"
"       .steam -id 730 -mode update\n"
"Remember, you need use the game/user ID rather than the game/user name.\n"
"A full list of game IDs can be found at:\n"
"       https://steamdb.info/search/"

error_unknown = "{user}, an unknown error has occured.\n {debug}" #Debug is an optional option that gets triggered if the user has enabled debug mode with .debug true. I have yet to implement this feature


errorText_Options = "the required options"
errorText_ID = "the correct game/user ID"
errorText_Param = "all of the needed parameters"


helpText = "{user}, the commands/options are as follow:\n"
"       -id is a required parameter that precedes the game or user id you are going to be using\n"
"       -mode is a required parameter that precedes the action that you will be doing. Allowed actions are:\n"
"               update: Gets reecent updatees/news for the game that corresponds to the game ID passeed with -id"
"               user: Gets information about the user that matches the passed Steam64 ID through -id"