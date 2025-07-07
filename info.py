commands = [
    {# Hello command
    "name":"hello",
    "description":"Hello, world! (This is a test)",
    "options":[]
    },
    {# Crazycaps command
    "name":"profile",
    "description":"Check a player's profile.",
    "options":[
        { # Crazycaps - Parameter 1
        "type": 3,
         "name": "player_id",
         "description": "ID of the player's profile",
         "required": True}
    ]
    }
]