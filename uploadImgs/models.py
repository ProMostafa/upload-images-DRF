from django.db import models

# Create your models here.


class Pictures(models.Model):
    picture = models.ImageField(upload_to='pictures/')

