import requests
import os
import urllib.parse
from dotenv import load_dotenv

import data

load_dotenv()

brawl_key = os.getenv('BRAWL_KEY')

def get_player(tag):
    if tag[0] != "#":
        encoded_tag = "%23" + tag
    else:
        encoded_tag = urllib.parse.quote(tag)
    print(encoded_tag)
    url = f"https://api.brawlstars.com/v1/players/{encoded_tag}"
    headers = {
        "Authorization": "Bearer " + brawl_key
    }

    r = requests.get(url, headers=headers)
    print(r.json())
    return r.json()

def get_user(discord_id:str):
    return get_player(data[discord_id])

get_player("PLOV929GC")