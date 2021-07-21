from django.db import models


class User(models.Model):
    GENDER_CHOICES = (
        ('��', '��'),
        ('Ů', 'Ů'),
    )
    name = models.CharField(max_length=30, unique=True, verbose_name='�� ��')
    birthday = models.DateField(blank=True, null=True, verbose_name='�� ��')
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, verbose_name='�� ��')
    account = models.IntegerField(default=0, verbose_name='�� ��')
    age = models.IntegerField(default=18, verbose_name='�� ��')