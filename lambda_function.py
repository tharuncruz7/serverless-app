import json

def lambda_handler(event, context):
    # Example function code
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
