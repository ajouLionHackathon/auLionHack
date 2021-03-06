from django.db import models
from pytz import timezone

# Create your models here.
class Trouble(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    create_Date=models.DateTimeField()

    def __str__(self):
        return self.title


class Tr_Comment(models.Model):
    trouble=models.ForeignKey(Trouble, on_delete=models.CASCADE)
    body = models.TextField()
    create_Date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
