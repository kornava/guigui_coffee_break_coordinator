# -*- coding: utf-8 -*-
# TODO : Add reservation feature, users can see if
# the place is busy or not(or reserved by somebodyelse)
from __future__ import unicode_literals

from django.db import models

import datetime


class user(models.Model):
    user_name = models.CharField(max_length=20, default="name")

    def __str__(self):
        return self.user_name

class coffee_break(models.Model):
    date = models.DateField(default="2017-02-02")
    time = models.TimeField(default="00:00:00")
    place = models.CharField(max_length=20, default="4B1")
    users = models.ManyToManyField(user)
    # def set_date(self)
    #     self.date = None
    # def set_time(self)
    #     self.time = None

    def __str__(self):
        return self.place