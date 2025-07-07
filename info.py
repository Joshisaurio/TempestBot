commands = [
    {# Joke command
    "name":"joke",
    "description":"I'll tell you a joke!",
    "options":[
        { # Crazycaps - Parameter 1
        "type": 5,
         "name": "crazycaps",
         "description": "Should I make the message lOok FuNkY?",
         "required": False}
    ]
    },
    {# Hello command
    "name":"hello",
    "description":"I'll greet you! (I might not be so kind sometimes...)",
    "options":[]
    },
    {# Crazycaps command
    "name":"crazycaps",
    "description":"I'll randomize capital letters in your message, to make it look fUnkY",
    "options":[
        { # Crazycaps - Parameter 1
        "type": 3,
         "name": "message",
         "description": "The message that I should make fUnKY",
         "required": True}
    ]
    }
]