# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from recordApp.models import StuInfo, Subject


class ScoreInfo(models.Model):
    """成绩表"""
    name = models.ForeignKey(StuInfo)
    exam_type = models.CharField(max_length=20)
    exam_date = models.DateField()
    score = models.PositiveIntegerField()
    subject = models.ForeignKey(Subject)
