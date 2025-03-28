from src.common.misc_func import MiscFunction
from src.common.models import Login


class AuthService:

    def login(payload: Login):
        token = ''
        if payload.email == 'admin' and payload.password == 'test':
            token = 'admin'

        elif payload.email == 'user' and payload.password == 'user':
            token = 'user'

        else:
            return MiscFunction.generate_response('Invalid credentials', 401)

        return MiscFunction.generate_response({
            'token': token
        }, 201)

    def logout():
        pass
