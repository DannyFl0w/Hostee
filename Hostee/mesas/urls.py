from django.urls import path
from . import views

app_name = 'mesas'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('lista/', views.lista_mesas, name='lista_mesas'),
    path('cambiar-estado/<int:mesa_id>/', views.cambiar_estado_mesa, name='cambiar_estado'),
    path('agregar/', views.agregar_mesa, name='agregar_mesa'),
    path('editar/<int:mesa_id>/', views.editar_mesa, name='editar_mesa'),
    path('eliminar/<int:mesa_id>/', views.eliminar_mesa, name='eliminar_mesa'),
]
