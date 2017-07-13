from django.db import models


class Category(models.Model):

    title = models.CharField(max_length=100)
    body = models.TextField()
    rank = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.title


class Series(models.Model):

    category = models.ForeignKey(Category)

    title = models.CharField(max_length=100)
    body = models.TextField()
    rank = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.title


class Chapter(models.Model):

    series = models.ForeignKey(Series)

    number = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.TextField()
    rank = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.number + ' ' + self.title
