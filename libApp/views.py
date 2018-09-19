# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import jsonpickle
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from libApp.models import BookInfo


@login_required
def page(num, size):
    num = int(num)

    book = Paginator(BookInfo.objects.all().order_by('-id'), size)
    # print(posts)
    if num <= 0:
        num = 1

    if num > book.num_pages:
        num = book.num_pages

    start = ((num - 1) / 3) * 3 + 1
    end = start + 3

    if end > book.num_pages:
        end = book.num_pages + 1

    return book.page(num), range(start, end)


@login_required
def list_view(request, num=1):
    size = 1
    book, page_range = page(num, size)
    # book = BookInfo.objects.filter(id__lt='10')
    return render(request, 'lib-manage.html', {'book': book, 'page_range': page_range})


@login_required
def manage_view(request):
    return render(request, 'lib-test.html')


@login_required
def add_view(request):
    if request.method == 'GET':
        return render(request, 'lib-add.html')
    else:
        book_id = request.POST.get('book_id', '')
        name = request.POST.get('name', '')
        price = request.POST.get('price', '')
        book_type = request.POST.get('book_type', '')
        author = request.POST.get('author', '')
        publish_time = request.POST.get('publish_time', '')
        publish_house = request.POST.get('publish_house', '')
        content = request.POST.get('content', '')

        if book_id and author:
            book = BookInfo(book_id=book_id, name=name, price=price, book_type=book_type, author=author,
                            publish_time=publish_time, publish_house=publish_house, content=content)
            book.save()

            return HttpResponse('<script>alert("添加成功");location.href="/lib/add/";</script>')

        return HttpResponse('<script>alert("添加失败，请重新添加");location.href="/lib/add/";</script>')


@login_required
def sreach_view(request):
    if request.method == 'GET':
        return render(request, 'lib-search.html')
    else:
        book_name = request.POST.get('book_name', '')
        book = BookInfo.objects.filter(name__contains=book_name)
        return render(request, 'lib-search.html', {'book': book})


import datetime


@login_required
def update_view(request, bid):
    bid = int(bid)
    book = BookInfo.objects.filter(id=bid)
    pub_time = datetime.datetime.strftime(book[0].publish_time, '%Y-%m-%d')

    return render(request, 'lib-update.html', {'book': book[0], 'pub_time': pub_time})


@login_required
def update1_view(request, bid):
    bid = int(bid)
    print bid
    postdict = request.POST.dict()
    postdict.pop('csrfmiddlewaretoken')
    print postdict
    BookInfo.objects.filter(id=bid).update(**postdict)

    return HttpResponseRedirect('/lib/list/')


@login_required
def delete_view(request):
    delList = request.GET.get('delList', '')
    delList = jsonpickle.loads(delList)
    for dl in delList:
        dl = int(dl)
    BookInfo.objects.filter(book_id=dl).delete()
    return HttpResponseRedirect('/lib/list/')
