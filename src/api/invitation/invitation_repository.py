from src.common.database import Database
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr

dynamodb = Database.get_resources()
table = dynamodb.Table('invitations')
client = Database.get_connection()


class InvitationRepository:

    def create_invitation(invitation):
        print(invitation)
        try:
            table.put_item(Item=invitation)
            return "Invitation created successfully."
        except ClientError as e:
            return f"Error creating invitation: {e.response['Error']['Message']}"

    def get_invitation(email, code):

        response = table.get_item(
            Key={'code': code, 'email': email})

        return response.get('Item')

    def get_invitation_by_email_and_status(email, status):
        response = table.query(
            KeyConditionExpression=Key('email').eq(
                email),
            FilterExpression=Attr('status').eq(status)
        )

        return response.get('Items')

    def update_invitation(key, UpdateExpression, ExpressionAttributeNames, ExpressionAttributeValues):

        response = table.update_item(
            Key=key,
            UpdateExpression=UpdateExpression,
            ExpressionAttributeNames=ExpressionAttributeNames,
            ExpressionAttributeValues=ExpressionAttributeValues,
            ReturnValues="UPDATED_NEW"
        )
        return response
