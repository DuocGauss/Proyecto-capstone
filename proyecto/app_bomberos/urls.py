from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('gestion_vehiculos/',views.gestion_vehiculos,name="gestion_vehiculos"),
    path('add_vehiculo/',views.add_vehiculo,name="add_vehiculo"),
    path('update_vehiculo/<int:id>',views.update_vehiculo,name="update_vehiculo"),
    path('delete_vehiculo/<int:id>',views.delete_vehiculo,name="delete_vehiculo"),
    path('detail_vehiculo/<int:id>',views.detail_vehiculo,name="detail_vehiculo"),
    path('register_m/',views.register_m, name='register_m'),
    path('login_custom/', views.login_custom, name='login_custom'),
    path('logout_custom/', views.logout_custom, name='logout_custom'),
    path('compañia/',views.compañia,name="compañia"),
    path('historial_mantenciones/',views.historial_mantenciones,name="historial_mantenciones"),
    path('historial_correctiva/',views.historial_correctiva,name="historial_correctiva"),
    path('historial_externo/',views.historial_externo,name="historial_externo"),

]
