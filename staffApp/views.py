# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.core.paginator import Paginator
from recordApp.models import *
from django.shortcuts import render
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

# Create your views here.
#接收前台的数据并往数据库添加
def staff_view(request):
    if request.method == 'GET':
        #接收班级与课程的数据并在页面展示与遍历
        clzs=Clazz.objects.all()
        course=Subject.objects.all()
        return render(request, 'staff-add.html',{'clzs':clzs,'course':course})
    else:
        #接收页面数据
        stff_id=request.POST.get('staff_num','')
        staff_username=request.POST.get('staff_username', '')
        staff_gender=request.POST.get('gender', '')
        staff_age=request.POST.get('staff_age', '')
        staff_address=request.POST.get('staff_address', '')
        staff_phone=request.POST.get('staff_phone', '')
        staff_email=request.POST.get('staff_email', '')
        staff_birth=request.POST.get('staff_birth', '')
        staff_eb=request.POST.get('staff_eb', '')
        staff_college=request.POST.get('staff_college', '')
        staff_id=request.POST.get('staff_id', '')
        staff_marry=request.POST.get('staff_marry', '')
        staff_date=request.POST.get('staff_date', '')
        staff_leave_date=request.POST.get('staff_leave_date', '')
        staff_dimission=request.POST.get('staff_dimission', '')
        staff_clz=request.POST.getlist('staff_clz',[])
        staff_course=request.POST.getlist('staff_course',[])
        #print staff_clz,staff_id,staff_username
        #判断是否存在
        if stff_id and staff_username:
            #往数据库添加数据
            staff=Teacher.objects.create(tea_id=stff_id,name=staff_username,gender=staff_gender,age=staff_age,address=staff_address,tel_num=staff_phone,email=staff_email,birth=staff_birth,education=staff_eb,over_school=staff_college,id_num=staff_id,ms=staff_marry,create_date=staff_date,leave_date=staff_leave_date,is_delete=staff_dimission)
            # st_clz = Clazz(name=staff_clz)
            # #添加Teacher表中数据不包含多对多字段
            # # t.clazz.add(st_clz)
            # staff.clazz.add(st_clz)
            # st_course=Subject(name=staff_course)
            # staff.subject.add(st_course)
            #添加班级数据
            clazz = []
            for c in staff_clz:
                cla = Clazz.objects.get(name=c)
                clazz.append(cla)
            staff.clazz.add(*clazz)
            #添加课程数据
            cour=[]
            for cr in staff_course:
                cou=Subject.objects.get(name=cr)
                cour.append(cou)
            staff.subject.add(*cour)
            staff.save()
            return HttpResponse('<script>alert("添加成功");location.href="/staff/staffadd/";</script>')
        else:
            return HttpResponse('<script>alert("添加失败，请重新添加");location.href="/staff/staffadd/";</script>')

#定义分页函数
def get_staff_num(num,size):
    num=int(num)
    staffs=Paginator(Teacher.objects.all().order_by('-create_date'),size)
    if num <= 0:
        num=1
    if num > staffs.num_pages:
        num=staffs.num_pages
    start=((num-1)/3)*3+1
    end=start+3
    if end > staffs.num_pages:
        end=staffs.num_pages+1
    return staffs.page(num),range(start,end)

#展示所有的教师信息
def stafflist_view(request,num='1'):
    size=1
    staffs,page_range=get_staff_num(num,size)
    return render(request,'staff-list.html',{'staffs':staffs,'page_range':page_range})

#搜索函数转至搜索结果页面
def staffsearch_view(request):
    if request.method == 'GET':
        name=request.GET.get('name','')
        # print name
        teach = Teacher.objects.all()
        count =teach.count()
        count = int(count)
        list1 = []
        for i in range(0,count):
            tname = teach[i].name
            list1.append(tname)
        # 判断页面接收的教师信息是否存在与数据库中，存在则将搜索结果展示在搜索页面中
        if name in list1:
            staffsearch=Teacher.objects.get(name=name)
            #print staffsearchs
            return render(request,'staff-search.html',{'staffsearch':staffsearch})
        #如果与数据库的信息不匹配，则提示警报信息，并返回教师信息展览页面
        #elif name :
            #staffsearch=Teacher.objects.get(name__contains=name)
            #return render(request,'staff-search.html',{'staffsearch':staffsearch})
        else:
            return HttpResponse('<script>alert("没有该条查询结果，请重新搜索");location.href="/staff/stafflist/";</script>')
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

#对教师信息进行修改
def staffupdate_view(request,pid):
    staff = Teacher.objects.filter(tea_id=pid)
    #print staff
    clzs = Clazz.objects.all()
    course = Subject.objects.all()
    return render(request,'staff-update.html',{'clzs':clzs,'course':course,'staff':staff})

#修改后的教师信息提交到数据库中
def staffupdated_view(request,pid):
    stff_id = request.POST.get('staff_num', '')
    staff_username = request.POST.get('staff_username', '')
    staff_age = request.POST.get('staff_age', '')
    staff_address = request.POST.get('staff_address', '')
    staff_phone = request.POST.get('staff_phone', '')
    staff_email = request.POST.get('staff_email', '')
    staff_birth = request.POST.get('staff_birth', '')
    staff_college = request.POST.get('staff_college', '')
    staff_id = request.POST.get('staff_id', '')
    staff_date = request.POST.get('staff_date', '')
    staff_leave_date = request.POST.get('staff_leave_date', '')
    staffs=Teacher.objects.filter(tea_id=pid).update(tea_id=stff_id,name=staff_username,age=staff_age,address=staff_address,tel_num=staff_phone,email=staff_email,birth=staff_birth,over_school=staff_college,id_num=staff_id,create_date=staff_date,leave_date=staff_leave_date)
    return HttpResponse('<script>alert("数据更新完毕，请继续添加");location.href="/staff/stafflist/";</script>')