from django.db import models


# Create your models here.
class Test(models.Model):
    str = models.CharField(default='fuck you', max_length=255)
