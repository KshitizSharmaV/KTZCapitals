# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone

from django.db import models

class Post(models.Model):
	query=models.TextField(max_length=100)
	created_date = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.published_date=timezone.now()

	def __str__(self):
		return self.query
