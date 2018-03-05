import json

from django.contrib.auth import authenticate

from api.views import Api
from api import errors

from .models import Treasure
from .authenticator import authenticator
from . import controllers as app_ctl

class AppApi(Api):
    authenticator = authenticator


class Signup(AppApi):
    need_authorize = False

    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')



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


class AccountView(AppApi):
    need_authorize = True

    def get(self, request):
        query = {
            'account_id': self.user_id,
        }
        treasures = Treasure.objects.filter(**query)

        data_list = []
        for treasure in treasures:
            data = treasure.detail
            data_list.append(data)

        data = {
            'account_list': data_list,
        }

        return data

    def post(self, request):
        data = json.loads(request.body)
        platform = data.get('platform') or ''
        username = data.get('username') or ''
        password = data.get('password') or ''

        app_ctl.create_account(platform, username, password)
