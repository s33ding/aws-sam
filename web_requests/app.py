import json
import requests

def lambda_handler(event, context):
    """Collect data from a public API"""
    try:
        # Fetch data from JSONPlaceholder API
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        response.raise_for_status()
        
        data = response.json()
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Data collected successfully',
                'data': data
            })
        }
    except requests.RequestException as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': f'Failed to collect data: {str(e)}'
            })
        }
