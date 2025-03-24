import utility

import os

import boto3
from botocore.exceptions import ClientError

logger = utility.get_logger()

RETRY_THRESHOLD = 3


def upload_file(file_name, bucket_name, access_key, secret_key, object_name=None, s3_client=None, retry=0):
    if object_name is None:
        object_name = os.path.basename(file_name)

    if s3_client is None:
        s3_client = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
    except ClientError as e:
        logger.error(e)
        if retry < RETRY_THRESHOLD:
            retry += retry
            upload_file(file_name, bucket_name, access_key, secret_key, object_name, s3_client, retry)
        else:
            logger.error(e)
            raise e

    logger.info('s3 file upload successful: %s', file_name)
    return True


def download_file(downloaded_file_name, object_name, bucket_name, access_key, secret_key):
    try:
        s3_client = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
        with open(downloaded_file_name, 'wb') as f:
            s3_client.download_fileobj(bucket_name, object_name, f)
    except ClientError as e:
        logger.error(e)
        return e

    logger.info('s3 file download successful: %s', downloaded_file_name)
    return True

