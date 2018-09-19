# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
import json
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from recordApp.models import StuInfo, Subject, Major, Clazz



@login_required
def member_list(request):
    """学生信息维护列表"""
    stu_all = StuInfo.objects.get_in_stu()  # 得到所有的学生信息，除了is_delete = True

    stu_count = stu_all.count()  # 统计所有活跃学生的个数

    # 分页
    num = request.GET.get('num', '1')
    pg = Paginator(stu_all, 4)
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

    data = {
        'stu_all': stu_all,
        'stu_count': stu_count,
        'page': page,
        'page_range': range(start, end)
    }
    return render(request, 'member-list.html', data)


@login_required
def ajax_status(request):
    """处理AJAX请求，改变学生的状态"""
    # 获取参数
    stu_id = request.POST.get('stu_id', '')
    status = request.POST.get('status', '在校生')

    # 更改数据库状态并保存结果
    stu = StuInfo.objects.get(stu_id=stu_id)

    stu.status = status
    stu.save()

    # 返回json数据
    data = {
        "temp": "1",
    }
    return JsonResponse(data)


@login_required
def ajax_delete(request):
    """处理AJAX请求，删除学生"""
    # 获取参数
    stu_id = request.POST.get('stu_id', '')
    # 更改数据库状态并保存结果
    stu = StuInfo.objects.get(stu_id=int(stu_id))
    stu.is_delete = True
    stu.save()
    # 返回json数据
    data = {
        "temp": '1',
    }
    return JsonResponse(data)


@login_required
def ajax_del_all(request):
    """处理AJAX请求，批量删除"""
    # 得到数据
    data_stu_id = request.POST.get('data')
    # 反序列化JSON字符串
    data_list = json.loads(data_stu_id)
    # 便利批量修改
    for i in data_list:
        stu = StuInfo.objects.get(stu_id=i)
        stu.is_delete = True
        stu.save()
    data = {

    }
    return JsonResponse(data)


@login_required
def member_edit(request):
    """处理学生的修改方法"""
    # 通过GET请求的到编辑id
    id_stu = request.GET.get('id_stu')
    # 得到学生对象
    stu = StuInfo.objects.get(id=id_stu)
    # 传递到前端界面

    return render(request, 'member-edit.html', {
        'stu': stu,
    })


@login_required
def ajax_stu_edit(request):
    # 获取数据
    id = request.POST.get('id')
    status = request.POST.get('status')
    stu_id = request.POST.get('stu_id')
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    clazz = request.POST.get('clazz')
    birth = request.POST.get('birth')
    address = request.POST.get('address')
    age = request.POST.get('age')
    id_num = request.POST.get('id_num')
    tel_num = request.POST.get('tel_num')
    major = request.POST.get('major')
    print status
    # 得到学生对象
    stu = StuInfo.objects.get(id=id)
    stu.status = status
    stu.stu_id = stu_id
    stu.name = name
    stu.gender = gender
    stu.clazz.name = clazz
    stu.birth = birth
    stu.address = address
    stu.age = age
    stu.id_num = id_num
    stu.tel_num = tel_num
    stu.major.name = major
    # 保存对象
    stu.save()

    return JsonResponse({})


@login_required
def member_add(request):
    """展示添加界面"""
    # 专业
    sub_all = Subject.objects.all()
    # 课程
    major_all = Major.objects.all()
    # 班级
    clazz_all = Clazz.objects.all()

    return render(request, 'member-add.html', {'sub_all': sub_all,
                                               'major_all': major_all,
                                               'clazz_all': clazz_all,
                                               })


@login_required
def ajax_stu_add(request):
    """学生的添加"""
    # 获得数据
    fromdata = request.POST.get('fromdata')
    data_dict = json.loads(fromdata)
    sub = []
    for k, v in data_dict.items():
        if v == 'on':
            sub.append(k)
    # 获取外键对象
    clazz = Clazz.objects.get(name=data_dict['clazz'])
    major = Major.objects.get(name=data_dict['major'])

    stu = StuInfo.objects.create(
        stu_id=data_dict['stu_id'],
        name=data_dict['name'],
        gender=data_dict['gender'],
        clazz=clazz,
        birth=data_dict['birth'],
        address=data_dict['address'],
        age=data_dict['age'],
        id_num=data_dict['id_num'],
        tel_num=data_dict['tel_num'],
        major=major,
    )

    # 遍历的到多许多对象
    sub_obj = []
    for s in sub:
        sub1 = Subject.objects.get(name=s)
        sub_obj.append(sub1)
    # 添加多对对的关系
    stu.subject.add(*sub_obj)
    stu.save()
    return JsonResponse({})


@login_required
def search_stu(request):
    """搜索活跃学生"""
    start = request.POST.get('start', '')
    end = request.POST.get('end', '')
    wb = request.POST.get('username', '')
    stu_all = StuInfo.objects.get_in_stu()
    if start and end:
        stu_all = stu_all.filter(create_date__range=(start, end))
        if wb != '':
            stu_all = stu_all.filter(name__contains=wb)
    elif wb:
        stu_all = stu_all.filter(name__contains=wb)
    else:
        stu_all = ''
    # 分页
    num = request.GET.get('num', '1')
    pg = Paginator(stu_all, 4)
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

    data = {
        'stu_all': stu_all,
        'page': page,
        'page_range': range(start, end)
    }

    return render(request, 'member-list.html',data)


@login_required
def member_list_rec(request):
    """非活跃学生的处理"""
    stu_all = StuInfo.objects.get_on_stu()

    stu_count = stu_all.count()  # 统计所有活跃学生的个数

    # 分页
    num = request.GET.get('num', '1')
    pg = Paginator(stu_all, 4)
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

    data = {
        'stu_all': stu_all,
        'stu_count': stu_count,
        'page': page,
        'page_range': range(start, end)
    }

    return render(request, 'member-list-rec.html',data)


@login_required
def ajax_rec(request):
    # 获取恢复学生的stu_id
    stu_id = request.POST.get('stu_id')
    # 得到学生对象
    stu = StuInfo.objects.get(stu_id=stu_id)
    # 更改状态
    stu.is_delete = False
    stu.save()
    return JsonResponse({})


@login_required
def ajax_rec_all(request):
    """处理AJAX请求，批量恢复"""
    # 得到数据
    data_stu_id = request.POST.get('data')
    # 反序列化JSON字符串
    data_list = json.loads(data_stu_id)
    # 便利批量修改
    for i in data_list:
        stu = StuInfo.objects.get(stu_id=i)
        stu.is_delete = False
        stu.save()
    data = {

    }
    return JsonResponse(data)


@login_required
def search_rec_stu(request):
    """搜索删除学生"""
    start = request.POST.get('start', '')
    end = request.POST.get('end', '')
    wb = request.POST.get('username', '')
    stu_all = StuInfo.objects.get_on_stu()
    if start and end:
        stu_all = stu_all.filter(create_date__range=(start, end))
        if wb != '':
            stu_all = stu_all.filter(name__contains=wb)
    elif wb:
        stu_all = stu_all.filter(name__contains=wb)
    else:
        stu_all = ''

        # 分页
        num = request.GET.get('num', '1')
        pg = Paginator(stu_all, 4)
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

        data = {
            'stu_all': stu_all,
            'page': page,
            'page_range': range(start, end)
        }

    return render(request, 'member-list-rec.html', data)
