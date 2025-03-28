
import boto3
import os


class Database:

    def get_params():

        # Get environment
        env = os.environ.get('ENV', 'local').lower()

        # Set endpoint URL based on environment
        config = {}
        if env == 'local':
            config['endpoint_url'] = os.environ.get(
                'DB_HOST', 'http://localhost:8000')

        return config

    def get_connection():

        client = boto3.client('dynamodb', **Database.get_params())
        return client

    def get_resources():

        client = boto3.resource('dynamodb', **Database.get_params())
        return client

    def run_migration():
        # Connect to DynamoDB
        dynamodb = Database.get_resources()

        table_name = 'invitations'

        # Check if table already exists
        existing_tables = [table.name for table in dynamodb.tables.all()]
        if table_name in existing_tables:
            print(f"Table {table_name} already exists, skipping creation")
        else:
            # Create the table
            table = dynamodb.create_table(
                TableName=table_name,
                KeySchema=[
                    {'AttributeName': 'email',
                        'KeyType': 'HASH'},
                    {'AttributeName': 'code', 'KeyType': 'RANGE'}
                ],
                AttributeDefinitions=[
                    {'AttributeName': 'email', 'AttributeType': 'S'},
                    {'AttributeName': 'code', 'AttributeType': 'S'},
                ],
                BillingMode='PAY_PER_REQUEST',
            )

            print(f"Table {table_name} created successfully")

        print("Migration completed successfully")
