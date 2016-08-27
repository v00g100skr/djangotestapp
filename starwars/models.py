from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import models
from django.utils import timezone


class Characters(models.Model):
    name = models.CharField(max_length=48)
    height = models.CharField(max_length=8)
    mass = models.CharField(max_length=8)
    hair_color = models.CharField(max_length=16)
    skin_color = models.CharField(max_length=16)
    eye_color = models.CharField(max_length=16)
    birth_year = models.CharField(max_length=8)
    gender = models.CharField(max_length=8)
    pic = models.FileField(upload_to='', default='no-img.jpg')


class RequestLog(models.Model):
    scheme = models.CharField(max_length=5)
    method = models.CharField(max_length=4)
    path = models.CharField(max_length=32)
    status = models.CharField(max_length=8)
    code = models.IntegerField()
    date = models.DateTimeField(default=timezone.now())


class CharactersLog(models.Model):
    action = models.CharField(max_length=6)
    character_id = models.IntegerField()
    date = models.DateTimeField(default=timezone.now())


@receiver(post_save, sender=Characters)
def characters_post_save(sender, **kwargs):
    action = 'update'

    if kwargs['created']:
        action = 'create'

    data = CharactersLog(
        action=action,
        character_id=kwargs['instance'].id
    )
    data.save()


@receiver(post_delete, sender=Characters)
def characters_post_delete(sender, **kwargs):
    data = CharactersLog(
        action='delete',
        character_id=kwargs['instance'].id
    )
    data.save()