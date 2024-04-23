from django.db import models

from authorize.models import User


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    body = models.CharField(max_length=255)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)

