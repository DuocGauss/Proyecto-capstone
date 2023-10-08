from django.contrib import admin
from .models import AutoBombero, MantencionVehiculo, CustomUser, Compañia

# Register your models here.
admin.site.register(AutoBombero)
admin.site.register(MantencionVehiculo)
admin.site.register(CustomUser)
admin.site.register(Compañia)
