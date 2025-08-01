# FastAPI AWS Deployment

This project demonstrates a FastAPI application with AWS deployment using Docker, AWS Copilot, and GitHub Actions.

## Project Structure

```
.
├── app/
│   └── main.py          # FastAPI application
├── .github/
│   └── workflows/
│       └── deploy.yml   # GitHub Actions workflow
├── copilot/
│   └── manifest.yml     # AWS Copilot configuration
├── Dockerfile           # Docker configuration
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Local Development

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   cd app
   uvicorn main:app --reload
   ```

4. Access the API documentation at http://localhost:8000/docs

## Docker Build

```
docker build -t fastapi-service .
docker run -p 8000:8000 fastapi-service
```

## Deployment

### Prerequisites

1. AWS account with appropriate permissions
2. AWS CLI configured
3. AWS Copilot CLI installed
4. GitHub repository with secrets configured:
   - `AWS_ROLE_TO_ASSUME`: ARN of an IAM role with permissions to deploy

### Initial Setup

1. Initialize AWS Copilot:
   ```
   copilot init --app fastapi-app --name fastapi-service --type "Load Balanced Web Service" --dockerfile ./Dockerfile
   ```

2. Create environments:
   ```
   copilot env init --name test --profile default
   copilot env init --name prod --profile default
   ```

3. Deploy:
   ```
   copilot deploy --name fastapi-service --env test
   ```

### CI/CD Pipeline

The GitHub Actions workflow will automatically:
1. Build the Docker image
2. Push it to Amazon ECR
3. Deploy using AWS Copilot

## API Endpoints

- `GET /`: Root endpoint, returns service status
- `GET /health`: Health check endpoint
- `POST /items/`: Create a new item
- `GET /items/`: List all items
- `GET /items/{item_id}`: Get a specific item
- `PUT /items/{item_id}`: Update an item
- `DELETE /items/{item_id}`: Delete an item
