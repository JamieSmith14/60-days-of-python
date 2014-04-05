identities = {
    "example": {
        "nickname": "examplebot",
        "realname": "I'm a bot",
        "username": "examplebot",
        "nickserv_pw": None
    },
    "maxbot": {
        "nickname": "maxbot",
        "realname": "anonymous",
        "username": "the game",
        "nickserv_pw": None
    },
}
networks = {
    "Freenode": {
        "server": "irc.freenode.net",
        "port": 6667,
        "ssl": False,
        "password": None,
        "identity": identities["maxbot"],
        "channels": (
            "#z1",
            "#z2",
        )
    },
    "OFTC": {
        "server": "irc.oftc.net",
        "port": 6667,
        "ssl": False,
        "password": None,
        "identity": identities["maxbot"],
        "channels": (
            "#z1",
            "#z2",
        )
    },
#     "Rizon": {
#         "server": "irc.rizon.net",
#         "port": 6667,
#         "ssl": False,
#         "identity": identities["example"],
#         "channels": (
#             "#z1",
#             "#z2",
#         )
#     },
#     "Quakenet": {
#         "server": "irc.quakenet.org",
#         "port": 6667,
#         "ssl": False,
#         "identity": identities["example"],
#         "channels": (
#             "#z1",
#             "#z2",
#         )
#     }
}