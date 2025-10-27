import asyncio
from db.create_tables import create_tables
from bot import CBot
from utils.settings import SODO_ID, API_ID, API_HASH


async def main():
    print("#-# " * 5, "Create Databae or Connect them", "#-# " * 5)
    create_tables(SODO_ID)
    print("#-# " * 5, "Start bot", "#-# " * 5)
    app = CBot("crawler", api_id=API_ID, api_hash=API_HASH)
    await app.start()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()


