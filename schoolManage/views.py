# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from recordApp.models import StuInfo, Teacher
from libApp.models import BookInfo


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def welcome(request):
    admin_sum = User.objects.count()
    stu_sum = StuInfo.objects.count()
    teacher_sum = Teacher.objects.count()
    book_sum = BookInfo.objects.count()
    sum = admin_sum + teacher_sum
    return render(request, 'welcome.html', {'admin_sum': admin_sum, 'stu_sum': stu_sum, 'teacher_sum': teacher_sum, 'book_sum': book_sum, 'sum': sum})


def login_index(request):
    if request.method == 'POST':
        username =  request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                msg = '登录失败'
                return render(request, 'login.html', {'msg': msg})
    else:
        return render(request, 'login.html')


@login_required
def loginout(request):
    logout(request)
    return redirect('/login/')