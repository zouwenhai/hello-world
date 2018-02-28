from django.contrib.auth import authenticate

from api import errors
from app.authenticator import authenticator


def login(username, password):
    user = authenticate(username=username, password=password)
    if not user:
        raise errors.ApiError('用户名或者密码不正确')

    signature = authenticator.gen_sign(user.id)

def logout(user_id):
    authenticator.clear_sign(user_id)
