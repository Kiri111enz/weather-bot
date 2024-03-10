import logging
import asyncio
from bot import start as start_bot


def main() -> None:
    while True:
        try:
            asyncio.run(start_bot())
        except Exception as e:
            logging.error(e)


if __name__ == '__main__':
    main()
