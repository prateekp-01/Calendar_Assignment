from django.contrib import admin
from django.urls import path, include
from calendar_assign import views

urlpatterns = [
    path("", views.index, name="home"),
    path("res", views.result, name="res")
]
