from django.db import models


class User(models.Model):
    GENDER_CHOICES = (
        ('男', '男'),
        ('女', '女'),
    )
    name = models.CharField(max_length=30, unique=True, verbose_name='姓 名')
    birthday = models.DateField(blank=True, null=True, verbose_name='生 日')
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, verbose_name='性 别')
    account = models.IntegerField(default=0, verbose_name='工 号')
    age = models.IntegerField(default=18, verbose_name='年 龄')