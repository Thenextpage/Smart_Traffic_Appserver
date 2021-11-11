import sys
import boto3
import base64
s3 = boto3.client('s3')


def lambda_handler(event, context):
    name = str(event['name'])
    try:
        share_url = s3.generate_presigned_url("get_object", ExpiresIn=3600, Params={"Bucket": 'imagetrafficbucket', "Key": name, })
    except Exception as e:
        return e
    return {"url":share_url}
