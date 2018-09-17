# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from recordApp.models import *
# Register your models here.

admin.site.register(Grade)
admin.site.register(Clazz)
admin.site.register(Subject)
admin.site.register(StuInfo)
admin.site.register(Teacher)
admin.site.register(Major)

