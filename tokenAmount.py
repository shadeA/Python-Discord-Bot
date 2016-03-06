import json
import logging
# import asyncio

log = logging.getLogger('core')
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(filename)s:%(lineno)d:%(message)s")



async def check(user):
    """
    A function that checks the tokens.json for the settings of a user
    """
    try:
        with open('token.json', 'x') as file:
            pass
    except FileExistsError:
        pass

    with open('./json/token.json', 'r') as file: # Make sure that we have the up to date token file
        try:
            jsonObj = json.load(file)
        except json.decoder.JSONDecodeError:
            jsonObj = {}

    # userAmount = jsonObj['daxter249'][0]['amount'] #This is 0
    amount = None
    flags  = None
    try:
        amount = jsonObj[user.name.lower()][0]['amount'] #This is a int
        flags  = jsonObj[user.name.lower()][1]['flags'] #This is a list
    except KeyError:
        'here'
    except Exception as e: # Unknown Error
        log.error(e)
