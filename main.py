import os
import brawlstars as bs
import requests
from dotenv import load_dotenv
import discord
from discord import app_commands
import time

import bsdata
import info
import tools
import bsdata as brawl

#############
### SETUP ###
#############

load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')
app_id = os.getenv('APP_ID')
brawl_key = os.getenv('BRAWL_KEY')

for i in info.commands:
    tools.create_command(i["name"], i["description"], i["options"])
    time.sleep(0.2)


###############
### DISCORD ###
###############

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(application_id=app_id,intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name="hello", description="Hello, world! (This is a test)")
async def hello_command(interaction: discord.Interaction):
    await interaction.response.send_message("Hello world")

@tree.command(name="profile", description="Check a player's profile.")
@app_commands.describe(player_id="ID of the player's profile")
async def profile_command(interaction: discord.Interaction, player_id:str):
    print("Command received")
    profile = bsdata.get_player(player_id)

    color_value = int(profile["nameColor"], 16)
    rgb = color_value & 0xFFFFFF  # Mask out the alpha (keep only RGB)
    hex_profile_color = f'#{rgb:06x}'  # Format as 6-digit hex

    embedVar = discord.Embed(title=f"{profile["name"]}'s profile", description=profile["tag"], color=discord.Colour.from_str(hex_profile_color))
    embedVar.add_field(name="Trophies",
                       value=f"Current trophies: {profile["trophies"]}\nHighest trophies: {profile["highestTrophies"]}",
                       inline=False)
    embedVar.add_field(name="Victories",
                       value=f"3v3 victories: {profile["3vs3Victories"]}\nShowdown victories: {profile["soloVictories"]+profile["duoVictories"]}",
                       inline=False)
    embedVar.add_field(name="Club:",
                       value=f"{profile["club"]["name"]} ({profile["club"]["tag"]})",
                       inline=False)

    await interaction.response.send_message(embed=embedVar)


client.run(discord_token)