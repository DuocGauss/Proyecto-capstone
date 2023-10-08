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
            'fecha_preventiva': forms.DateInput(attrs={'type': 'date'}),
            'fecha_correctiva': forms.DateInput(attrs={'type': 'date'}),
            'fecha_externa': forms.DateInput(attrs={'type': 'date'}),
        }
    
     # Personaliza las etiquetas de los campos de fecha
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_preventiva'].label = 'Fecha'
        self.fields['fecha_correctiva'].label = 'Fecha'
        self.fields['fecha_externa'].label = 'Fecha'
        self.fields['hora_entrada_preventiva'].label = 'Hora de entrada'
        self.fields['hora_entrada_correctiva'].label = 'Hora de entrada'
        self.fields['hora_salida_preventiva'].label = 'Hora de salida'
        self.fields['hora_salida_correctiva'].label = 'Hora de salida'
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
        
