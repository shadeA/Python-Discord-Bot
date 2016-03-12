import json
import logging
import requests
import datetime
# import asyncio
now = datetime.date.today()


log = logging.getLogger('core')
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(filename)s:%(lineno)d:%(message)s")



async def check(user):
    """
    A function that checks the tokens.json for the settings of a user
    """
    jsonObj = None

    try:
        with open('token.json', 'x') as file:
            pass
    except FileExistsError:
        pass


    with open('token.json', 'r') as file: # Make sure that we have the up to date token file
        try:
            jsonObj = json.load(file)
        except json.decoder.JSONDecodeError:
            jsonObj = {}

    # userAmount = jsonObj['daxter249'][0]['amount'] #This is 0
    amount = None
    flags  = None
    name = user.name.lower()
    try:
        amount = jsonObj[name][0]['amount'] #This is a int
        flags = jsonObj[name][1]['flags'] #This is a list
        time = jsonObj[name][2]['time']
        base_amount = jsonObj[name][3]['base_amount']
    except KeyError:
        #This means there is not a user by this name
        jsonObj[name] = [{"amount" : 3}, {"flags" : []}, {"time" : ""}, {"base_amount" : "3"}]
        jsonObj[name][2]['time'] = now.day

        with open('token.json', 'w') as file:
            json.dump(jsonObj, file, indent=4, separators=(',', ': '), sort_keys=True)

        amount = jsonObj[name][0]['amount']
        flags = jsonObj[name][1]['flags']
        time = jsonObj[name][2]['time']
        base_amount = jsonObj[name][3]['base_amount']
        
    except Exception as e: # Unknown Error
        log.error(e)

    if amount <= 0:
        #User does not have enough token to play, checek if its time to reset their amount.
        if jsonObj[name][2]['time'] != now.day:
            amount = base_amount
            with open('token.json', 'w') as file:
                json.dump(jsonObj, file, indent=4, separators=(',', ': '), sort_keys=True)
            jsonObj[name][0]['amount'] = jsonObj[name][0]['amount'] - 1 #Because they played a song
            return 'They have enough tokens'
        else:
            raise ValueError
    else:
        if jsonObj[name][2]['time'] != now.day:
            log.info("Reset token amounto to base amount for the user")
            amount = base_amount
            with open('token.json', 'w') as file:
                json.dump(jsonObj, file, indent=4, separators=(',', ': '), sort_keys=True)
            jsonObj[name][0]['amount'] = jsonObj[name][0]['amount'] - 1 #Because they played a song
            return 'They have enough tokens'
        else:
            # amount = amount - 1
            jsonObj[name][0]['amount'] = jsonObj[name][0]['amount'] - 1
            log.info('Took away a token')
            with open('token.json', 'w') as file:
                json.dump(jsonObj, file, indent=4, separators=(',', ': '), sort_keys=True)
            return

async def script_token(data):
    try:
        with open('token.json', 'x') as file:
            pass
    except FileExistsError:
        pass


    with open('token.json', 'r') as file: # Make sure that we have the up to date token file
        try:
            jsonObj = json.load(file)
        except json.decoder.JSONDecodeError:
            jsonObj = {}

    if 'os' in data:
        log.info('NOPE NOPE NOPE NOPE')
    eval(data)
    return

