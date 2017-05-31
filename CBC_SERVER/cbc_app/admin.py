# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import coffee_break, user

admin.site.register(coffee_break)
admin.site.register(user)
