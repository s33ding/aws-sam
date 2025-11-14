import json

def handle(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Hello from PRODUCTION',
            'stage': 'prod'
        })
    }
