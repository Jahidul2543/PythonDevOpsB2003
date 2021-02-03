import boto3
import uuid
import json
from pprint import pprint

"""
This script will have some s3 utilities using boto3

"""
client = boto3.client('s3')
random_string = str(uuid.uuid4())
bucket_name = 'my-bucket-' + random_string[:13]
print(bucket_name)


def create_bucket():
    print('create bucket')
    response = client.create_bucket(
        Bucket=bucket_name
    )
    print(response)


def process_a_dict():
    response_dict = {'ResponseMetadata': {'RequestId': '6E620E10A62A6DD8',
                                          'HostId': 'pdUTGLMwq3E3Pjss0pUfDSFHo2N+uaSBBxCKzNgC0n+QsNsBboYcQVws290WbUHSeq34mOLBVw0=',
                                          'HTTPStatusCode': 200, 'HTTPHeaders': {
            'x-amz-id-2': 'pdUTGLMwq3E3Pjss0pUfDSFHo2N+uaSBBxCKzNgC0n+QsNsBboYcQVws290WbUHSeq34mOLBVw0=',
            'x-amz-request-id': '6E620E10A62A6DD8', 'date': 'Fri, 29 Jan 2021 02:34:30 GMT',
            'location': '/my-bucket-c3d1c85f-85e9', 'content-length': '0', 'server': 'AmazonS3'}, 'RetryAttempts': 0},
                     'Location': '/my-bucket-c3d1c85f-85e9'}
    print(json.dumps(response_dict, ))


def delete_bucket():
    response = client.delete_bucket(
        Bucket='my-bucket-c3d1c85f-85e9',
    )
    pprint(response)


def main():
    # create_bucket()
    process_a_dict()
    # delete_bucket()


if __name__ == "__main__":
    main()
