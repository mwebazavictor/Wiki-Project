from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.new_entry, name="add"),
    path("", views.search, name="search"),
    path("<str:title>", views.entry, name="title"),
    
]
