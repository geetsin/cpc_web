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

class Members(models.Model):
    userName = models.TextField()
    firstName = models.TextField()
    lastName = models.TextField()
    address = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    membershipExpiry = models.DateField()
    familyCount = models.IntegerField()
    upcomingEvent = models.IntegerField()
