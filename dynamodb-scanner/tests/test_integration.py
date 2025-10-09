import subprocess
import json

def test_remote_invoke():
    """Test the deployed Lambda function"""
    result = subprocess.run([
        'sam', 'remote', 'invoke', 'ScannerFunction', 
        '--stack-name', 'dynamodb-scanner-stack'
    ], capture_output=True, text=True)
    
    assert result.returncode == 0
    response = json.loads(result.stdout)
    assert response['statusCode'] == 200
    
    body = json.loads(response['body'])
    assert 'items' in body
    assert 'count' in body
    print(f"Found {body['count']} items in DynamoDB")

def test_api_endpoint():
    """Test the API Gateway endpoint"""
    result = subprocess.run([
        'curl', '-s', 
        'https://zc2hao52wa.execute-api.us-east-1.amazonaws.com/Prod/scan'
    ], capture_output=True, text=True)
    
    response = json.loads(result.stdout)
    assert 'items' in response
    assert 'count' in response
    print(f"API returned {response['count']} items")
