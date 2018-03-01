from django.db import models


class Account(models.Model):

    platform = models.CharField(max_length=512)
    username = models.CharField(max_length=512)
    password = models.CharField(max_length=512)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)

    @property
    def detail(self):
        data = {
            'platform': self.platform,
            'username': self.username,
            'password': self.password,
        }
        return data
