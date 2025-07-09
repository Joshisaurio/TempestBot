tempest_clubs = ["#PL0V929GC", "#JLQ888Q0", "#80L8YUY02"]
club_names = {"PL0V929GC":"Main", "#JLQ888Q0":"Apprentice", "#80L8YUY02":"Elite"}

commands = [
    {# Hello command
    "name":"hello",
    "description":"Hello, world! (This is a test)",
    "options":[]
    },
    {# Profile command
    "name":"profile",
    "description":"Check a player's profile.",
    "options":[
        { # Profile - Parameter 1
        "type": 3,
         "name": "player_id",
         "description": "ID of the player's profile",
         "required": True}
    ]
    }
]