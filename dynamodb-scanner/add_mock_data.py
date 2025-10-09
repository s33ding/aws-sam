import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('ItemsTable')

mock_data = [
    {'id': '1', 'name': 'Laptop', 'price': Decimal('999.99'), 'category': 'Electronics'},
    {'id': '2', 'name': 'Coffee Mug', 'price': Decimal('12.50'), 'category': 'Kitchen'},
    {'id': '3', 'name': 'Book', 'price': Decimal('24.99'), 'category': 'Education'},
    {'id': '4', 'name': 'Headphones', 'price': Decimal('79.99'), 'category': 'Electronics'},
    {'id': '5', 'name': 'Desk Chair', 'price': Decimal('199.99'), 'category': 'Furniture'}
]

for item in mock_data:
    table.put_item(Item=item)
    print(f"Added: {item['name']}")

print("Mock data added successfully!")
