from django import template
from menu.models import *

register = template.Library()#создание экземпляра класса Library через которое и происходит регистрация собственных шаблонных тегов

@register.simple_tag(name = "getmenu")#декоратор превращения функции в простой тег
def get_menu():
    return Main_menu.objects.all()

@register.simple_tag(name = "dopmenu")#декоратор превращения функции в простой тег
def get_dopmenu():
    return Dop_menu.objects.all()

@register.inclusion_tag("menu/list_dpmenu.html")#декоратор для интегрированного пользовательского тега, функция ниже передает словарь шаблону указанном в параметре декоратора
def show_menu(pk_menu=None):
    if not pk_menu:
        cats = Dop_menu.objects.all()
    else:
        cats = Dop_menu.objects.filter(pk=pk_menu)
    return ({"cats":cats})
