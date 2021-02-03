from pymongo import MongoClient
import urllib.parse
from mongo_properties import MongoProperties
import logging

logger = logging.getLogger("s3_to_mongo")

# Create handlers
file_hdlr = logging.FileHandler("/tmp/s3_to_mongo.log")
console_hdlr = logging.StreamHandler()

# Set logging format
formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(message)s"
)
file_hdlr.setFormatter(formatter)

# Add handleres to logger
logger.addHandler(file_hdlr)

# Set log level
logger.setLevel(logging.INFO)


class MongoWriter:

    def write_to_mongo(self, documents) -> None:
        mongo_properties = MongoProperties.read_mongo_properties()
        logger.info("Mongo properties %s", str(mongo_properties))
        username = urllib.parse.quote_plus(mongo_properties.username)
        password = urllib.parse.quote_plus(mongo_properties.password)
        client = MongoClient(mongo_properties.host,
                             username=username, password=password)
        db = client[mongo_properties.database]
        collection = db[mongo_properties.collection]
        if isinstance(documents, list):
            collection.insert_many(documents)
        else:
            collection.insert_one(documents)
