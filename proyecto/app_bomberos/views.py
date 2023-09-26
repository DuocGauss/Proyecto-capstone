from django.shortcuts import render, redirect, get_object_or_404
from .models import AutoBombero
from .forms import frmVehiculoBomberos, frmMantencionVehiculo
from django.contrib import messages

# Create your views here.

def index(request):
    obtener = AutoBombero.objects.all()
    return render(request, 'app_bomberos/index.html', {
        'obtener': obtener
    })


def gestion_vehiculos(request):
    obtener = AutoBombero.objects.all()
    return render(request, 'app_bomberos/gestion_vehiculos.html', {
        'obtener': obtener
    })
    

def add_vehiculo(request):
    form=frmVehiculoBomberos(request.POST or None)
    contexto={
        "form":form
    }
    if request.method=="POST":
        form=frmVehiculoBomberos(data=request.POST,files=request.FILES)
        if form.is_valid():
           form.save()
           messages.success(request,"Vehículo Agregado!")

           return redirect(to="gestion_vehiculos")
        
    

    return render(request,"app_bomberos/add_vehiculo.html",contexto)



def update_vehiculo(request,id):
    prod=get_object_or_404(AutoBombero,pk=id)
    form=frmVehiculoBomberos(instance=prod)
    #form.fields["id"].disabled=True
    contexto={
        "form":form
    }

    if request.method=="POST":
        form=frmVehiculoBomberos(data=request.POST,files=request.FILES,instance=prod)
        #form.fields["id"].disabled=False
        if form.is_valid():
            search=AutoBombero.objects.get(pk=prod.id)
            datos_form=form.cleaned_data
            search.patente=datos_form.get("patente")
            search.tipo_de_vehiculo=datos_form.get("tipo_de_vehiculo")
            search.imagen=datos_form.get("imagen")
            search.save()
            messages.success(request,"Vehículo Modificado!")
            return redirect(to="gestion_vehiculos")
        contexto["form"]=form
        
    return render(request,"app_bomberos/update_vehiculo.html",contexto)


def delete_vehiculo(request,id):
    v=get_object_or_404(AutoBombero,pk=id)
    contexto={
        "v":v
    }
    if request.method=="POST":
        v.delete()
        messages.success(request,"Vehículo Eliminado!")
        return redirect(to="gestion_vehiculos")

    return render(request,"app_bomberos/delete_vehiculo.html",contexto) 


def detail_vehiculo(request, id):
    v = get_object_or_404(AutoBombero, pk=id)
    form_mantencion = frmMantencionVehiculo(initial={'id_autobombero': v.id})

    if request.method == "POST":
        form_mantencion = frmMantencionVehiculo(request.POST)
        if form_mantencion.is_valid():
            form_mantencion.save(commit=False)
            form_mantencion.instance.id_autobombero = v
            form_mantencion.save()
            messages.success(request,"Mantención Agregada!")
            return redirect(to="index")

    contexto = {
        "v": v,
        "form_mantencion": form_mantencion,
    }
    return render(request, "app_bomberos/detail_vehiculo.html", contexto)