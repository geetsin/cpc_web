# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from cpc.models import Events
from cpc.models import Members

# Register your models here.

admin.site.register(Events)
admin.site.register(Members)
