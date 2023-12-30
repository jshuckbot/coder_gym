from django.urls import path

from coursesapp import views

urlpatterns = [
    path("", views.index, name="index"),
]
