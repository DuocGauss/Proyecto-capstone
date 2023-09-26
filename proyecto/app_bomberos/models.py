from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class AutoBombero(models.Model):
    patente = models.CharField(max_length=20,default="Desconocido")
    tipo_de_vehiculo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="imgprod", null=True)
    
    def __str__(self):
        return self.patente
    
    
class MantencionVehiculo(models.Model):
    CARRO_CHOICES = [
        ('Disponible', 'Disponible'),
        ('No Disponible', 'No Disponible'),
        ('En Mantencion', 'En Mantencion'),
    ]

    MOTOR_CHOICES = [
        ('Diesel', 'Diesel'),
        ('Gasolina', 'Gasolina'),
    ]

    ESTADO_CHOICES = [
        ('Bueno', 'Bueno'),
        ('Regular', 'Regular'),
        ('Malo', 'Malo'),
    ]

    id_autobombero = models.ForeignKey('AutoBombero', on_delete=models.CASCADE)
    kilometraje = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    nro_motor = models.CharField(max_length=50)
    nro_chasis = models.CharField(max_length=50)
    fecha = models.DateField()
    numero_orden_compra = models.CharField(max_length=50)
    nombre_mandante = models.CharField(max_length=100)
    nombre_mecanico = models.CharField(max_length=100)
    nombre_proveedor = models.CharField(max_length=100)
    costo_total_mantencion = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion_carro = models.TextField()
    estado_carro = models.CharField(max_length=20, choices=CARRO_CHOICES, default='Disponible')
    tipo_motor = models.CharField(max_length=10, choices=MOTOR_CHOICES)
    estado_motor = models.CharField(max_length=10, choices=ESTADO_CHOICES)
    estado_bateria = models.CharField(max_length=10, choices=ESTADO_CHOICES)
    estado_transmision = models.CharField(max_length=10, choices=ESTADO_CHOICES)
    estado_caja_direccion = models.CharField(max_length=10, choices=ESTADO_CHOICES)
    estado_diferencial = models.CharField(max_length=10, choices=ESTADO_CHOICES)

    def __str__(self):
        return f'Mantencion Vehículo #{self.id} - Patente: {self.id_autobombero.patente}'
