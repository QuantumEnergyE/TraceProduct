from django.db import models

# Create your models here.


class Records(models.Model):
    uid = models.CharField(max_length=256)
    url = models.URLField()
    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now_add=True)