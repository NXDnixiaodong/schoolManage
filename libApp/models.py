# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from datetime import datetime
# from django.utils import timezone
import datetime

from django.db import models

from recordApp.models import StuInfo


class BookInfo(models.Model):
    name = models.CharField(max_length=30)
    book_id = models.CharField(max_length=20, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    book_type = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    publish_time = models.DateField()
    publish_house = models.CharField(max_length=30)
    content = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = '图书'

    def __unicode__(self):
        return u'%s' % self.name


class BorrowBook(models.Model):
    stu_name = models.ForeignKey(StuInfo)
    book_name = models.ManyToManyField(BookInfo)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(default=datetime.datetime.now() + datetime.timedelta(days=30))
    price = models.CharField(max_length=10, default='100')

    class Meta:
        verbose_name_plural = '借阅单'

    def __unicode__(self):
        return u'%s' % self.stu_name
