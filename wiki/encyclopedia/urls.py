from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.entry_page, name="entry"),
    path("wiki/", views.entry_page, name="entry"),
    path("CreateNew/", views.add_entry, name="submission"),
    path("error", views.error, name="error"),
    path("search", views.search, name="search"),
    path("wiki/<str:title>/search", views.search, name="search"),
    path("wiki/search", views.search, name="search"),
    path("wiki/<str:title>/edit", views.edit, name="edit"),
    path("wiki/edit", views.edit, name="edit2")
]

