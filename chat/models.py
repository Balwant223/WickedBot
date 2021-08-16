from django.db import models
from django.utils.timezone import deactivate


class User(models.Model):
    name=models.CharField(max_length=20)
    f_joke=models.DecimalField(max_digits=100,decimal_places=0,default=0)
    d_joke=models.DecimalField(max_digits=100,decimal_places=0,default=0)
    s_joke=models.DecimalField(max_digits=100,decimal_places=0,default=0)