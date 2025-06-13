from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('login/', LoginView.as_view(
        template_name='acceso/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('gestion-usuarios/', views.gestion_usuarios, name='gestion_usuarios'),
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),
    path('editar-usuario/<int:user_id>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar-usuario/<int:user_id>/', views.eliminar_usuario, name='eliminar_usuario'),
]
