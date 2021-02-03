# S3 to MongoDB

A simple Python script to get json file from s3 bucket and write the data into MongoDB.

## Setup Python Dependencies

### Enable virtual environment

#### Installation

`python3 -m pip install --user virtualenv`

Navigate to the utility directory and run

`python3 -m venv venv`

#### Activation

The following command activates the virtual environment

`. venv/bin/activate`

### Install Utility Dependencies

`python setup.py install`

## Running the Utility

Define the s3 connection properties and file names in `s3.ini` and Mongo properties in `mongo.ini` then run the below command

`./app.py`