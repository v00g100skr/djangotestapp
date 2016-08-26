from django.db import models


class Characters(models.Model):
    name = models.CharField(max_length=48)
    height = models.CharField(max_length=8)
    mass = models.CharField(max_length=8)
    hair_color = models.CharField(max_length=16)
    skin_color = models.CharField(max_length=16)
    eye_color = models.CharField(max_length=16)
    birth_year = models.CharField(max_length=8)
    gender = models.CharField(max_length=8)
