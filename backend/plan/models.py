from django.db import models

class Person(models.Model):
    task = models.CharField(max_length=1000)