import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Hello from DEV - with debug info!',
            'stage': 'dev',
            'debug': True,
            'event': event
        })
    }
