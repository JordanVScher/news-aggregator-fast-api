from pymongo import MongoClient
from app.config.parameters import MONGO_URI, MONGO_DB_NAME
from functools import lru_cache


class MongoClientSingleton:
    def __init__(self):
        self.uri = MONGO_URI
        self.db_name = MONGO_DB_NAME
        self.sync_client = None

    @staticmethod
    @lru_cache(maxsize=1)
    def get_instance():
        """
        Returns a singleton instance of the MongoClientSingleton
        """
        return MongoClientSingleton()

    def get_sync_client(self):
        """
        Returns a synchronous MongoDB Client
        """
        if not self.sync_client:
            self.sync_client = MongoClient(self.uri, 27017)
        return self.sync_client

    def get_sync_db(self):
        """
        Returns a synchronous database instance
        """
        return self.get_sync_client()[self.db_name]


def get_mongo_client():
    return MongoClientSingleton.get_instance()
