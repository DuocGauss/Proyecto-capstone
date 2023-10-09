from django import forms
from .models import AutoBombero, MantencionVehiculo, CustomUser, Compañia
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from django.forms.widgets import HiddenInput
 



class frmVehiculoBomberos(forms.ModelForm):
    class Meta:
        model = AutoBombero
        fields = '__all__'
        

class frmMantencionVehiculo(forms.ModelForm):
    class Meta:
        model = MantencionVehiculo
        exclude = ['id_autobombero']
        widgets = {
            'fecha_preventiva_ingreso': forms.DateInput(attrs={'type': 'date'}),
            'fecha_preventiva_entrega': forms.DateInput(attrs={'type': 'date'}),
            'fecha_correctiva': forms.DateInput(attrs={'type': 'date'}),
            'fecha_externa': forms.DateInput(attrs={'type': 'date'}),
        }
    
     # Personaliza las etiquetas de los campos de fecha
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_preventiva_ingreso'].label = 'Fecha de ingreso'
        self.fields['fecha_preventiva_entrega'].label = 'Fecha de entrega'
        self.fields['fecha_correctiva'].label = 'Fecha'
        self.fields['fecha_externa'].label = 'Fecha de entrega'
        self.fields['hora_motor_preventiva'].label = 'Hora motor'
        self.fields['hora_bomba_preventiva'].label = 'Hora bomba'
        self.fields['hora_motor_correctiva'].label = 'Hora motor'
        self.fields['hora_bomba_correctiva'].label = 'Hora bomba'
        self.fields['observaciones_preventiva'].label = 'Observaciones'
        self.fields['observaciones_correctiva'].label = 'Observaciones'
        self.fields['observaciones_externa'].label = 'Observaciones'


class frmMecanicoUser(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name','role', 'compañia'] 
        


class frmLogin(AuthenticationForm):
    class Meta:
        model = CustomUser  # Reemplaza 'CustomUser' con el nombre de tu modelo de usuario personalizado
        fields = ['username', 'password'] 
        

class frmCompañia(forms.ModelForm):
    class Meta:
        model = Compañia
        fields = '__all__'
        
