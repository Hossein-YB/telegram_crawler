from decouple import config

SODO_ID = config("SODO_ID", cast=int)
API_ID = config("API_ID", cast=int)
API_HASH = config("API_HASH")

