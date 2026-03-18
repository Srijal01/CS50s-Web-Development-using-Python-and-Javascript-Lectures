from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greeet, name="greeet"),
    path("srijal", views.srijal, name="srijal")
]