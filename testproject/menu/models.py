from django.db import models
from django.urls import reverse


class Main_menu(models.Model):
    title =  models.CharField(max_length=200,unique=True)
    description = models.TextField()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('home',kwargs={'menu_id':self.pk})

class Dop_menu(models.Model):
    title = models.CharField(max_length=200)
    main = models.ForeignKey('Main_menu',on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('dp_menu',kwargs={'dp_menu_id':self.pk})
