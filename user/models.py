from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile')
