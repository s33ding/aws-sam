import sys
import os
import json
from decimal import Decimal
from unittest.mock import Mock, patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scanner'))
import app

def test_lambda_handler_success():
    # Mock DynamoDB response
    mock_table = Mock()
    mock_table.scan.return_value = {
        'Items': [
            {'id': '1', 'name': 'Test Item', 'price': Decimal('10.99')},
            {'id': '2', 'name': 'Another Item', 'price': Decimal('5.50')}
        ]
    }
    
    with patch('app.dynamodb') as mock_dynamodb:
        mock_dynamodb.Table.return_value = mock_table
        
        # Set environment variable
        os.environ['TABLE_NAME'] = 'TestTable'
        
        result = app.lambda_handler({}, None)
        
        assert result['statusCode'] == 200
        body = json.loads(result['body'])
        assert body['count'] == 2
        assert len(body['items']) == 2
        assert body['items'][0]['price'] == 10.99

def test_lambda_handler_error():
    mock_table = Mock()
    mock_table.scan.side_effect = Exception("DynamoDB error")
    
    with patch('app.dynamodb') as mock_dynamodb:
        mock_dynamodb.Table.return_value = mock_table
        
        os.environ['TABLE_NAME'] = 'TestTable'
        
        result = app.lambda_handler({}, None)
        
        assert result['statusCode'] == 500
        body = json.loads(result['body'])
        assert 'error' in body
