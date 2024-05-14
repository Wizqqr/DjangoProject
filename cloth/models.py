from django.db import models

class TagCloth(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Cloth(models.Model):

    name = models.CharField(max_length=100)
    tags = models.ManyToManyField(TagCloth)
    price = models.PositiveIntegerField(default=100)


    def __str__(self):
        return self.name
