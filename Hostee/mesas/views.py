from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Mesa
from django.views.decorators.csrf import csrf_exempt
from .forms import MesaForm

def es_cajero(user):
    return user.groups.filter(name='Cajeros').exists()

@login_required
@user_passes_test(es_cajero)
def dashboard(request):
    mesas = Mesa.objects.all().order_by('numero')
    return render(request, 'mesas/dashboard.html', {'mesas': mesas})

@login_required
@user_passes_test(es_cajero)
def lista_mesas(request):
    mesas = Mesa.objects.all().order_by('numero')
    return render(request, 'mesas/lista_mesas.html', {'mesas': mesas})

@login_required
@user_passes_test(es_cajero)
def cambiar_estado_mesa(request, mesa_id):
    mesa = get_object_or_404(Mesa, id=mesa_id)
    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')
        if nuevo_estado in dict(Mesa.ESTADOS):
            mesa.estado = nuevo_estado
            mesa.save()
            messages.success(request, f'Estado de la mesa {mesa.numero} actualizado correctamente.')
        else:
            messages.error(request, 'Estado no válido.')
    return redirect('mesas:dashboard')

@csrf_exempt
@login_required
@user_passes_test(es_cajero)
def agregar_mesa(request):
    if request.method == 'POST':
        form = MesaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesa agregada exitosamente.')
            return redirect('mesas:dashboard')
    else:
        form = MesaForm()
    return render(request, 'mesas/agregar_mesa.html', {'form': form})

@csrf_exempt
@login_required
@user_passes_test(es_cajero)
def editar_mesa(request, mesa_id):
    mesa = get_object_or_404(Mesa, id=mesa_id)
    if request.method == 'POST':
        form = MesaForm(request.POST, instance=mesa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesa actualizada exitosamente.')
            return redirect('mesas:dashboard')
    else:
        form = MesaForm(instance=mesa)
    return render(request, 'mesas/editar_mesa.html', {'form': form, 'mesa': mesa})

@login_required
@user_passes_test(es_cajero)
def eliminar_mesa(request, mesa_id):
    mesa = get_object_or_404(Mesa, id=mesa_id)
    if request.method == 'POST':
        mesa.delete()
        messages.success(request, 'Mesa eliminada exitosamente.')
        return redirect('mesas:dashboard')
    return render(request, 'mesas/eliminar_mesa.html', {'mesa': mesa})