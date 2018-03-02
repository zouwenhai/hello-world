from django.contrib.auth import authenticate

from .models import Account
from .models import Platform
from .models import AccountToPlatformMapping


def login(platform, username, password):
    user = authenticate(username=username, password=password)
    if not user:
        raise errors.ApiError('用户名或者密码不正确')


def create_platform(name, sign):
    data = {
        'name': name,
        'sign': sign,
    }
    platform = Platform.objects.create(**data)

    return platform


def create_account(phone, password, name, sex=Account.SEX_UNKNOW, status=Account.ST_NORMAL):
    data = {
        'phone': phone,
        'name': name,
        'sex': sex,
        'status': status,
        'username': phone,
    }
    account = Account.objects.create(**data)
    account.set_password(password)
    account.save()

    return account


def create_account_to_platform_mapping(account_id, platform_ids):

    for platform_id in platform_ids:
        data = {
            'account_id': account_id,
            'platform_id': platform_id,
        }
        AccountToPlatformMapping.objects.create(**data)
