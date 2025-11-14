import json

def handle(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Hello from DEV environment!',
            'stage': 'dev',
            'debug': True,
            'event_info': event.get('httpMethod', 'unknown')
        })
    }
