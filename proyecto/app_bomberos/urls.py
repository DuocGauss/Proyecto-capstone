from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('gestion_vehiculos/',views.gestion_vehiculos,name="gestion_vehiculos"),
    path('add_vehiculo/',views.add_vehiculo,name="add_vehiculo"),
    path('update_vehiculo/<int:id>',views.update_vehiculo,name="update_vehiculo"),
    path('delete_vehiculo/<int:id>',views.delete_vehiculo,name="delete_vehiculo"),
    path('detail_vehiculo/<int:id>',views.detail_vehiculo,name="detail_vehiculo"),
]
