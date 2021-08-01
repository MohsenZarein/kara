from pymongo import MongoClient
from django.conf import settings


def get_db_client():
    """ instanciate a mongo client and return it """
    client = MongoClient(
        host=settings.MONGO_HOST,
        port=settings.MONGO_PORT,
        username=settings.MONGO_USERNAME,
        password=settings.MONGO_PASSWORD
    )

    return client