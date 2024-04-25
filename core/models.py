from django.db import models

from authorize.models import User


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    body = models.CharField(max_length=255)
    translate_to = models.CharField(max_length=30)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'message'

