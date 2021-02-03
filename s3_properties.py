import configparser

from util import masker


class S3Properties:
    access_key: str
    secret_key: str
    region: str
    bucket_name: str
    file_name: str

    def __init__(
            self, access_key, secret_key, region, bucket_name, file_name
    ):
        self.access_key = access_key
        self.secret_key = secret_key
        self.region = region
        self.bucket_name = bucket_name
        self.file_name = file_name

    @staticmethod
    def read_s3_properties():
        config = configparser.RawConfigParser()
        config.read("s3.ini")
        properties = dict(config.items("S3_PROPERTIES"))
        s3_properties = S3Properties(
            properties["access_key"],
            properties["secret_key"],
            properties["region"],
            properties["bucket_name"],
            properties["file_name"],
        )
        return s3_properties

    def __str__(self):
        return masker(self.access_key) + " " + masker(
            self.secret_key) + " " + self.region + " " + self.bucket_name + " " + self.file_name
