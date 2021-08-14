from typing import MutableMapping
from django.shortcuts import render
from django.http import HttpResponse
from .models import city


def index(request):

    

    citys  = city.objects.all()
    return render(request,'index.html',{'citys':citys})