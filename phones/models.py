from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200)
