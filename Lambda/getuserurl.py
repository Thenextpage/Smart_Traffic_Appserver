# This is not a lambda code, but a simple code to access the s3 to get the temporary link to the images 
# which the cognito users 'weakName' Attributes are not yet declared. 
# After checking the image, the Admin will be able to verify the user and give the right attributes using the aws cli

import boto3
import json

client = boto3.client('cognito-idp')
s3 = boto3.client('s3')
response = client.list_users(UserPoolId='us-east-2_YSgIKazhe',AttributesToGet=['email','sub','custom:weakName'])

idlist=[]
idlist2=[]
urllist=[]
a=json.dumps(response, indent=4, sort_keys=True, default=str)
b=json.loads(a)
for i in range(len(b['Users'])):
    if b['Users'][i]['Attributes'][1]["Value"] == 'none':
        idlist.append(b['Users'][i]['Username'])

for key in s3.list_objects(Bucket='imagetrafficbucket')['Contents']:
    filename = key['Key']
    idname=filename.split("_")
    idlist2.append(idname[0])

idlist3=list(set(idlist2))

for j in idlist:
    if j in idlist3:
        presignedurl = s3.generate_presigned_url("get_object", ExpiresIn=3600,
                                                 Params={"Bucket": 'imagetrafficbucket', "Key": j + '.jpg', })
        urllist.append(presignedurl)

print(urllist)
