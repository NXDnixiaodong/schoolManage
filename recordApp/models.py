# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Grade(models.Model):
    """年级类"""
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "年级"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.name


class Clazz(models.Model):
    """班级表"""
    name = models.CharField(max_length=20)
    grade = models.ForeignKey(Grade)

    class Meta:
        verbose_name = "班级"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.name


class Major(models.Model):
    """专业表"""
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "专业"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.name


class Subject(models.Model):
    """课程表"""
    name = models.CharField(max_length=20)
    major = models.ForeignKey(Major)

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.name


class StuInfo(models.Model):
    """学生管理类"""
    stu_id = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    clazz = models.ForeignKey(Clazz)
    birth = models.DateField()
    address = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    id_num = models.CharField(max_length=20, null=True, blank=True)
    tel_num = models.CharField(max_length=20, null=True, blank=True)
    major = models.ForeignKey(Major,default='')
    subject = models.ManyToManyField(Subject)
    status = models.CharField(max_length=10, default='在校生')
    is_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name = "学生信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.name


class Teacher(models.Model):
    """教师"""
    tea_id = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    tel_num = models.PositiveIntegerField()
    email = models.CharField(verbose_name='电子邮箱', max_length=30)
    birth = models.DateField(verbose_name='出生日期')
    education = models.CharField(verbose_name='学历', max_length=10)
    over_school = models.CharField(verbose_name='毕业院校', max_length=20)
    id_num = models.CharField(verbose_name='身份证号', max_length=20, null=True, blank=True)
    ms = models.BooleanField(verbose_name='婚姻状态', default=False)
    create_date = models.DateField(auto_now_add=True)
    leave_date = models.DateField(null=True,blank=True)
    is_delete = models.BooleanField(default=False)
    clazz = models.ManyToManyField(Clazz)  # 关联班级
    subject = models.ManyToManyField(Subject)  # 关联课程

    class Meta:
        verbose_name = "教师信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.name
