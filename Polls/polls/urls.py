from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.index, name="index"),
    path("grades/", views.grades, name="grades")
]
