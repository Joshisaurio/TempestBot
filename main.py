import os
import brawlstars as bs
import requests
from dotenv import load_dotenv
import discord
from discord import app_commands
import time

import info
import tools

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

###################
### BRAWL STARS ###
###################
bsclient = bs.Client(brawl_key)

def get_profile_string(player_id):
    print(f"Getting player {player_id}...")
    if player_id[0] != "#":
        player_id = f"#{player_id}"

    player = bsclient.get_player(player_id)

    output = f"{player.name}: {player.trophies} trophies, {player.team_victories} team victories"

    return output

def get_profile(player_id):
    print(f"Getting player {player_id}...")
    if player_id[0] != "#":
        player_id = f"#{player_id}"

    player = bsclient.get_player(player_id)

    return player


# Fetch player info
player = bsclient.get_player("#PL0V929GC")

#print(player)
#print(f"{player.name}: {player.trophies} trophies, {player.team_victories} team victories")


## NOTES:
for property, value in vars(player).items():
    print(property, ":", value)


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
    profile = get_profile(player_id)

    print(profile.name_color)

    color_value = int(profile.name_color,16)
    rgb = color_value & 0xFFFFFF  # Mask out the alpha (keep only RGB)
    hex_profile_color = f'#{rgb:06x}'  # Format as 6-digit hex

    fancy_player_id = player_id
    if player_id[0] != "#":
        fancy_player_id = f"#{player_id}"

    embedVar = discord.Embed(title=f"{profile.name}'s profile", description=fancy_player_id, color=discord.Colour.from_str(hex_profile_color))
    embedVar.add_field(name="Trophies", value="hi", inline=False)
    embedVar.add_field(name="Field2", value="hi2", inline=False)

    await interaction.response.send_message(embed=embedVar)


client.run(discord_token)