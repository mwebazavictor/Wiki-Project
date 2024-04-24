from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry, name="title"),
    path("", views.search, name="search"),
    path("add", views.new_entry, name="add")
]
