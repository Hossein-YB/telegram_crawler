import asyncio
from db.create_tables import create_tables
from utils.settings import SODO_ID


async def main():
    print("#-#" * 20, "Create Databae or Connect them", "#-#" * 20)
    create_tables(SODO_ID)



if __name__ == "__main__":
    asyncio.run(main())


