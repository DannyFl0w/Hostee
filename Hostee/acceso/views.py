from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .forms import UserForm
from django.contrib.auth import login, authenticate, logout

def es_gerente(user):
    return user.groups.filter(name='Gerentes').exists()

def es_cajero(user):
    return user.groups.filter(name='Cajeros').exists()

def welcome(request):
    if request.user.is_authenticated:
        try:
            if es_gerente(request.user):
                return redirect('estadisticas:panel_gerente')
            elif es_cajero(request.user):
                return redirect('mesas:dashboard')
            else:
                messages.error(request, 'No tienes un rol asignado. Por favor, contacta al administrador.')
                return redirect('logout')
        except Exception as e:
            messages.error(request, f'Error al redirigir: {str(e)}')
            return redirect('logout')
    return render(request, 'acceso/welcome.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('login')

@login_required
def home(request):
    return redirect('mesas:dashboard')

@login_required
@user_passes_test(es_gerente)
def gestion_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'acceso/gestion_usuarios.html', {'usuarios': usuarios})

@login_required
@user_passes_test(es_gerente)
def crear_usuario(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            grupo = form.cleaned_data.get('grupo')
            if grupo:
                user.groups.add(grupo)
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('gestion_usuarios')
    else:
        form = UserForm()
    return render(request, 'acceso/crear_usuario.html', {'form': form})

@login_required
@user_passes_test(es_gerente)
def editar_usuario(request, user_id):
    usuario = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=usuario)
        if form.is_valid():
            user = form.save()
            grupo = form.cleaned_data.get('grupo')
            if grupo:
                user.groups.clear()
                user.groups.add(grupo)
            messages.success(request, 'Usuario actualizado exitosamente.')
            return redirect('gestion_usuarios')
    else:
        form = UserForm(instance=usuario)
    return render(request, 'acceso/editar_usuario.html', {'form': form, 'usuario': usuario})

@login_required
@user_passes_test(es_gerente)
def eliminar_usuario(request, user_id):
    usuario = User.objects.get(id=user_id)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado exitosamente.')
        return redirect('gestion_usuarios')
    return render(request, 'acceso/eliminar_usuario.html', {'usuario': usuario})