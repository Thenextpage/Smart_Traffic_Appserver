import json
import boto3
import base64
from botocore.errorfactory import ClientError
import botocore.errorfactory as Exception

s3 = boto3.client('s3')


def lambda_handler(event, context):
        name = event['name']
        namestr = str(name)+'.jpg'
        image = event['file']
        image=image[2:-1]
        #image = image[image.find(",")+1:]
        dec = base64.b64decode(image)
        try:
            b = s3.head_object(Bucket='imagetrafficbucket', Key=namestr)
        except ClientError:
            try: 
                a=s3.put_object(Bucket='imagetrafficbucket', Key=namestr, Body=dec, ACL='public-read')
                return
            except Exception as e:
                return e
            
        except Exception as e:
            return e

        raise ValueError('SameFileNameExists')
