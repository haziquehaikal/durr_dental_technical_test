# Dental Code Test

A Python project for dental code test

## Prerequisites

> **NOTE** : Please ensure that all items below are installed before proceeding.

- Python 3.11+
- NodeJS 21.x
- OpenJDK 17
- serverless 3.34.0
- pip3 (Python package manager)

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/haziquehaikal/durr_dental_technical_test.git
cd durr_dental_technical_test
```

### 3. Install Dependencies
- Install python dependencies
```bash
pip3 install -r requirements.txt
```
- Install node dependencies
```bash
npm install 
```

### 4. Configure local Dynamo DB

- Download DynamoDB JAR file and unzip it 
```bash
wget https://d1ni2b6xgvw0s0.cloudfront.net/v2.x/dynamodb_local_latest.zip
```

- Run the binary 
```bash 
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
```
> **Note:** You may use other deployment or installation methods via Docker, Maven, etc. See [AWS DynamoDB Local documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html) for more information.



## Running the Project

```bash
serverless offline
```

## Running the test

```bash
pytest
```

## Route
> **Note:** For protected routes, you must include an `Authorization` header with a valid token. You may obtain the token from the `Auth` routes. 
- Invitation
```
POST   /invitation/create       - Create invitation (admin protected route)
GET    /invitation/checkstatus  - Get invitation status
PATCH  /invitation/confirm      - Confirm invitation
DELETE /invitation/delete       - Delete invitation (admin protected route)
```
- Docs
```bash
GET /docs  - swagger documentation
```
- Auth
```
POST /auth/login  - Mock login 
```
