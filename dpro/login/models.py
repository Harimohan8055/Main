from django.db import models

# Create your models here.

class users(models.Model):
    TYPE=(
        ('Individual','Individual'),
        ('Institutions','Institutions'),
        ('Companies','Companies'),
    )
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=TYPE)
    mobno = models.IntegerField(max_length=10)
