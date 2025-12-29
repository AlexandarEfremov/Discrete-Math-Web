from django.urls import path
from math_project.index import views

urlpatterns = [
    path("", views.index, name="index")
]
