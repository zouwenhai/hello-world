from django.db import models
from django.contrib.auth.models import User


class Account(User):

    SEX_MALE = 10
    SEX_FEMALE = 20
    SEX_UNKNOW = 30
    SEX_TYP = (
        ('男', SEX_MALE),
        ('女', SEX_FEMALE),
        ('未知', SEX_UNKNOW),
    )

    ST_NORMAL = 10
    ST_FORBIDDEN = 20
    ST_DELETED = 30
    ST_TYP = (
        ('正常', ST_NORMAL),
        ('禁用', ST_FORBIDDEN),
        ('删除', ST_DELETED),
    )

    status = models.SmallIntegerField(choices=ST_TYP, default=ST_NORMAL)
    name = models.CharField(max_length=32, default='')
    phone = models.CharField(max_length=11, default='')
    sex = models.SmallIntegerField(choices=SEX_TYP, default=SEX_UNKNOW)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)


class Platform(models.Model):

    name = models.CharField(max_length=32, default='')
    sign = models.CharField(max_length=32, default='')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)


class AccountToPlatformMapping(models.Model):

    account = models.ForeignKey(Account)
    platform = models.ForeignKey(Platform)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
