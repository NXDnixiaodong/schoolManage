# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from recordApp.models import StuInfo, Subject


class ScoreInfo(models.Model):
    """成绩表"""
    name = models.ForeignKey(StuInfo,verbose_name='学生')
    exam_type = models.CharField(max_length=20, verbose_name='考试类型')
    exam_date = models.DateField(verbose_name='考试日期')
    score = models.PositiveIntegerField(verbose_name='分数')
    subject = models.ForeignKey(Subject, verbose_name='科目')

    class Meta:
        verbose_name_plural = '成绩单'

    def __unicode__(self):
        return u'%s'%self.name