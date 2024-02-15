from django.db import models

# Create your models here.


class Posts(models.Model):
    title: models.CharField(max_length=100)
    body: models.CharField(max_length=400)
    author: models.CharField(max_length=50)

