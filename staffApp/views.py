# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    num = request.GET.get('num', '1')
    users = User.objects.all()
    pg = Paginator(users,4)
    print '---' * 20
    num = int(num)
    if num < 1:
        num = 1
    if num > pg.num_pages:
        num = pg.num_pages

    start = ((num - 1) / 4) * 4 + 1
    end = start + 4
    if end > pg.num_pages:
        end = pg.num_pages + 1

    page = pg.page(num)
    # return HttpResponse(page)
    return render(request, 'admin-list.html', {'page': page, 'page_range': range(start,end)})

@login_required
def find(request):
    if request.method == "POST":
        username = request.POST.get('username')
        us = User.objects.filter(username=username)
        return render(request, 'admin-list.html', {'users': us})
    else:
        return redirect('/staff/')

@login_required
def add(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        like = request.POST.get('like')
        password = request.POST.get('repass')
        user = User.objects.create_user(username=username, email=email, password=password)
        if like == '超级管理员':
            user.is_superuser = True
        else:
            user.is_superuser = False
        user.save()
        return redirect('/staff/')
    else:
        return render(request, 'admin-add.html')
