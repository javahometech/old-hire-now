import boto3
import json
import os

dynamodb = boto3.resource('dynamodb')
table_name=os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def post(event, context):
    print(event)
    try:
        resp = {
            'statusCode':200,
            "body": event
        }
        return json.dumps(resp)
    except Exception as e:
        response = {
            'statusCode': 500,
            'message': str(e)
        }
        raise Exception(json.dumps(response))
