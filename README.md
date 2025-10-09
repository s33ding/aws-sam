# RDS PostgreSQL Lambda Connector

A serverless application that connects AWS Lambda to RDS PostgreSQL using AWS SAM.

## Prerequisites

- **AWS CLI** installed and configured (`aws configure`)
- **AWS SAM CLI** installed
- **Python 3.9+** installed
- **Docker** running (for local testing)
- **Existing RDS PostgreSQL instance**
- **Database credentials stored in AWS Secrets Manager**

### Install AWS SAM CLI

```bash
# macOS
brew install aws-sam-cli

# Linux/WSL
pip install aws-sam-cli

# Windows
choco install aws-sam-cli
```

## Project Structure

```
rds-postgres-lambda/
├── hello_world/
│   ├── app.py              # Lambda function code
│   └── requirements.txt    # Python dependencies (psycopg2-binary)
├── events/
│   └── event.json         # Test events for local testing
├── tests/                 # Unit tests
├── template.yaml          # SAM infrastructure template
└── samconfig.toml        # SAM deployment configuration
```

## Development Workflow

### 1. Build the Application
```bash
cd rds-postgres-lambda
sam build
```

### 2. Test Locally
```bash
# Start local API server
sam local start-api

# Test specific function
sam local invoke HelloWorldFunction --event events/event.json

# Test API endpoint
curl http://localhost:3000/hello
```

### 3. Deploy to AWS
```bash
# First deployment (guided setup)
sam deploy --guided

# Subsequent deployments
sam deploy
```

## Configuration

The Lambda function requires these environment variables in `template.yaml`:
- `SECRET_NAME`: Name of your Secrets Manager secret containing database credentials

## Common Commands

```bash
# View function logs
sam logs -n HelloWorldFunction --stack-name <your-stack-name> --tail

# Validate SAM template
sam validate

# Generate test events
sam local generate-event apigateway aws-proxy

# Delete the stack
sam delete

# Delete without confirmation prompt
sam delete --no-prompts
```

## Testing

### Local Testing
```bash
# Start API locally
sam local start-api

# Test in another terminal
curl http://localhost:3000/hello
```

### AWS Testing
After deployment, test your live endpoint:
```bash
curl https://<api-id>.execute-api.<region>.amazonaws.com/Prod/hello
```

## Troubleshooting

### Build Issues
- Ensure Docker is running
- Check Python version compatibility
- Verify `requirements.txt` includes `psycopg2-binary`

### Deployment Issues
- Validate template: `sam validate`
- Check IAM permissions for deployment
- Verify AWS credentials are configured

### Runtime Issues
- Check CloudWatch logs for errors
- Verify Secrets Manager permissions in Lambda's IAM role
- Ensure Lambda has network access to RDS (VPC configuration)

## Key Files

### `hello_world/app.py`
Main Lambda function that:
- Retrieves database credentials from Secrets Manager
- Connects to PostgreSQL using psycopg2
- Handles API Gateway requests

### `template.yaml`
SAM template defining:
- Lambda function configuration
- IAM roles and permissions
- API Gateway setup
- Environment variables

### `requirements.txt`
Python dependencies:
```
psycopg2-binary
boto3
```

## Next Steps

1. Add error handling and logging
2. Implement connection pooling
3. Add more API endpoints
4. Set up CI/CD pipeline
5. Add monitoring with CloudWatch

## Resources

- [AWS SAM Documentation](https://docs.aws.amazon.com/serverless-application-model/)
- [Lambda Best Practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
- [psycopg2 Documentation](https://www.psycopg.org/docs/)
