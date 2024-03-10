from collections import namedtuple
from dotenv import dotenv_values

Config = namedtuple('Config', [
    'BOT_TOKEN'
])

config = Config(**dotenv_values('.env'))
