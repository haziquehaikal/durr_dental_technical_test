
import uuid
import time
import boto3
import re
from fastapi.responses import JSONResponse


class MiscFunction:

    def generate_code():
        return str(uuid.uuid4())[:8].upper()

    def generate_response(message, code):

        return JSONResponse(content={'message': message}, status_code=code)

    def validate_email(email: str):
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        print(re.match(email_pattern, email))
        return re.match(email_pattern, email)
