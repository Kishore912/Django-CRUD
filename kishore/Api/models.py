from django.db import models

# Create your models here.


class Api_request(models.Model):
    # sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length = 20 )
    age = models.IntegerField()

