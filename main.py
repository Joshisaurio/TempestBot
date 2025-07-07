import os
import brawlstars as bs
import requests
from dotenv import load_dotenv
import discord
from discord import app_commands

import info
import tools

load_dotenv()


discord_token = os.getenv('DISCORD_TOKEN')
brawl_key = os.getenv('BRAWL_KEY')

client = bs.Client(brawl_key)

# Fetch player info
player = client.get_player("#PL0V929GC")

print(player)
print(f"{player.name}: {player.trophies} trophies, {player.team_victories} team victories")

"""
## NOTES:
for property, value in vars(player).items():
    print(property, ":", value)
"""