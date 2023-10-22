##################################################
#### **************************************** ####
#### !/usr/bin/python3                        ####
#### -*- coding: utf-8 -*-                    ####
#### @Time    : 2023/20/10 11:40              ####
#### @Author  : themanoftalent                ####
#### @Site:https://github.com/themanoftalent  ####
#### @Project : python-app                    ####
#### **************************************** ####
##################################################
from django.contrib import admin
from django.urls import path

from cart import views

urlpatterns = [
    path('', views.index),
    path('add_to_cart/<int:id>', views.add_to_cart),
    path('show_cart', views.show_cart),
    path('admin/', admin.site.urls),
]
