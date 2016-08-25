from django.db import models


class Characters(models.Model):
    name = models.CharField(max_length=48)
    height = models.IntegerField()
    mass = models.IntegerField()
    hair_color = models.CharField(max_length=16)
    skin_color = models.CharField(max_length=16)
    eye_color = models.CharField(max_length=16)
    birth_year = models.IntegerField()
    gender = models.CharField(max_length=8)
