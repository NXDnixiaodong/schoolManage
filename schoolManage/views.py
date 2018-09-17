from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def welcome(request):
    return render(request, 'welcome.html')
