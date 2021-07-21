import datetime

from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    reg_date = models.DateTimeField('date created')
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)


class Result(models.Model):
    filename = models.CharField(max_length=200)
    gap_percent = models.FloatField(max_length=10000, default=0.1)
    p1 = models.FloatField(max_length=10000, default=0.01)
    p2 = models.FloatField(max_length=10000, default=0.05)
    inf = models.TextField(max_length=10000)
    mut_inf = models.TextField(max_length=10000)
    tri_inf = models.TextField(max_length=10000)
    graph = models.TextField(max_length=10000)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
