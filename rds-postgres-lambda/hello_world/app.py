import json
import psycopg2
import boto3
import os

def get_secret():
    secret_name = os.environ.get('SECRET_NAME')
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId=secret_name)
    return json.loads(response['SecretString'])

def lambda_handler(event, context):
    try:
        secret = get_secret()
        conn = psycopg2.connect(
            host=secret['host'],
            database=secret['dbname'],
            user=secret['username'],
            password=secret['password']
        )
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Connected to database",
                "db_version": db_version
            }),
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            }),
        }
