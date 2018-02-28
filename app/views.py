import json

from django.contrib.auth import authenticate

from api import Api
from api import errors
from app.authenticator import authenticator
from app import controllers as app_ctl
from account import controllers as account_ctl

class AppApi(Api):
    authenticator = authenticator


class Signup(AppApi):
    need_authorize = False

    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        account_ctl.create_traveller(username, username, password)


class Login(AppApi):
    need_authorize = False

    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            raise errors.ApiError('用户名或者密码不正确')
        signture = authenticator.gen_sign(user.id)

        data = {
            'signture': signture,
        }

        return data


class Logout(AppApi):

    def post(self, request):
        app_ctl.logout(self.user_id)
