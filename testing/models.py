# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

class article(models.Model):
    AID = models.IntegerField(primary_key=True, default=None)
    Title = models.CharField(max_length=100)
    Date = models.DateField()
    Categories = models.CharField(max_length=100)
    Summary = models.CharField(max_length=500)
    Source = models.CharField(max_length=100)
    Source_url = models.CharField(max_length=200)
    Author = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __unicode__(self):
        return '%s %s' % (self.Title, self.Author)
