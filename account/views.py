import json

from django.shortcuts import render

from api.views import Api
from . import controllers as account_ctl
from .authenticator import authenticator


class AppApi(Api):
    authenticator = authenticator


class LoginView(AppApi):
    need_authorize = False

    def post(self, request):
        data = json.loads(request.body)
        platform_sign = data.get('platform_sign')
        username = data.get('username')
        password = data.get('password')

        user = account_ctl.login(platform_sign, username, password)
        key = '%s:%s' % (platform_sign, user.pk)
        signture = authenticator.gen_sign(key)

        data = {
            'signture': signture,
        }

        return data


class PlatformView(AppApi):

    def post(self, request):
        data = json.loads(request.body)

        name = data.get('name')
        sign = data.get('sign')
        if not name or not sign:
            return

        create_data = {
            'name': name,
            'sign': sign,
        }

        account_ctl.create_platform(**create_data)


class AccountView(AppApi):

    def post(self, request):
        data = json.loads(request.body)

        name = data.get('name')
        phone = data.get('phone')
        sex = data.get('sex')
        password = data.get('password')

        platform_ids = data.get('platform_ids')

        create_data = {
            'phone': phone,
            'password': password,
            'name': name,
            'sex': sex,
            'platform_ids': platform_ids,
        }
        account_ctl.create_account_process(**create_data)
