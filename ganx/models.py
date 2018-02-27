from django.db import models


class Account(models.Model):

    platform = models.CharField(max_length=24)
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
