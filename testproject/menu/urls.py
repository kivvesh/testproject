from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='home'),
    path('<int:id_menu>/',menu,name='menu'),
]