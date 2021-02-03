import logging
import boto3
import json
import botocore

from s3_properties import S3Properties

logger = logging.getLogger("s3_to_mongo")

# Create handlers
file_hdlr = logging.FileHandler("/tmp/s3_to_mongo.log")
console_hdlr = logging.StreamHandler()

# Set logging format
formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(message)s"
)
file_hdlr.setFormatter(formatter)
console_hdlr.setFormatter(formatter)

# Add handleres to logger
logger.addHandler(file_hdlr)
logger.addHandler(console_hdlr)

# Set log level
logger.setLevel(logging.INFO)


class S3Reader:

    def read_s3_files(self):
        properties = S3Properties.read_s3_properties()
        logger.info("S3 properties %s", str(properties))
        s3 = boto3.client('s3', region_name=properties.region,
                          aws_access_key_id=properties.access_key,
                          aws_secret_access_key=properties.secret_key)
        # Print out bucket names
        # response = s3.list_buckets()

        try:
            content_object = s3.get_object(Bucket=properties.bucket_name, Key=properties.file_name)
            actual_content = content_object['Body'].read().decode('utf-8')
            json_content = json.loads(actual_content)
            return json_content
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                raise FileNotFoundError
