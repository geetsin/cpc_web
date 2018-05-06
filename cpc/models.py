# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Events(models.Model):
    eventId = models.IntegerField()
    eventName = models.TextField()
    eventDescription = models.TextField()
    eventDate = models.DateField()
    eventTime = models.TimeField()
    isOpenToAll = models.BooleanField()
    eventDuration = models.TextField()
    eventVenue = models.TextField()
