from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    sex = models.CharField(max_length=1,
                           choices=(
                               ('f', 'female'),
                               ('m', 'male')
                           ),
                           verbose_name='성별')
    name = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    address = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nickname
    class Meta:
        db_table = "accounts"
    
