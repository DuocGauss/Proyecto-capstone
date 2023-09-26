from django import forms
from .models import AutoBombero, MantencionVehiculo



class frmVehiculoBomberos(forms.ModelForm):
    class Meta:
        model = AutoBombero
        fields = '__all__'
        

class frmMantencionVehiculo(forms.ModelForm):
    class Meta:
        model = MantencionVehiculo
        exclude = ['id_autobombero']
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
