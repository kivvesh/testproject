from django.shortcuts import render
from .models import *

# Create your views here.

def index(requests):
    menu = Main_menu.objects.all()
    dp_menu = Dop_menu.objects.all()
    context = {'dpmenu':dp_menu}
    return render(requests,'menu/base.html',context=context)

def menu(requests,id_menu):
    dp_menu = Dop_menu.objects.get(pk = id_menu)
    return render(requests,'menu/menu.html',{'menu':dp_menu})