import boto3
import json
import os
import uuid

dynamodb = boto3.resource('dynamodb')
table_name=os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def post(event, context):
    try:
        job_id = str(uuid.uuid4())
        event['job_id'] = job_id
        table.put_item(
            Item=event
        )
        resp = {
            'statusCode':200,
            "message": "Job Posted Successfully",
            "job_id": job_id
        }
        return json.dumps(resp)
    except Exception as e:
        response = {
            'statusCode': 500,
            'message': str(e)
        }
        raise Exception(json.dumps(response))
