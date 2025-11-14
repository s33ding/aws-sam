def lambda_handler(event, context):
    # Get stage from event, fallback to environment, default to prod
    stage = event.get('stage') or event.get('queryStringParameters', {}).get('stage') or 'prod'
    
    if stage == 'dev':
        from dev_handler import handle
    else:
        from prod_handler import handle
    
    return handle(event, context)
