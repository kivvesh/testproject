from django.contrib import admin

# Register your models here.
from .models import *

class MenuAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Main_menu,MenuAdmin)

admin.site.register(Dop_menu)
