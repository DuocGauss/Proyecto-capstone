from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone



# Create your models here.
class Compañia(models.Model):
    nombre_compañia = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    # Agrega otros campos según tus necesidades

    def __str__(self):
        return self.nombre_compañia


class AutoBombero(models.Model):
    clave = models.CharField(max_length=20,default="Desconocido")
    patente = models.CharField(max_length=20,default="Desconocido")
    tipo_vehiculo = models.CharField(max_length=50, default="Desconocido")
    marca = models.CharField(max_length=50, default="Desconocido")
    modelo = models.CharField(max_length=50)
    año = models.IntegerField(validators=[MinValueValidator(1900)], default=1900)
    nro_motor = models.CharField(max_length=100, default="Sin especificar")
    nro_chasis = models.CharField(max_length=150, default="Sin especificar")
    compañia = models.ForeignKey(Compañia, on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(upload_to="imgprod", null=True)
    
    def __str__(self):
        return self.clave
    
    
class MantencionVehiculo(models.Model):
    ESTADO_CHOICES = [
        ('Bueno', 'Bueno'),
        ('Malo', 'Malo'),
        ('N/A', 'N/A'),
    ]
    
    TIPO_MANTENCION_CHOICES = [
        ('Preventiva', 'Preventiva'),
        ('Correctiva', 'Correctiva'),
        ('Externa', 'Externa'),
    ]
    
    id_autobombero = models.ForeignKey('AutoBombero', on_delete=models.CASCADE)
    fecha_preventiva_ingreso = models.DateField(default=timezone.now)
    fecha_preventiva_entrega = models.DateField(default=timezone.now)
    fecha_correctiva = models.DateField(default=timezone.now)
    fecha_externa = models.DateField(default=timezone.now)
    hora_motor_preventiva = models.TimeField(default='00:00:00')
    hora_bomba_preventiva = models.TimeField(default='00:00:00')
    hora_motor_correctiva = models.TimeField(default='00:00:00')
    hora_bomba_correctiva = models.TimeField(default='00:00:00')
    kilometraje = models.IntegerField(default=0)
    estado_combustible = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_motor_funcionamiento = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_filtro_aire = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_nivel_aceite_motor = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_tablero_instrumentos = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_nivel_refrigerante = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_nivel_aceite_transmision = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_fugas_aceite_aire = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_frenos_servicio_funcionamiento = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_fugas_aire = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_frenos_estacionamiento = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_nivel_liquido_hidraulico = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_liquido_juego_direccion = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_liquido_fugas = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_parabrisas_ventanas = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_carroceria = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_luces_altas_bajas = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_luces_estacionamiento_viraje = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_luces_traseras_frenos = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_luces_reserva_alarma_retroceso = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_bornes_terminales_bateria = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_presion_desgaste_neumaticos = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_llantas = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_sistemas_sonoros_emergencia = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_luces_emergencia = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_luces_tablero_bomba = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_pto_enganche_bomba = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_lecturas_manometros_manovacuometros = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    estado_fugas_general_funcionamiento_bomba = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='N/A')
    observaciones_preventiva = models.TextField(default="Sin observaciones")
    observaciones_correctiva = models.TextField(default="Sin observaciones")
    observaciones_externa = models.TextField(default="Sin observaciones")
    tipo_mantencion = models.CharField(max_length=20, choices=TIPO_MANTENCION_CHOICES, default='Correctiva')
    

    def __str__(self):
        return f'Mantencion Vehículo #{self.id} - Patente: {self.id_autobombero.patente}'
    
    
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('capitan', 'Capitán'),
        ('mecanico', 'Mecánico'),
        ('comandante', 'Comandante'),
    )
    
    # Agregar un campo de rol
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='mecanico')
    compañia = models.ForeignKey(Compañia, on_delete=models.SET_NULL, null=True, blank=True)
    
    




