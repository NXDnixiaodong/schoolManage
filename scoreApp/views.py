# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
from .models import *
from django.shortcuts import render, redirect
from recordApp.models import *
from django.db import connection
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    if request.method == "POST":
        return HttpResponse('POST')
    else:
        cursor = connection.cursor()
        sql = 'select name_id, exam_date from scoreApp_scoreinfo group by name_id,exam_date order by exam_date'
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        list1 = []
        for i in result:
            stu = StuInfo.objects.get(pk=i[0])
            print stu
            score = stu.scoreinfo_set.filter(exam_date=i[1])
            list1.append([stu,score, i[1]])
        return render(request, 'order-list.html', {'stu': list1})


@login_required
def delete(request):
    id = request.GET.get('id')
    date = request.GET.get('date')
    stu = StuInfo.objects.get(pk=id)
    date = date.replace('年', '-')
    date = date.replace('月', '-')
    date = date.replace('日', '')
    stu.scoreinfo_set.filter(exam_date=date).delete()
    return JsonResponse({'date':'已删除'})


@login_required
def add(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        username = request.POST.get('username')
        score = request.POST.getlist('score')
        exam_type = request.POST.get('exam_type')
        date = request.POST.get('date')
        stu = StuInfo.objects.get(pk=id)
        subject = stu.subject.all().order_by('id')
        num = 0
        for i in subject:
            print i, stu, exam_type, date, score[num]
            ScoreInfo.objects.create(name=stu, exam_type=exam_type, exam_date=date, score=score[num], subject=i)
            num += 1
        return redirect('/score/')

    else:
        return render(request, 'order-add.html')


@login_required
def add_ajax(request, id):
    try:
        stu = StuInfo.objects.get(pk=id)
        subject = stu.subject.all().order_by('id')
        subject = [i.name for i in subject]
        print subject
    except Exception as e:
        return redirect('/score/add/')
    else:
        return JsonResponse({'subject': [subject], 'stu': stu.name})


@login_required
def find(request):
    if request.method == "POST":
        start = request.POST.get('start')
        end = request.POST.get('end')
        username = request.POST.get('username')
        if StuInfo.objects.filter(pk=username):
            stu = StuInfo.objects.get(pk=username)
        else:
            stu = StuInfo.objects.get(pk=1)
        result = stu.scoreinfo_set.filter(exam_date__gt=start).filter(exam_date__lt=end)
        print result
        return render(request, 'find.html', {'stu': result})
    else:
        return redirect('/')


# @login_required
# def grade(request):
#     if request.method == "POST":
#         # 获取查询条件： 年级 考试类型 考试时间
#         grade = request.POST.get('grade')
#         exam_type = request.POST.get('exam_type')
#         date = request.POST.get('date')
#         # 找出所选年级的所有班级
#         clazzs = Clazz.objects.filter(grade__name=grade)
#         print grade, exam_type, date ,clazzs
#         for cls in clazzs:
#             stus = StuInfo.objects.filter(clazz__name=cls)
#             # 当前班级总分数
#             cls_score_sum = 0
#             # 当前班级总人数
#             stu_num = 0
#             print cls, stus
#             for stu in stus:
#                 # 获取每个学生在当前类别考试与具体时间下所得到的全部成绩
#                 score = stu.scoreinfo_set.filter(exam_type=exam_type).filter(exam_date=date).aggregate(Sum('score'))
#                 cls_score_sum += score
#                 stu_num += 1
#                 print score
#         return render(re)
#     else:
#         return render(request, 'grade.html')


@login_required
def clazz(request):
    if request.method == "POST":
        # 获取查询条件： 班级 考试类型 考试时间
        clazz = request.POST.get('clazz')
        exam_type = request.POST.get('exam_type')
        date = request.POST.get('date')
        # 找出所选班级的所有的学生
        stus = StuInfo.objects.filter(clazz__name=clazz)
        result = {}
        print clazz, exam_type, date
        print stus
        for stu in stus:
            # 获取当前学生在当前类别考试与具体时间下所得到的全部成绩
            score = stu.scoreinfo_set.filter(exam_type=exam_type).filter(exam_date=date)
            if score:
                result[stu] = [score]
        print result
        if result:
            msg = None
        else:
            msg = '没有当前查询结果！'
        return render(request, 'clazz.html', {'stus': result})
    else:
        return render(request, 'clazz.html')