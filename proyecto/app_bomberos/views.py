from django.shortcuts import render, redirect, get_object_or_404
from .models import AutoBombero, MantencionVehiculo, Compañia
from .forms import frmVehiculoBomberos, frmMantencionVehiculo, frmMecanicoUser, frmLogin, frmCompañia
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import Group



# Create your views here.

def index(request):
    obtener = AutoBombero.objects.all()
    user_role = request.session.get('user_role', None)
    
    usuario_autenticado = request.user

    # Verificar si el usuario es un capitán y tiene una compañía asignada
    if usuario_autenticado.is_authenticated and usuario_autenticado.role == 'capitan' and usuario_autenticado.compañia:
        compañia_capitan = usuario_autenticado.compañia

        # Filtrar los vehículos por la compañía del capitán actual
        obtener = AutoBombero.objects.filter(compañia=compañia_capitan)
    else:
        # Si el usuario no es un capitán o no tiene una compañía asignada, mostrar todos los vehículos
        obtener = AutoBombero.objects.all()
    
    contexto = {
        'obtener': obtener,
        'user_role': user_role, 
    }
    return render(request, 'app_bomberos/index.html', contexto)


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
            search.clave=datos_form.get("clave")
            search.patente=datos_form.get("patente")
            search.tipo_vehiculo=datos_form.get("tipo_vehiculo")
            search.marca=datos_form.get("marca")
            search.modelo=datos_form.get("modelo")
            search.año=datos_form.get("año")
            search.nro_motor=datos_form.get("nro_motor")
            search.nro_chasis=datos_form.get("nro_chasis")
            search.compañia=datos_form.get("compañia")
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
    user_role = request.session.get('user_role', None)

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
        "user_role": user_role,
    }
    return render(request, "app_bomberos/detail_vehiculo.html", contexto)


def register_m(request):
    user_role = request.session.get('user_role', None)
    if request.method == 'POST':
        form = frmMecanicoUser(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            
            # Establecer la variable de sesión 'user_role' basada en el rol seleccionado
            user_role = form.cleaned_data.get('role')
            request.session['user_role'] = user_role
            
            # Asignar la compañía solo si el rol es "capitán"
            if user_role == 'capitan':
                compañia = form.cleaned_data.get('compañia')
                user.compañia = compañia
                user.save()
            messages.success(request,"Cuenta creada!")
            return redirect('index')  # Redirigir a la página de inicio después del registro
    else:
        form = frmMecanicoUser()
    
    contexto = {
        'form': form,
        'user_role': user_role,
    }
        
    return render(request, 'registration/register_m.html', contexto)




def login_custom(request):
    if request.method == 'POST':
        form = frmLogin(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                # Establecer la variable de sesión 'user_role' basada en el rol del usuario
                if user.role:
                    request.session['user_role'] = user.role
                else:
                    # Si el usuario no tiene un rol definido, puedes manejarlo de alguna manera
                    pass
                
                return redirect('index')  # Redirigir a la página de inicio después de iniciar sesión
    else:
        form = frmLogin()
    
    return render(request, 'registration/login_custom.html', {'form': form})



def logout_custom(request):
    logout(request)
    return redirect('index')  # Redirige a la página de inicio después de cerrar sesión


def compañia(request):
    form=frmCompañia(request.POST or None)
    contexto={
        "form":form
    }
    if request.method=="POST":
        form=frmCompañia(data=request.POST,files=request.FILES)
        if form.is_valid():
           form.save()
           messages.success(request,"Compañia Agregada!")

           return redirect(to="index")
       
    return render(request,"app_bomberos/compañia.html",contexto)



def historial_mantenciones(request):
    obtener = MantencionVehiculo.objects.filter(tipo_mantencion='Preventiva')
    user_role = request.session.get('user_role', None)
    
    contexto = {
        'obtener': obtener,
        'user_role': user_role, 
    }
    return render(request, 'app_bomberos/historial_mantenciones.html', contexto)


def historial_correctiva(request):
    obtener = MantencionVehiculo.objects.filter(tipo_mantencion='Correctiva')
    user_role = request.session.get('user_role', None)
    
    contexto = {
        'obtener': obtener,
        'user_role': user_role, 
    }
    return render(request, 'app_bomberos/historial_correctiva.html', contexto)



def historial_externo(request):
    obtener = MantencionVehiculo.objects.filter(tipo_mantencion='Externa')
    user_role = request.session.get('user_role', None)
    
    contexto = {
        'obtener': obtener,
        'user_role': user_role, 
    }
    return render(request, 'app_bomberos/historial_externo.html', contexto)







