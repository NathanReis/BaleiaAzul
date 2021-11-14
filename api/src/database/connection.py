from dotenv import load_dotenv
from pymongo import MongoClient
from os import getenv, path

load_dotenv(
    path.join(
        path.dirname(path.realpath(__file__)),
        '..',
        '..',
        '.env'
    )
)


class DBConnection:
    __instance = None

    def __new__(cls):
        if cls.__instance == None:
            DB_URL = getenv('DB_URL')

            cls.__instance = MongoClient(DB_URL)

        return cls.__instance
