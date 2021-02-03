from s3_reader import S3Reader
from mongo_writer import MongoWriter

if __name__ == "__main__":
    print("running main")
    s3_reader = S3Reader()
    json_content = s3_reader.read_s3_files()
    mongo = MongoWriter()
    mongo.write_to_mongo(json_content)
