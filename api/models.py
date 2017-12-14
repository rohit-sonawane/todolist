# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

# Create your models here.
class TodoList(models.Model):
    """This class represents the bucketlist model."""
    owner = models.ForeignKey('auth.User',  
    related_name='todolists', 
    on_delete=models.CASCADE) 
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=2000)
    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.id)

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)