import json
import boto3
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client('ses')
emails = os.environ['EMAIL_LIST'].split(',')


def lambda_handler(event, context):
    object_url = process(event)
    response = send_email(object_url)
    return {
        'status': 200,
        'body': json.dumps(response)
    }


def process(event):
    # print(json.dumps(event, indent=4))
    object_key = event['Records'][0]['s3']['object']['key']
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_url = 'https://' + bucket_name + '.s3.amazonaws.com/' + object_key
    print(object_key)
    print(bucket_name)
    print(object_url)
    return object_url


def send_email(object_url):
    body = 'Object URL: <a class="ulink" href="' + object_url + '" target="_blank">New Object URL</a>.'
    email_list = emails
    logger.info(email_list)
    response = client.send_email(
        Destination={
            'ToAddresses': email_list,
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': 'UTF-8',
                    'Data': body,
                },
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': object_url,
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': 'New Object Creation Notification',
            },
        },
        Source='shafkat.waheed@gmail.com'
    )
    logger.info(response)
    return response


# lambda_handler()
