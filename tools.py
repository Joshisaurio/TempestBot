import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')
app_id=os.getenv('APP_ID')

def create_command(name:str, description:str, options:list):
    TOKEN = discord_token
    APPLICATION_ID = app_id

    command_data = {
        "name": name,
        "description": description,
        "options": options
    }

    url = f"https://discord.com/api/v10/applications/{APPLICATION_ID}/commands"

    headers = {
        "Authorization": f"Bot {TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data=json.dumps(command_data))

    if response.status_code == 201 or response.status_code == 200:
        print(f"Command /{name} registered successfully!")
        print(response.json())
    else:
        print(f"Failed to register command: {response.status_code}")
        print(response.text)