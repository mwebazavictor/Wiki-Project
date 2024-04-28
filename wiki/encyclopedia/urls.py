from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/add", views.new_entry, name="add"),
    path("wiki/search", views.search, name="search"),
    path("wiki/edit/<str:title>/",views.edit_page, name="edit"),
    path("wiki/random", views.random_page, name="random"),
    path("wiki/<str:title>", views.entry, name="title"),
    
]
