import logging
import asyncio
from bot import start as start_bot
from env import config


def main() -> None:
    while True:
        try:
            asyncio.run(start_bot(config.BOT_TOKEN))
        except Exception as e:
            logging.error(e)


if __name__ == '__main__':
    main()
