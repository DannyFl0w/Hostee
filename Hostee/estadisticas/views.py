from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from acceso.views import es_gerente
from .models import EstadisticaRobot, AlertaRobot
from django.db.models import Avg, Sum, Count
from django.utils import timezone
from datetime import timedelta

@login_required
@user_passes_test(es_gerente)
def panel_gerente(request):
    # Aquí irá la lógica para obtener estadísticas del robot
    estadisticas = {
        'total_mesas': 10,
        'mesas_ocupadas': 5,
        'mesas_disponibles': 5,
        'total_usuarios': 3,
        'usuarios_activos': 2,
    }
    return render(request, 'estadisticas/panel_gerente.html', {'estadisticas': estadisticas})
