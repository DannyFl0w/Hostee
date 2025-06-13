from django.urls import path
from . import views

app_name = 'estadisticas'

urlpatterns = [
    path('', views.panel_gerente, name='panel_gerente'),
] 