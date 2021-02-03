import configparser

from util import masker


class MongoProperties:
    host: str
    username: str
    password: str
    database: str
    collection: str

    def __init__(
            self, host, username, password, database, collection
    ):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.collection = collection

    @staticmethod
    def read_mongo_properties():
        config = configparser.RawConfigParser()
        config.read("mongo.ini")
        properties = dict(config.items("MONGO_PROPERTIES"))
        mongo_properties = MongoProperties(
            properties["host"],
            properties["username"],
            properties["password"],
            properties["database"],
            properties["collection"],
        )
        return mongo_properties

    def __str__(self):
        return masker(self.host) + " " + masker(self.username) + " " + masker(
            self.password) + " " + self.database + " " + self.collection
