# -*- coding: utf-8 -*-
from django.db import models

class Task(models.Model):
    subject = models.CharField(u"тема", max_length=200)
    slug = models.SlugField(u"путь", db_index=True)
    description = models.TextField(u"аннотация", null=True, blank=True)

    class Meta:
        verbose_name = u"задача"
        verbose_name_plural = u"задачи"
