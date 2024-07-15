
from pymongo import MongoClient # type: ignore
from pymongo.error import ConnectionFailure # type: ignore

from config import Settings


class MongoDatabaseConnector:

    """
        singleton class to connect to MongoDB database.
    """
