from django.db import models

# Create your models here.
class players(models.Model):
    name=models.CharField(max_length=10)
    rank=models.IntegerField()
    no_matches=models.IntegerField()
    address=models.CharField(max_length=10)