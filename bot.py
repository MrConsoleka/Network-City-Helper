import asyncio
from source import setup

if __name__ == "__main__":
    try:

        asyncio.run(setup())

    except (KeyboardInterrupt, SystemExit):
        pass


