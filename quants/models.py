# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Posts(models.Model):
    author = models.ForeignKey('auth.User', default='Kshitiz')
    title = models.CharField(max_length=200, default='AAPL')
    text = models.TextField('Hello')
    created_date = models.DateTimeField(
            default=timezone.now)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


