from django.contrib.auth import authenticate

from api import errors

from .models import Account
from .models import Platform
from .models import AccountToPlatformMapping


def login(platform_sign, username, password):
    user = authenticate(username=username, password=password)
    if not user:
        raise errors.ApiError('用户名或者密码不正确')
    platform = Platform.objects.filter(sign=platform_sign).first()
    if not platform:
        raise errors.ApiError('平台标识异常')
    if not  AccountToPlatformMapping.objects.filter(account_id=user.pk, platform=platform).exists():
        raise errors.ApiError('当前用户无权登录此系统')

    return user



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


def create_account_process(phone, password, name, sex=Account.SEX_UNKNOW,
        status=Account.ST_NORMAL, platform_ids=[]):
    account = create_account(phone, password, name, sex, status)
    create_account_to_platform_mapping(account.pk, platform_ids)
