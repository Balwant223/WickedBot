from django.db import models
from django.utils.timezone import deactivate

class User(models.Model):
    name=models.CharField(max_length=20)
    number=models.DecimalField(max_digits=10,decimal_places=0)


class JokeCalls(models.Model):
    JOKE_CHOICES=(
        ('fat','Fat'),
        ('dumb','Dumb'),
        ('stupid','Stupid'),
    )
    name=models.CharField(max_length=20,choices=JOKE_CHOICES)
    calls=models.DecimalField(max_digits=100,decimal_places=0)