from django.urls import path
from . import views

app_name = "app_bomberos"
urlpatterns = [
    path("", views.index, name="index"),
]
